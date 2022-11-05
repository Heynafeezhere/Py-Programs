#Banking System Management

class BankingSystem(object):
    def __init__(self) -> None:
        super().__init__()
        self.toexit = False
        self.__details = []
        while self.toexit!=True:
            print("Select Your Choice:-")
            print("1.Create Account")
            print("2.Deposit")
            print("3.Withdrawl")
            print("4.Balance Check")
            print("5.Exit")
            choice = int(input())
            if choice==1:
                self.__createAccount()
            elif choice==2:
                self.__deposit()
            elif choice==3:
                self.__withdrawal()
            elif choice==4:
                self.__balanceCheck()
            elif choice==5:
                self.toexit = True
            else:
                print("!!!Invalid Option!!!")

    def __createAccount(self):
        name = input("Enter Your Name: ")
        age = int(input("Enter Your Age: "))
        self.bal = 0
        a = Account(name,age,self.bal)
        self.__details.append(a)
        print()
        print(a)
        print()
        print("Account Created Successfully!")
        print()

    def __deposit(self):
        accnum = input("Enter your account number: ")
        print()
        amount = int(input("Enter Deposit Amount: "))
        print()
        temp = -1
        for i in range(len(self.__details)):
            if self.__details[i].getAccNum() == accnum:
                temp = i
        if temp == -1:
            print("!!!!No Such Account!!!!")
            print()
        else:
            self.__details[temp].depositAmount(amount)
            print("Balance: ",self.__details[temp].getBalance())
            print()

    def __withdrawal(self):
        accnum = input("Enter Your Account No: ")
        print()
        amount = int(input("Enter Your Withdrawal amount: "))
        print()
        temp = -1
        for i in range(len(self.__details)):
            if self.__details[i].getAccNum() == accnum:
                temp = i
        if temp==-1:
            print("!!!No such Account!!!")
        else:
            print(self.__details[temp].withdrawalAmount(amount))

    def __balanceCheck(self):
        accnum = input("Enter Your Account No: ")
        print()
        temp=-1
        for i in range(len(self.__details)):
            if self.__details[i].getAccNum() == accnum:
                temp = i
        if temp==-1:
            print("!!!No such Account!!!")
        else:
            print("Balance: ",self.__details[temp].getBalance())
            print()


class Account(object):
    __nextnum = 1
    def __init__(self,name,age,bal) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.balance = bal
        self.accnum = Account.__nextnum
        Account.__nextnum += 1

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getAccNum(self):
        return "IOB-" + str(self.accnum)

    def getBalance(self):
        return self.balance

    def depositAmount(self,amount):
        self.balance += amount
    
    def withdrawalAmount(self,amount):
        if self.balance - amount>0:
            self.balance -= amount
            return "Balance:" + str(self.balance)
        else:
            return "!!!Insufficient Balance!!!"


    def __str__(self) -> str:
        return "Name:" + self.getName() + " " + "Account Num:" + self.getAccNum()



a = BankingSystem()


            