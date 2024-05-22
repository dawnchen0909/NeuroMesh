def min_subsequences(source, target):       
  i, minimum = 0, 1
  
  for c in target:
    i = source.find(c, i)
  
    if i == -1:
      i = source.find(c)
      minimum += 1
      
      if i == -1:
          return i
        
    i += 1
  
  return minimum
