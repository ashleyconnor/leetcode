class Solution:
    def merge_intervals(self, intervals):
        intervals.sort()
        interval_stack = [intervals.pop(0)]
        for index in range(0, len(intervals)):
            start, end = intervals.pop(0)
            stack_start, stack_end = interval_stack[-1]
            if start > stack_end:
                interval_stack.append([start, end])
            else:
                interval_stack[-1] = [stack_start, max(end, stack_end)]
        return interval_stack
