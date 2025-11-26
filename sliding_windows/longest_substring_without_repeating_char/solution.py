def find_longest_substring(input_str):
   max_size = 0
   count = {}
   left = right = 0
   
   while right < len(input_str):
      count[input_str[right]] = count.get(input_str[right], 0) + 1
      while count[input_str[right]] > 1:
         count[input_str[left]] -= 1
         left += 1
      window_size = right - left + 1
      max_size = max(max_size, window_size)
      right += 1

   return max_size
