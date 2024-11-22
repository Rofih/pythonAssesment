


class Account:
    balance = 0

    def __init__(self,name:str,phone:str,password:str):
        self.__name = name
        self.phone = phone
        self.__password = password
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def getBalance(self):
        return f'Mr {self.__name} your balance is {self.balance}'

    def withdraw(self, amount,pin):
        state = self.pinVerification(pin)
        if state:
            if amount > 0:
                if amount < self.balance:
                    self.balance = self.balance - amount
            return amount
        else :
            return 'invalid pin'
    def generateAccountNumber(self):
        return self.phone[1:]
    def pinVerification(self,pin):
        if self.__password == pin:
            return True
        else :
              state= False

