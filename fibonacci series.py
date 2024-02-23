def fibo(num):
    a=0
    b=1
    print(a)
    print(b)
    for num in range(2,num):
     c=a+b
     a=b
     b=c
     print(c)
     
    


num=10
fibo(num)