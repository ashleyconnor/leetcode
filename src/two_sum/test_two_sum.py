import pytest

from .solution import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "numbers,target,expected",
        [([2, 7, 11, 15], 9, (0, 1)), ([5, 4, 3, 10, 7], 12, (0, 4))],
    )
    def test_two_sum(self, numbers, target, expected):
        assert Solution().two_sum(numbers, target) == expected
