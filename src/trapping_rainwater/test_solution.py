import pytest

from .solution import Solution


class TestSolution:
    def test_trap(self):
        assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
        assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9
        assert Solution().trap([1, 2, 3, 4, 3, 2, 1]) == 0
        assert Solution().trap([1, 2, 3, 2, 2, 2, 3, 2, 1]) == 3
        assert Solution().trap([1, 2, 3, 1, 1, 3, 1, 1, 3, 2, 3]) == 9
