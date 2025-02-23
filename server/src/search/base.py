# server/src/search/base.py
# 抽象基类
from abc import ABC, abstractmethod
from typing import Optional

class SearchProvider(ABC):
    @abstractmethod
    def search(self, query: str, num_results: int = 3) -> Optional[str]:
        """搜索抽象方法"""
        pass

class DummySearch(SearchProvider):
    """空实现（保底策略）"""
    def search(self, query: str, num_results: int = 3) -> Optional[str]:
        return None