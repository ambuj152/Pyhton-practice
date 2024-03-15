class D2c():
 
 
 def __init__(self,num):
    self.num=num
    


 def ConvertD2C(self):
    l=[]
    rem=0
    if(num>1):
     while(num!=0):
            rem=num%2
            num= num//2
            
            l.append(rem)     
            
     print(l[::-1])


num=34
d1=D2c(num)
d1.ConvertD2C()
# ConvertD2C(34)

# def recmethod(num):
#     if(num>1):
#         recmethod(num//2)
#     print(num%2, end="")

# recmethod(65)