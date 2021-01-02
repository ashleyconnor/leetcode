import pytest

from .solution import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "haystack,needle,expected",
        [("hello", "", 0), ("hello", "ll", 2), ("aaaaa", "bba", -1)],
    )
    def test_str_str(self, haystack, needle, expected):
        assert Solution().str_str(haystack, needle) == expected
