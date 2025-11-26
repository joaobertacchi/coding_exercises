def insert_interval(existing_intervals, new_interval):
  output = []
  merging_interval = new_interval
  
  i = 0
  while i < len(existing_intervals) and existing_intervals[i][1] < merging_interval[0]:
    output.append(existing_intervals[i])
    i += 1
    
  if i == len(existing_intervals):
    output.append(merging_interval)
    return output
  
  a = existing_intervals[i]
  if merging_interval[1] < a[0]:
    output.append(merging_interval)
    output.append(a)
    i += 1
  else:
    merging_interval = [min(a[0], merging_interval[0]), max(a[1], merging_interval[1])]
  
    i += 1
    while i < len(existing_intervals) and merging_interval[1] >= existing_intervals[i][0]:
      a = existing_intervals[i]
      merging_interval = [min(a[0], merging_interval[0]), max(a[1], merging_interval[1])]
      i += 1
      
    output.append(merging_interval)
  
  while i < len(existing_intervals):
    output.append(existing_intervals[i])
    i += 1

  return output
