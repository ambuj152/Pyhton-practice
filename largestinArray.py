def largest(array):
 large=array[0]
 length=len(array)
 
 for i in range(0,length):
  
   if array[i]>large:

    large=array[i]
    

   
 print("the largest number is", large)






array=[1,3,2,10,7,8,9]

largest(array)