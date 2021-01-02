import pytest

from .solution import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "string,expected",
        [("abcabcba", 3), ("dvedf", 4), ("bbbbb", 1), ("qrsvbspk", 5)],
    )
    def test_lengthOfLongestSubstring(self, string, expected):
        assert Solution().lengthOfLongestSubstring(string) == expected
