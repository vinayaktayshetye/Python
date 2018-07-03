
# coding: utf-8

# In[4]:


#Vinayak Tayshetye
#Bank Application

accDetail = []
uniqueAcc = []
accNo = 0

def mainBank():    
    getInput()
     
    
def getInput():
    global accNo
    print("\nBank account application")
    print("1) Create new account")
    print("2) Credit/Debit an account")
    print("3) List all accounts")
    print("4) List account history")
    print("5) View total deposits with bank")
    print("6) Quit")    
    
    while True:
        num = eval(input("\nMake a selection from the options menu: "))
        if num == 1:
            print("\nCreating a new account...")
            print("Please enter the individuals")
            firstName = str(input("First Name: ")).title()
            lastName = str(input("Last Name: ")).title()
            bal = int(input("Beginning Balance (USD):"))
            accNo += 1
            account_number = createAcc(accNo, firstName, lastName, bal)
            print("New account created for {0:s} {1:s} (Account# {2:d})".format(firstName, lastName, account_number))                     
        elif num == 2:
            transcCrDb()           
        elif num == 3:
            listAllAcc()                    
        elif num == 4:
            accHistory()            
        elif num == 5:
            totalDeposits()
        elif num == 6:            
            print("\nThis will 'RESET' all the data. \nPlease confirm your action..!!!")
            ans = str(input("Enter Yes or No: "))            
            if ans.lower() == "yes" or ans.lower() == "y":
                print("\nYou have ended the session. \nThank you for using bank application")
                break                
        elif isinstance(num, str):
            print("You did not enter a proper number.")            
        else:
            print("You did not enter a proper number.")            
            
def createAcc(accountNo, firstName, lastName, bal):
    global uniqueAcc, accDetail 
    details = [accountNo, firstName, lastName, 0, bal]
    uniqueAcc.append(details)
    accDetail.append(details)
    return accountNo
 
def transcCrDb():
    print("\nCrediting/Debiting an account...")
    transcAcc = int(input("Please enter the account number: "))
    creditDebit = int(input("Enter '1 to Credit' and '2 to Debit' :"))
    transcAmt = int(input("Please enter the amount: "))    
    if creditDebit == 1:
        latestRec = 0
        for i in range(len(accDetail)):
            if transcAcc == accDetail[i][0]:
                latestRec = i   
            else:
                latestRec = latestRec                
        bal = (accDetail[latestRec][4]) + transcAmt
        details = [accDetail[latestRec][0], accDetail[latestRec][1], accDetail[latestRec][2], transcAmt, bal ]        
        accDetail.append(details)        
        print("{0:s} {1:s} (Account# {2:d}) credited ${3:.2f}".format(accDetail[latestRec][1],accDetail[latestRec][2],accDetail[latestRec][0], transcAmt))
        print("New balance : ${0:.2f}".format(bal))        
    else:
        latestRec = 0
        for i in range(len(accDetail)):
            if transcAcc == accDetail[i][0]:
                latestRec = i   
            else:
                latestRec = latestRec                
        bal = (accDetail[latestRec][4]) - transcAmt
        details = [accDetail[latestRec][0], accDetail[latestRec][1], accDetail[latestRec][2], -transcAmt, bal]
        accDetail.append(details)        
        print("{0:s} {1:s} (Account# {2:d}) debited ${3:.2f}".format(accDetail[latestRec][1],accDetail[latestRec][2],accDetail[latestRec][0], transcAmt))
        print("New balance : ${0:.2f}".format(bal))                              
            
def listAllAcc():
    j=0

    print("{0:<8s} {1:<10s} {2:<12s} ${3:<10s}".format("Acc.No.", "First Name", "Last Name", "Balance")) 
    
    while j <= len(accDetail):
        latestRec = 0
        i=0
        count = 0
        for i in range(len(accDetail)):
            
            if accDetail[i][0] == j:
                latestRec = i
                count += 1                             
        
        if count != 0:
            print("{0:^8n} {1:<10s} {2:<12s} ${3:<10,.2f}".format(accDetail[latestRec][0],accDetail[latestRec][1],accDetail[latestRec][2], accDetail[latestRec][4]))
           
        j += 1    

def accHistory():
    accountNo = int(input("\nEnter account number to display transaction history: "))
    print("\nTransaction history")
    print("{0:s} {1:>5s} ".format("Acc.No.", "Name"))
    for j in range(len(accDetail)):
        if accDetail[j][0] == accountNo:
            print("{0:03} {1:>12s} {2:s}".format(accDetail[j][0],accDetail[j][1],accDetail[j][2]) )
            break    
    print("\n{0:<10s} {1:<10s}".format("Current Bal", "Transaction Amt"))
    
    for i in range(len(accDetail)):
        if accDetail[i][0] == accountNo:
            print("${0:<10,.2f} ${1:<10,.2f}".format(accDetail[i][4], accDetail[i][3]))

def totalDeposits():
    j=0
    balances = []    
    while j <= len(accDetail):
        latestRec = 0
        i=0
        count = 0
        for i in range(len(accDetail)):            
            if accDetail[i][0] == j:
                latestRec = i
                count += 1
        if count != 0:
            balances.append(accDetail[latestRec][4])
        j += 1    
    print("Total deposits available with bank is ${0}:".format(round(sum(balances),2)))
                
def reset_list():
    global accDetail
    accDetail = [] 

def total_deposits():
    balances = []
    for account in accDetail:
        balance = 0
        for i in range(len(accDetail)):
            if account[0] == i:
                balance = account[4]
                balances.append(balance)
    return sum(balances)
            

#mainBank()

