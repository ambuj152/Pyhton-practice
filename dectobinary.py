def ConvertD2C(num):
    l=[]
    if(num>1):
     while(num!=0):
            rem=num%2
            num= num//2
            
            l.append(rem)     
            
     print(l[::-1])



ConvertD2C(34)

def recmethod(num):
    if(num>1):
        recmethod(num//2)
    print(num%2, end="")

recmethod(65)