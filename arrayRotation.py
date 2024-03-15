
class arrayRotation():
    def __init__(self,arr,k):
       self.arr=arr
       self.k=k
       
    def rotate_array(self):
     n = len(arr)
     
     rotated_arr = arr[-k:] + arr[:-k]
     print("Original array:", arr)
     print("Rotated array:", rotated_arr)

arr = [1, 2, 3, 4, 5,6]
k = 1
aR=arrayRotation(arr,k)
aR.rotate_array()





