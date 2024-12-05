Class Solution:
def getSecondLargest(self,arr):
  n=len(arr)
  if n<2:
    return -1
  first=second=float('-inf')
  for num in arr:
    if num>first:
      
