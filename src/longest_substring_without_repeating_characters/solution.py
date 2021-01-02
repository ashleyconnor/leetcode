class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = ""
        substring = ""
        max_substring_index = index = 0

        while index < len(s):
            letter = s[index]
            if letter in substring:
                max_substring_index += 1
                substring = s[max_substring_index:index]
                continue
            index += 1
            substring += letter
            if len(substring) > len(max_substring):
                max_substring = substring
        return len(max_substring)
