
def pallindrome(num):
    
     ambuj=str(num)

     if(ambuj ==ambuj[::-1]):
      return num
    
number=12321
if(pallindrome(number)):
 print("the number is pallindrome")
else:
  print("the is not pallindrome")