We are given an input array, tasks, where tasks[i] = [starti, endi
 ] represents the start and end times of n tasks. Our goal is to schedule these tasks on machines given the following criteria:
- A machine can execute only one task at a time.
- A machine can begin executing a new task immediately after completing the previous one.
- An unlimited number of machines are available.

Find the minimum number of machines required to complete these n tasks.

Constraints:
- n == tasks.length
- 1 ≤ tasks.length ≤10ˆ3
- 0 ≤ tasksi.start < tasksi.end ≤ 10ˆ4
