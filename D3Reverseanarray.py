class solution:
  def reverseArray(self,arr):
    i=0
    j=len(arr)-1
    while i<j:
      temp=arr[i]
      arr[i]=arr[j]
      arr[j]=temp
      i+=1
      j-=1
