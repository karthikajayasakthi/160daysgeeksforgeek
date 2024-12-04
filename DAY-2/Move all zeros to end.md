DAY-2
Move all zeros to end

PROGRAM:

class Solution:
    def pushZerosToEnd(self,arr):
        count=0
        leng= len(arr)
        for j in range(leng):
            if arr[j]!=0:
                arr[count]=arr[j]
                count+=1
        while count<leng:
            arr[count]=0
            count+=1

screenshots :
![Screenshot (419)](https://github.com/user-attachments/assets/df9ee811-938b-45f5-ae83-591666f32c52)


![Screenshot (418)](https://github.com/user-attachments/assets/71797fc1-d9be-4266-9962-b45bb37bd2f1)
