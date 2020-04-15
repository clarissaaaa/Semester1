# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 08:41:51 2019

@author: Clarissa
"""

class Account :
#class name starts with a capital letter 
    #make it private by putting double underscore
    __balance = 0 
    def __init__ (self,balance):
        self.__balance = balance 
        
    def getBalance(self):
        return self.__balance 
    
    def deposit(self, amt):
        if amt > 0 :
            self.__balance = self.__balance + amt
            return True
        else:
            return False 
    def withdraw(self, amt):
        try:
            if amt <= 0 :
                return False 
            else:
                self.__balance  -= amt 
                return True 
        except TypeError :
                return False

#myAccount = Account(0)
#myAccount.__balance = 100000
  # print(myAccount.getBalance())


class Customer :
    __fName = ''
    __lName = '' 
    __account = Account(0)
    
    def __init__ (self, fName, lName):
        self.__fName = fName 
        self.__lName = lName 
        self.__account = Account(0)
    
    def getFirstName(self):
        return self.__fName 
        
    def getLastName(self):
        return self.__lName
           
    def getAccount(self):
        return self.__account 
    
    def setAccount(self, acct):
        self.__account = acct
        
fName = input("Enter first name: ")
lName = input("Enter last name: ")
name = fName.title() + ' ' + lName.title() 
myCustomer = Customer(fName,lName)          
customer_list = []

class Bank :
    __customers = myCustomer
    __numberOfCustomer = len(customer_list)
    __bankName = ''
    
    def __init__(self, bankName):
        self.__customers = myCustomer
        self.__numberOfCustomer = len(customer_list)
        self.__bankName = bankName
    
    def BankName(self):
        return self.__bankName
    
    def addCustomer (self, myCustomer):
        customer_list.append(myCustomer)
        
    
    def getNumOfCustomers(self):
        return self.__numberOfCustomer
     
   # def getCustomer(self, myCustomer):
     #   return customer_list.index(myCustomer)

#Make a simple bank Menu
print("\n Bank option are:\n 1. BCA \n 2. Mandiri \n 3. BNI")
bank_opt = input("Choose your option: ")

myAccount = Account(0)
myCustomer.setAccount(myAccount)
myBank = Bank(bank_opt)
myBank.addCustomer(myCustomer)


def Menu():
    print("\n Welcome,", name) 
    print("\n Your transaction option are: \n 1. Deposit Money \n 2. Withdraw Money \n 3. Check Balance \n 4. Print customer list \n 5. Add customer \n 6. Change Bank \n 7. Quit bank system")
    return input ("Choose your option: ")


loop = 1 
while loop == 1:
    choice = Menu()
    if choice == '1':
        money = input("How much: RP. ")
        amt = int(money)
        myAccount.deposit(amt) 
        print("You have deposited RP.",amt, "of money")
    elif choice == '2':
        money = input("How much: RP. ")
        amt = int(money)
        myAccount.withdraw(amt)
        print("You have withdrawn RP.",amt, "of money")
    elif choice == '3':
        print ("Your current balance is: RP.", myCustomer.getAccount().getBalance())
    elif choice == '4':
        print("The total number of the customer for this bank: ", len(customer_list))
        print("Current customer/s name:")
        for c in customer_list:
            print (c.getFirstName() + ' ' + c.getLastName())
            
    elif choice == '5':
        fName = input("Enter first name: ")
        lName = input("Enter last name: ")
        name = fName.title() + ' ' + lName.title() 
        myCustomer = Customer(fName,lName) 
        myBank.addCustomer(myCustomer)
        
    elif choice == '6':
        print("\n Bank option are:\n 1. BCA \n 2. Mandiri \n 3. BNI")
        bank_opt = input("Choose your option: ")
        
        myAccount = Account(0)
        myCustomer.setAccount(myAccount)
        myBank = Bank(bank_opt)
        myBank.addCustomer(myCustomer)
        
    elif choice == '7':
        print("Thank you, have a nice day!")
        loop = 0