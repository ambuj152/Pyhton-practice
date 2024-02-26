class Prime:
    def __init__(self,num):
        self.number=num
    def calc_Prime(self):
        flag=0
        if self.number==1:
            print("the number is not valid")
        else:
          for i in range(2,self.number):
                if(self.number%i==0):
                 flag = 1
                 break 
          if flag:
              print("number is not prime")  
          else:
              print( self.number,"is prime")


s1=Prime(17)
s1.calc_Prime()
        