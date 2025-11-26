You are given two integer arrays, list1 and list2, sorted in non-decreasing order, and an integer, k.
A pair (u, v) is defined as one element u chosen from list1 and one element v chosen from list2.
Your task is to return the k pairs (u1, v1), (u2, v2), ...,(uk, vk) whose sums u1+v1, u2+v2, ..., uk+vk are the smallest among all possible such pairs.

Constraints:
- 1 ≤ list1.length, list2.length ≤ 500
- -10ˆ4 ≤ list1[i], list2[i] ≤ 10ˆ4
- 1 ≤ k ≤ 10ˆ3
- Input lists should be sorted in ascending order.
- If the value of k exceeds the total number of valid pairs that may be formed, return all the pairs.
