DAY-3
REVERSE ARRAY 

You are given an array of integers arr[]. Your task is to reverse the given array.

Solution :
class Solution:
    def reverseArray(self,arr):
        i=0
        j= len(arr)-1
        while i<j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i+=1
            j-=1

            
Screenshots :
![Screenshot (419)](https://github.com/user-attachments/assets/f074e65c-2a16-4837-acb5-4dca0ad62135)

![Screenshot (418)](https://github.com/user-attachments/assets/f95e60d2-7c5e-4ecf-be66-ef6a64e1d71e)

