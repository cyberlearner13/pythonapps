class Account:
    def __init__(self,filepath):
        self.filepath = filepath
        with open(filepath,'r') as file:
            self.balance = int(file.read())

    def withdraw(self,amount):
        if(amount>self.balance):
            print("Sorry! no overdraft facility")
        else:
            self.balance = self.balance - amount
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        
    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))



# account=Account("balance.txt")
# print(account.balance)
# account.withdraw(500)
# account.deposit(500)
# account.commit()
# print(account.balance)

class Checking(Account):
    type = "checking"
    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee = fee

    def transfer(self,amount):
        if(amount>self.balance):
            print("Sorry! Cannot transfer ! Insufficient balance")
        else:
            self.balance = self.balance - amount - self.fee

checking=Checking("balance.txt",1)
checking.transfer(20000)
checking.commit()
print(checking.balance)
print(checking.type)