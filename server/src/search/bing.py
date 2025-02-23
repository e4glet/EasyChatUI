# server/src/search/bing.py
# Bing实现
import os
import requests
from .base import SearchProvider
from loguru import logger
import json

class BingSearch(SearchProvider):
    def __init__(self):
        self.api_key = os.getenv("BING_API_KEY")  # 引擎密钥
        self.endpoint = "https://api.bing.microsoft.com/v7.0/search"
    
    def search(self, query: str, num_results: int = 3) -> str:
        try:
            headers = {"Ocp-Apim-Subscription-Key": self.api_key}
            params = {
                "q": query,
                "count": num_results,
                "responseFilter": "Webpages",
                "textDecorations": False,
                "textFormat": "Raw"
            }
            
            response = requests.get(self.endpoint, headers=headers, params=params)
            response.raise_for_status()
            
            results = []
            for item in response.json().get("webPages", {}).get("value", []):
                results.append({
                    "name": item.get("name"),
                    "snippet": item.get("snippet"),
                    "url": item.get("url")
                })
            
            return json.dumps(results, ensure_ascii=False)[:1500]
        except Exception as e:
            logger.error(f"Bing搜索失败：{str(e)}")
            return None