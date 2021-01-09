import pytest

from .solution import Solution


class TestSolution:
    def test_trap(self):
        assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
        assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9
