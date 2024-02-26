class Account:
    def __init__(self,balance,accNo):
        self.balance=balance
        self.accNo=accNo
    def debit(self,amount):
      self.balance=self.balance-amount
      print("RS",amount,"is debited")
      print("the remaining balance is",self.printBalance())

    def credit(self,amount):
      self.balance=self.balance+amount
      print("RS",amount,"is credited")
      print("the total balance is",self.printBalance())
      
    def printBalance(self):
       return self.balance
      

acc=Account(10000, 12345)
print( "your account number is",acc.accNo,"and the balance ammount is",acc.balance)
acc.debit(600)
acc.credit(1000)
acc.printBalance()