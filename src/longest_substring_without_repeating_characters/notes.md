# Notes

There are a few different ways to solve this problem.

I used the sliding window technique to only iterate through the string once. However I made
use of a string in order to store the characters which would allow me to produce the substring
and not only the length if required.

My first attempt was naiive and missed the test case `"dvedf"`, returning 3 instead of 4:

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = ''
        substring = ''

        for letter in s:
            if letter in substring:
                substring = letter
                continue
            substring += letter

            if len(substring) > len(max_substring):
                max_substring = substring
        return len(max_substring)
```

This solution incorrectly discards the entire substring when part of the substring could be part of the solution.

It was clear that I would need to keep track of where my substring started so I added `max_substring_index`.