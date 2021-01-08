# Notes

The trick here is to sort the intevals by start time.

We can then interate through the pairs with the knowledge that the start intervals are in ascending order.

Then merge intervals with each:

1. Push the first interval to a stack.
2. Pop an interval from the list of intervals.
3. Check the value at the top of the stack, if there is an overlap use the start time from the stack interval and the max end
   time from both intervals. Overwrite the top stack interval with this combined value. If there is no overlap simply push the interval to the stack.
4. Return this new stack.
