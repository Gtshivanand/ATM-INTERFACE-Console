"""  Interface to Controls Bank System And User's Interaction"""
from tkinter import messagebox
import string
import logging
logging.basicConfig(filename = "errors.txt",level=logging.ERROR)

class ManageDbm(object):
    """Base DataBase Manager,Controls The Opening And Closing Of The
    Bank's DataBase.Its __INIT__ Method Read(r) Or Write(w) Mode Of
    Opening A File As Its Argument And Then Opens The DataBase Using
    That Mode
    """
    def __init__(self,arg):
        self.arg = arg
        self.dict = open("database.txt",arg)
        

    """This Destructor Closes The Opened File InOrder To Facilitate
    Of Details Written On It So As Not To Lose Important Data
    """
    def __del__(self):
        self.dict.close()


class BankAcct(object):
    """THE __INIT__ METHOD OF THE BACNKACCT CLASS RECEIVES AN ATM PIN AS
    ARGUMENT,THEN SEARCHES THROUGH THE DATABASE TO CHECK IF THE PIN EXISTS
    AND THEN INITILIZES BANK DETAILS
    """
    account_name = list()
    def __init__(self,pin):
        self.__pin = pin
        self.__acct = ManageDbm("r")
        
        self.__dbm = self.__acct.dict.read().replace("\n","")
        self.DataBase = eval(self.__dbm)
        self.atmCash = self.DataBase[100000][2]

        
        """SEARCHES FOR SPECIFIED ACCT. PIN FROM THE DATABASE.
        IF FOUND,INITIALISES THE CLASS'S ACCT. NO,NAME AND ACCT. BALANCE.
        IF NOT FOUND IN THE DATABASE,RETURNS AN ERROR MESSAGE TO THE USER
        """
        name = BankAcct.account_name[-1]
        for key in self.DataBase:
            if self.__pin in self.DataBase[key] and name in self.DataBase[key]:
                self.AcctNo = key
                self.__name = self.DataBase[key][0]
                self.__bal = int(self.DataBase[key][2])
                break
    
    def CheckPin(self,name):
            """ Verifies If User's Pin Exists"""
            
            for key in self.DataBase:
              if (self.__pin in self.DataBase[key] and name in self.DataBase[key]):
                return True
            else: return False
            
    @staticmethod
    def CheckName(name):
        """Verifies If User's log-in name exists"""
        
        database = ManageDbm("r")
        dbm = database.dict.read().replace("\n","")
        DataBase = eval(dbm)
        database.dict.close()
        del database
       
        for key in DataBase:
            if name in DataBase[key]:
                BankAcct.account_name.append(name)
                return True
        else: return False

    @staticmethod
    def ResetPin(name,new):
        """Verifies If User's log-in name exists,If It Exists After Verification
        Updates The Customer's Pin With The Newly Randomly Selected Pin.
        """
        
        database = ManageDbm("r")
        db = database.dict.read().replace("\n","")
        del database
        DataBase = eval(db)
       
        for key in DataBase:
            if name in DataBase[key]:
                DataBase[key][1] = new
                break
        else: return False