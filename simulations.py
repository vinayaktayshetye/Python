
# coding: utf-8

# In[ ]:


from bankAccountTry4 import createAcc, total_deposits, reset_list, mainBank
from random import normalvariate

marketing_spend = 25000
interest_rate = 0.10
trials = 1000

### simulation for College students ###
avg_num_accounts_St = 1000
std_dev_accounts_St = 150
avg_balance_St = 3000
std_balance_St = 750

returns_on_investment_St = []
returns_on_investment_Sr = []

for trial in range(0,trials):
    reset_list()
    number_of_accounts_St = int(normalvariate(avg_num_accounts_St, std_dev_accounts_St))
    #Creating accounts
    for index in range(0, number_of_accounts_St):
        balance_of_account_St = normalvariate(avg_balance_St, std_balance_St)
        createAcc(index, "Tony", "Stark", balance_of_account_St)
    #Calculating the Expected Total Deposits for College students
    expected_total_deposits_St = total_deposits()
    #Calculating the return on investment Deposits for College students
    return_on_investment_St = (expected_total_deposits_St * interest_rate) - marketing_spend
    returns_on_investment_St.append( return_on_investment_St)

### Simulation for Senior Citizen ###
avg_num_accounts_Sr = 600
std_dev_accounts_Sr = 75
avg_balance_Sr = 10000
std_balance_Sr = 2500

for trial in range(0,trials):
    reset_list()
    number_of_accounts_Sr = int(normalvariate(avg_num_accounts_Sr, std_dev_accounts_Sr))
    #Creating accounts
    for index in range(0, number_of_accounts_Sr):
        balance_of_account_Sr = normalvariate(avg_balance_Sr, std_balance_Sr)
        createAcc(index, "Tony", "Stark", balance_of_account_Sr)
    #Calculating the Expected Total Deposits for Senior Citizen
    expected_total_deposits_Sr = total_deposits()
    #Calculating the return on investment for Senior Citizen
    return_on_investment_Sr = (expected_total_deposits_Sr * interest_rate) - marketing_spend
    returns_on_investment_Sr.append(return_on_investment_Sr)
    
print("Expected Totla deposits for:") 
print("College Students Plan:${0}".format(round(expected_total_deposits_St)))  
print("Senior Citizens Plan:${0}".format(round(expected_total_deposits_Sr)))
    
print("\nExpected Return on Investment for:") 
print("College Students Plan:${0}".format(round(sum(returns_on_investment_St)/trials)))  
print("Senior Citizens Plan:${0}".format(round(sum(returns_on_investment_Sr)/trials)))

# bankAccountTry1.start()

if returns_on_investment_St > returns_on_investment_Sr :
    print("\nThe bank management should focus on acquiring \nnew accounts for college students.")
else:
    print("\nThe bank management should focus on acquiring \nnew accounts for senior citizens.")
    
mainBank()


# In[11]:





# In[6]:




