Given a list, lists, containing m sorted lists of integers in ascending order, and an integer k, find the kth smallest element among all the lists.
Even if some values appear multiple times across the lists, each  kth smallest number.
If k exceeds the total number of elements across all lists, return the largest element among them. If the lists are empty, return 0.

Constraints:
- 1 ≤ m ≤ 50
- 0 ≤ lists[i].length ≤ 50
- −10ˆ9 ≤ lists[i][j] ≤ 10ˆ9
- 1 ≤ k ≤ 10ˆ9
