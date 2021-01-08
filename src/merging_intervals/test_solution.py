import pytest

from .solution import Solution


class TestSolution:
    def test_merge_intervals(self):
        assert Solution().merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
            [1, 6],
            [8, 10],
            [15, 18],
        ]
        assert Solution().merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
        assert Solution().merge_intervals([[6, 8], [1, 9], [2, 4], [4, 7]]) == [[1, 9]]
