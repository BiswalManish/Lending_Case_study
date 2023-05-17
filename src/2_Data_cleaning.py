#!/usr/bin/env python
# coding: utf-8

# # Part 2: Data Cleaning
# 
#     First we will separate categorical and numeric column
#     
#     Then we will convert some categorical column to numerical column and vice-a-versa
#     
#     Then prepare the data for final analysis
#     
#     

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#adding the path of the src dir to the notebook path
import sys
sys.path.insert(0, '/Users/manish/Documents/Projects/data_science/Lending_club_case_study/src')

import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.max_colwidth', 500)


# In[2]:


path = '/Users/manish/Documents/Projects/data_science/Lending_club_case_study/data/clean_data/loan_cleaned.csv'


# In[3]:


df = pd.read_csv(path)


# In[4]:


df.head()


# In[5]:


print(df.info())


# In[6]:


from functions import *


# In[7]:


#getting the unique values in each column
get_null_unique(df, df.columns)


# ### Actions to be done to respective columns
# 
#     loan_amnt, num, Bins of 10
#     funded_amnt_inv, num Bins of 10
#     funded_amnt, num, Bis of 10
#     term, cat, no action
#     int_rate, cat, remove trailing % and convert to num and bins of 10
#     installment, num, Bins of 10
#     grade, cat, no action
#     sub_grade, cat, no_action
#     emp_length, cat, convert to <=1, 1-5, 5-10 and 10+
#     home_ownership, cat, no action
#     annual_inc, num, Bins of 10
#     verifiaction_status, cat, no action
#     issue_d, cat, get months
#     loan_status, cat, no action
#     purpose, cat, no action
#     dti, num, Bins of 10
#     delinq_2yrs, num, no change, actually treat as categorical
#     earliest_cr_line, cat, get year
#     inq_last_6mths, num, no action, but treat as categorical
#     open_acc, num, bins of 10
#     pub_rec, num, no action, treat as categorical
#     revol_bal, num, Bins of 10
#     revol_util, cat, remove trailing % and convert to num and in bins of 10
#     total_acc, num, bins of 10
#     total_payment, num, bins of 10
#     total_pymnt_inv, num, bins of 10 or drop as redundant to total_payment
#     total_rec_prncp, num, bins of 10 or a redundant column can be dropped
#     total_rec_int, num, bins of 10
#     total_rec_late_fee, num, bins of 10
#     recoveries, num, bins of 10
#     collection_rec_fee, num, bins of 10 or can be dropped as seems redundant
#     last_pymnt_d, cat, convert to month
#     last_pymnt_amnt, num, bins of 10
#     last_credit_pull_d, cat, convert to year and month
#     pub_rec_bankruptcies, cat, no action

# def remove_trailing(df, col = None):
#     
#     
#     return df[col].applymap(lambda x: float(x.rstrip('%')))
# 
#     

# In[8]:


#resolving interest rate and revol_util
df[['int_rate', 'revol_util']] = remove_trailing(df,['int_rate', 'revol_util'] )
df[['int_rate', 'revol_util']].head()


# def to_bins(df, col = None):
#     
#     resolve = []
#     
#     k = max(df[col])/3
#     
#     
#     for x in df[col]:
#         
#         if x < k:
#             
#             z =  'new'
#         
#         elif x >= k and x <= 2 * k :
#             
#             z =  'mid'
#     
#         else:
#             z =  'old'
#         
#         resolve.append(z)
#         
#     return resolve
#     

# In[9]:


#converting the emp_length to bins
df.emp_length = df.emp_length.apply(lambda x : int(x.rstrip( '+ years').lstrip('<')))
df.emp_length = to_bins(df, 'emp_length')


# In[10]:


#resolving delinq_2yrs
df.delinq_2yrs.value_counts()


# In[11]:


#converting numerical columns to required categorical
convert_to_cat = ['delinq_2yrs', 'inq_last_6mths', 'pub_rec']
df[convert_to_cat] = df[convert_to_cat].applymap(lambda x : str(x))
df[convert_to_cat].head()


# In[12]:


#not keeping date wise columns 
date_wise = ['issue_d', 'last_pymnt_d', 'last_credit_pull_d', 'earliest_cr_line']


# In[13]:


df = df.drop(date_wise, axis = 1)


# In[14]:


#saving the processed dataframe to analysis file
#df.to_csv("loan_for_analysis.csv", sep = ',', index = False)


# ### Lets move to analysis file

# In[ ]:




