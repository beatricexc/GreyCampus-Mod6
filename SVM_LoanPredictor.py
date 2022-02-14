#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter # counter is used to sum categorical values 
import warnings 
warnings.filterwarnings("ignore")


# In[9]:


train_input = pd.read_csv(r"C:\Users\becel\Downloads\loan_pred_train.csv")
test_input  = pd.read_csv(r"C:\Users\becel\Downloads\loan_pred_test.csv")


# In[14]:


print(train_input.columns)


# In[13]:


print(test_input.columns)


# In[15]:


# in train data - dep var is loan status
# in test data - dep var is outcome
# we have to se them as per the data as we notice that the last var is changed in both
# making the names the same and them merging them together
# we can now fill the missing values simultaneously 
all = pd.concat([train_input, test_input], axis = 0) #axis = 0 is to ensure we have all columns within one data frame, the
                                                     # one unit called as "all"
#this is equal to rbind
all.shape


# In[21]:


all. tail
#all.reset_index (inplace = True, drop = True)
# we reset index because we combined the two data sets (train + test)
# which gives unique number to all the indexes


# In[25]:


# finding all missing and null values
all.isnull().sum()


# In[29]:


Counter(all['Gender'])


# In[32]:


# we now fill them with male
all[all['Gender'].isnull()].index.tolist()

# these rows are for gender
# fill the moodel with male
gender_null = all[all['Gender'].isnull()].index.tolist()
gender_null


# In[34]:


all['Gender'].iloc[gender_null]= "Male"


# In[36]:


# checking if they're filled or not 
sum(all['Gender'].isnull())
Counter(all['Gender'])


# In[39]:


# checking the Married column and filling it out

Counter(all['Married'])
#Let's fill themn with Yes if they have dependencies and with NO if not
pd.crosstab(all['Married'].isnull(), all['Dependents'].isnull())


# In[41]:


married_null = all[all['Married'].isnull()].index.tolist()
#these are the 3 rows where marries is null
married_null


# In[42]:


all['Married'].iloc[married_null] = "Yes"


# In[44]:


all.isnull().sum()


# In[45]:


# counter is equal tu table if it is 1D
Counter(all['Dependents'])

#545 have 0 depen, 160 have 1 dep only 


# In[46]:


pd.crosstab(all['Married'], all ['Dependents'].isnull())


# In[48]:


pd.crosstab(all['Dependents'], all['Married'])


# In[51]:


# finding all the indexes of all rows with dependents missing and Married as NO 

bachelor_nulldependent = all[(all['Married'] == "No") & (all['Dependents'].isnull())]
bachelor_nulldependent


# In[52]:


Counter(all['Dependents'])


# In[54]:


# checking the gender of dependents

pd.crosstab(all['Gender'], all['Dependents'])


# In[56]:


all['Gender'].iloc[all[all['Dependents'].isnull()].index.tolist()]


# In[57]:


# filling the values with the males
pd.crosstab(all['Gender'], all['Dependents'])


# In[62]:


# filling the dependents with 1
all['Dependents'].iloc[all[all['Dependents'].isnull()].index.tolist()] = "0"


# In[60]:


all.isnull().sum()


# In[63]:


Counter(all['Self_Employed'])


# In[64]:


self_emp_null = all[all['Self_Employed'].isnull()].index.tolist()


# In[65]:


# filling missing values with NO
all['Self_Employed'].iloc[self_emp_null]= "No"


# In[66]:


all.isnull().sum()


# In[67]:


pd.crosstab(all['LoanAmount'].isnull(), all['Loan_Amount_Term'])


# In[68]:


all.groupby(all['Loan_Amount_Term'])['LoanAmount'].mean()


# In[ ]:




