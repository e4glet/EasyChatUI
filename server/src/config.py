# server/src/config.py
# 配置管理
import os
from pathlib import Path
from typing import Type
from search.base import SearchProvider, DummySearch
from search.bing import BingSearch

class Config:
    # 通过环境变量切换搜索引擎
    SEARCH_PROVIDER: Type[SearchProvider] = BingSearch if os.getenv("USE_BING") else DummySearch
    MAX_SEARCH_RESULTS = 3
    
    @classmethod
    def get_search_provider(cls) -> SearchProvider:
        """工厂方法创建实例"""
        return cls.SEARCH_PROVIDER()