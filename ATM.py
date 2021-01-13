#  This software delveloped by Badr Alharbi for Demonstration of ATM
#  You can do what ever you want in this application on your responsability 
#  For Use 1231 to access the ATM menu
#  Transfare some money you can use this account with out qouts '1600000363600770' 

import time

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
WHITE = '\033[37m'

currentBalance = 1000.0
disposedValue = 0.0
newBalance = 0.0
OpenDrawer = False
disposeDoorIsopen = False
customerPin = '1231'
targtedAccount='1600000363600770'
systemStatus=1
systemexit=False
session=False
customerEntry=''

def chckPin():
    global systemStatus,customerEntry,session
    if not session:
        customerEntry=input('Please Enter you PIN ..\n')
    if customerEntry == customerPin:
        session=True
        userMenu()
    else:
        systemStatus+=1        
        print(f'{YELLOW}Sorry! please Enter Your PIN {systemStatus}')

def userMenu():
    global systemexit
    print(f"""{WHITE}
    Welcome To National Bank
    -------Please -----------------

    [W]ithdraw
    [D]eposit
    [T]ransfare
    [B]Display Balance
    [E]xit 
    """ 
          )
    time.sleep(1)
    userEntry = input(f'Select the requiered service {GREEN}')
    if userEntry.upper() == 'W':
        withdraw()
    elif userEntry.upper() == 'D':
        deposit()
    elif userEntry.upper() == 'T':
        transfare()
    elif userEntry.upper() == 'B':
        activeCurrentBalance(currentBalance)
        time.sleep(1.5)
    elif userEntry.upper() == 'E':
        exitSystem() 
    elif userEntry.upper()=='R':
        userMenu()
    else:
        exitSystem() 
    chkUserOption()

def chkUserOption():
    global session
    checkagain=input(f'{YELLOW}Do you need other service? {GREEN} Y/N ')
    if checkagain.upper()=='Y' and session:
        userMenu()
    else:
        exitSystem()

def activeCurrentBalance(currentBalance):
    print(f'{WHITE}Your current Balance is {GREEN}{currentBalance}.')

def withdraw():
    global currentBalance,OpenDrawer
    time.sleep(1.5)
    activeCurrentBalance(currentBalance)
    withdrawEntry = float(input(f'Please enter the requiered amount {GREEN} '))
    if (withdrawEntry <= currentBalance):
        time.sleep(1.5)
        print(f'{YELLOW}Please Wait Door Is openning')
        OpenDrawer = True
        time.sleep(1.5)
        print(f'{YELLOW}Please take your money')
        OpenDrawer = False
        currentBalance = currentBalance-withdrawEntry
        time.sleep(1.5)
        activeCurrentBalance(currentBalance)
        time.sleep(1.5)
    else:
        print(f'{RED}Sorry you have insufficient fund!')
        time.sleep(1)


def deposit():
    global currentBalance,disposeDoorIsopen
    disposeDoorIsopen=True
    trail=0
    time.sleep(1.5)
    print(f'{YELLOW}The door is opening...')
    i=0
    while disposeDoorIsopen:

        ReadIsertedMoney=float(input(f'{GREEN}Please insert money of 50,100,500 class \n'))
        if (ReadIsertedMoney % 50 == 0):
            
            confirm=input(f'You will dispost {GREEN}{ReadIsertedMoney} {WHITE}To confirm Press Y ')
            if confirm.upper()=='Y':
                time.sleep(1)
                print(f'A {GREEN}{ReadIsertedMoney} {WHITE}Riyal was successfully diposted ')
                currentBalance=ReadIsertedMoney+currentBalance
                disposeDoorIsopen =False
        else:
            i+=1
            print(f'{YELLOW}Please You need to insert money of 50,100,500 class ')
            if i==3:
                break
    time.sleep(1.5)
    activeCurrentBalance(currentBalance)

def transfare():
    global currentBalance
    targtedAcc = input(f'Please enter the beneficiary account {GREEN}')
    if targtedAcc==targtedAccount:
        transfarredAmount = float(input(f'Please Enter The money to be transfared.{GREEN}\n'))
        if transfarredAmount<=currentBalance:
            currentBalance=currentBalance-transfarredAmount
            print(f'A {GREEN}{transfarredAmount} {WHITE} was transferred to {GREEN} {targtedAccount} ')
        else:
            print (f'{YELLOW}Sorry you have insuffecint fund')
            readUserEntry=input(f'To Dipost money Enter {GREEN}[D] {WHITE} Or any key to Exit trasfare')
            if (readUserEntry.upper()=='D'):
                deposit()


def exitSystem():
    global systemexit
    print(f'{WHITE} Thank you for visting.... ')
    systemexit=True 


while systemStatus<5 and not systemexit:
    chckPin()
if systemStatus==5:
    exitSystem()