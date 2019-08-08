class Solution:
    def twoSum(self, nums, target):
        visited_nums = {}
        for i in range(len(nums)):
            target_minus_element = target - nums[i]

            if target_minus_element in visited_nums:
                return visited_nums[target_minus_element] , i

            visited_nums[nums[i]] = i

# Solution().twoSum([2,7,11,15], 9)