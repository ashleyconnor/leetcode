# Notes

This solution involves creating a dictionary where the key is the value
of each number processed and the value is the index of that number.

This allows easy O(1) lookup when processing the current number as we can
find the desired (target_minus_element) number by calculating the
(target - current) and then checking if that number is available in our dictionary.

If it is available we fetch the index using that number and return that
and the current index which point to values that equal our target number.

This solution runs in O(n) time and uses O(n) space
