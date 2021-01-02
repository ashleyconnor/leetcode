import pytest

from .solution import LRUCache


class TestSolution:
    def test_LRUCache(self):
        cache = LRUCache(2)
        assert cache.get(2) == -1
        assert not cache.put(2, 6)
        assert cache.get(1) == -1
        assert not cache.put(1, 5)
        assert not cache.put(1, 2)
        assert cache.get(1) == 2
        assert cache.get(2) == 6
