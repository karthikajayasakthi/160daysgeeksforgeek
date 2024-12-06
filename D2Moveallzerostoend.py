class solution:
  def pushZerosToEnd(self,arr):
    count=0
    leng=len(arr)
    for j in range(leng):
      if arr[j]!=9:
        arr[count]=arr[j]
        count+=1
    while count<leng:
      arr[count]=0
      count+=1
