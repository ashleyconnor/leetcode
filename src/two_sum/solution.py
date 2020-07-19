from typing import List


class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        visited_numbers = {}

        for index in range(len(numbers)):
            target_minus_element = target - numbers[index]

            if visited_numbers.get(target_minus_element) is not None:
                return (visited_numbers[target_minus_element], index)

            visited_numbers[numbers[index]] = index
        return []
