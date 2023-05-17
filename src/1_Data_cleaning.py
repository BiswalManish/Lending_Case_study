#!/usr/bin/env python
# coding: utf-8

# # Part 1: Data Cleaning
# 
# 
#     Business Objectives
#     
#     This company is the largest online loan marketplace, facilitating personal loans, business loans, 
#     and financing of medical procedures. Borrowers can easily access lower interest rate loans through
#     a fast online interface. 
#     
#     The company wants to understand the driving factors (or driver variables) behind loan default,
#     i.e. the variables which are strong indicators of default.  The company can utilise this knowledge 
#     for its portfolio and risk assessment. 
#     
#     We have to do univariate and multivariate analysis to find the risky indiacators.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#adding the path of the src dir to the notebook path
import sys
sys.path.insert(0, '/Users/manish/Documents/Projects/data_science/Lending_club_case_study/src')

from functions import *

import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.max_colwidth', 1000)


# In[2]:


#creating a path variable for the .csv file
path = '/Users/manish/Documents/Projects/data_science/Lending_club_case_study/data/raw_data/loan.csv'


# In[3]:


#reading the .csv file to a pandas dataframe instance
loan = pd.read_csv(path)
loan.head()


# In[4]:


#Basic info
loan.info()


# The data has `111` columns, with `74` float type, `13` int type and `24` categorical type columns.
# The data has a total of `39717` entries.
# 
# 
# The data is too big to find the identifiers directly, we have to choose the relevant columns.
# But before that lets check the missing values in the columns
# 
# The target column or y is `loan_status`. Lets check the column

# In[5]:


#loan status
print('loan_status missing entries: ' ,loan.loan_status.isnull().sum())
print('---'*10)
print(f'''loan_status categories: 
{loan.loan_status.value_counts()}
''')


# ### Loan status analysis

# In[6]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


#some plots to check the loan status column

plt.figure(figsize = (12,6) )


plt.subplot(1,2,1)
sns.countplot(x = loan.loan_status, )
sns.set_style('whitegrid')



plt.subplot(1,2,2)
plt.pie(loan.loan_status.value_counts(), labels = loan.loan_status.unique(), autopct = '%.2f%%')


plt.show()


# There are `0` missing entries in the target columns and `5627` defaulted loans, `32950` have fully paid loan status and `1140` loans are ongoing. We have to analyze the defaulters.
# 
# Lets get the data for only those who have either defaulted or fully paid

# In[8]:


loan = loan[loan.loan_status != 'Current']
loan.shape


# In[9]:

#Missing value initially
get_null_unique(loan, loan.columns)


#getting null column lists and % of missing values in it
Null_counts = get_Null_counts(loan)


# In[10]:


#checking the columns count with % of missing values
print(Null_counts.value_counts(ascending = False))


# The data has huge number of columns `>50` that `100%` missing values. We can absolutely drop them
# 1 column has `97.2 %`, and 1 has `97.13%` missing values. We can drop them as well.
# 
# 
# Also 1 column seems to have `65%` and other has `32.6%` missing values we can drop these and still have
# `53` columns to work with

# In[11]:


#getting the list of all these columns
Drop_columns_cent_percent = Null_counts.index[Null_counts.values == 100]


# In[12]:


print(list(Drop_columns_cent_percent))


# In[13]:


loan.shape


# In[14]:


#dropping null columns
loan = loan.drop(columns = Drop_columns_cent_percent, axis = 1)
loan.shape


# In[15]:


#updating Null_counts
Null_counts = get_Null_counts(loan)


# In[16]:


Rest_all_high_missing_value_columns = Null_counts.index[Null_counts.values > 30]
print(list(Rest_all_high_missing_value_columns))


# In[17]:


#Dropping these columns
loan = loan.drop(Rest_all_high_missing_value_columns, axis = 1)
loan.shape


# In[18]:


#Updating null counts
Null_counts = get_Null_counts(loan)


# In[19]:


print(Null_counts)


# We have dropped all the columns with `100%` missing values.
# We have all the columns with more than `30%` missing values.
# Lets check the rest of the null columns
# 

# In[20]:


#making a list of remaining null columns
Remaining_nulls = list(Null_counts[Null_counts.values > 0].index)


# In[21]:


loan.loc[:, Remaining_nulls]


# In[22]:


#creating the dictionary file path
dict_path = '/Users/manish/Documents/Projects/data_science/Lending_club_case_study/data/raw_data/Data_Dictionary.xlsx'


# In[23]:


dict_df = pd.read_excel(dict_path)


# In[24]:


dict_df[dict_df.LoanStatNew.isin(Remaining_nulls)]


# In[25]:


Null_counts[Remaining_nulls]


# In[26]:


Remaining_nulls


# In[27]:


#looking at null_values
get_null_unique(loan, Remaining_nulls)


#     emp_title is irrelevant as it has 4637 unique entries. It is better to drop these columns
#     
#     title can also be dropped citing the same issue
#     
#     revol_util is an imp column and has 0.28 nan values and we can drop these values
#     
#     collections_12_mths_ex_med, chargeoff_within_12_mths, tax_liens are not useful as they 
#     have only 0 or nan values
#     
#     we can drop the null entries from remaining columns

# In[28]:


#dropping the non-useful columns
loan = loan.drop(columns = ['emp_title', 'title', 'collections_12_mths_ex_med',
                    'chargeoff_within_12_mths', 'tax_liens'], axis = 1)


# In[29]:


#dropping null entries
loan = loan.dropna(subset = ['emp_length', 'revol_util', 'last_pymnt_d', 
                      'last_credit_pull_d', 'pub_rec_bankruptcies'], axis = 0)


# In[30]:


#now we have treated missing values
loan.isnull().sum()


# In[31]:


loan.columns


# In[32]:


#Lets get closer look at remaining columns
get_null_unique(loan, loan.columns)


# The above analysis shows that there are some columns with too many unique values that are not essential in finding the defaulters and some with only 1 unique value which is also not useful.

# In[33]:


#list_of_columns that have too many or 1 unique entry which are irrelevant

ls_unnecessary = ['id', 'member_id', 'pymnt_plan', 'url', 'out_prncp_inv',
                 'url', 'zip_code', 'addr_state', 'initial_list_status',
                 'out_prncp', 'policy_code', 'application_type',
                 'acc_now_delinq', 'delinq_amnt']


# In[34]:


#dropping these columns
loan = loan.drop(columns = ls_unnecessary, axis = 1)


# In[35]:


#Lets check rest columns
get_null_unique(loan, loan.columns)


# In[36]:


loan.shape


# In[37]:


#Now we will use these columns for further data cleaning
#lets save the clean data to a csv file

#loan.to_csv('loan_cleaned.csv', sep = ',', index = False)


# ### Lets get to part 2 of data cleaning
