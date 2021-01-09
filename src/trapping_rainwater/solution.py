from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        total = 0
        left_max = []
        right_max = []

        for index, height in enumerate(heights):
            if index == 0:
                left_max.append(height)
            else:
                left_max.append(max(left_max[index - 1], height))

        for index, height in reversed(list(enumerate(heights))):
            if index == len(heights) - 1:
                right_max.append(height)
            else:
                right_max.insert(0, max(right_max[(index + 1) - len(heights)], height))

        for index, height in enumerate(heights):
            total += min(right_max[index], left_max[index]) - height
        return total
