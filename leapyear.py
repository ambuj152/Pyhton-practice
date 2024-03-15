class isleap:

    def __init__(self,num):
        self.num=num


    def leapyear(self):
        if(num%4==0 and num/100 and num/400):
          print(num,"the year is leap year")
        else:
            print("year is not leap year")

        


num=2008
leap=isleap(num)
leap.leapyear()