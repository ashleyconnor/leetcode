import pytest

from .solution import Solution


class TestSolution:
    def test_number_of_islands(self):
        grid_one = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]

        grid_two = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]

        assert Solution().number_of_islands(grid_one) == 1
        assert Solution().number_of_islands(grid_two) == 3
