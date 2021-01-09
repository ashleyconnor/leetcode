# Notes

This one was pretty difficult. I ended up on a wild goose chase that resulted in the following erronuous code.

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        rainwater = 0
        left_index = 0

        if len(height) < 3:
            return 0

        while left_index < len(height):
            if left_index == 0 and height[1] > height[0]:
                left_index += 1
                continue

            tmp_rainwater = []
            right_index = 0

            while right_index < len(height):
                if right_index == (len(height) - 1) and height[-1] < height[-2]:
                    # print("Skipping right edge")
                    right_index += 1
                    continue
                if right_index <= left_index:
                    right_index += 1
                    continue

                if height[right_index] >= height[left_index]:
                    # print(f"Left Column Index: {left_index}")
                    # print(tmp_rainwater)
                    # print(f"Right Column Index: {right_index}")
                    for water in tmp_rainwater:
                        # print("Height L",  height[left_index])
                        # print("Height R", height[right_index])
                        # print("Rainwater collected", (min(height[right_index], height[left_index]) - water))
                        rainwater += (
                            min(height[right_index], height[left_index]) - water
                        )
                    left_index = right_index
                    tmp_rainwater = []
                else:
                    # print("Adding water to dish", height[right_index])
                    tmp_rainwater.append(height[right_index])
                right_index += 1
            left_index += 1
        return rainwater
```

I was clearly overthinking the problem with the actual solution resulting in much simpler code.

The solution is to effectively find the largest height to both the left and the right of each height in the list.

In a more naive solution this is done for each height resulting in a O(n^2) time complexity.

The secret to make this solution linear is to simply precalculate the max height to the left and right for each node in a single
pass. This allows us to simply reference the max left and right heights in a single pass through the initial list.

Storing this information is not free though and so the space complexity increases to O(n) but the time complexity is reduced to O(3n) or O(n).
