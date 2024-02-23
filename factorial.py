def fact(num):
    factorial=1
    
    while num > 0:
      factorial *=num
      num-=1
    
    print( "factorial is ",factorial)

num = 5
fact(num)
