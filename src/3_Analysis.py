#!/usr/bin/env python
# coding: utf-8

# # Part 3: Analysis
# 
#     In this notebook we will do univariate and bi-variate analysis.
#     We will check out distribution of each categorical col
#     Then we will check distribution of numerical col
#     Then we will check cat and num cols with the loan status
#     Then we will check interdependencies of cat-cat or cat-num or num-num

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from functions import *
from plots import *

import warnings
warnings.filterwarnings('ignore')

#adding path of our function and plot files in dir src and data files in dir cleaned_data
import sys
sys.path.insert(0, '/Users/manish/Documents/Projects/data_science/Lending_club_case_study/src')


pd.set_option('display.max_colwidth', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)


# In[2]:


path = '/Users/manish/Documents/Projects/data_science/Lending_club_case_study/data/clean_data/loan_for_analysis.csv'


# In[3]:


df = pd.read_csv(path)


# In[4]:


df.head()


# In[5]:


#dividing to categorical and numerical columns

cat_cols = list(df.columns[df.dtypes == 'object'])
num_cols = list(df.columns[df.dtypes != 'object'])


# ## 1. Univariate Analysis
# 

# In[6]:





# In[7]:




# ### 1.1 Categorical columns

# In[8]:


#showing some categorical plots
plot_categorical(df)


# ### 1.2 Numerical columns

# In[9]:


# some plots for numerical cols
plot_numerical(df)


# ## 2.Bivariate analysis
# 

# ### 2.1 Categorical columns vs loan_status

# In[10]:


plot_categorical(df, hue = 'loan_status')


# In[11]:


plot_numerical(df, y ='loan_status')


# #### Observations: 
# 
#     Categorical columns
# 
#     1. Term is an important factor for determining the defaulters. If the term of loan is 60 months they are more likely to default than fully pay. Although both terms have similar counts of defaulters
# 
#     2. Proportions of defaulters to fully paid is most when grade is C, followed by D and E. Although grade B loans are most in count.
#     
#     3. Proportions of people with employment length of more than 7 years are more  likely to default than fully pay.
#     
#     4. Proportion of people with mortgage are more likely to default. But number of defaulters who have rented property are more in count.
#     
#     5. Proportions of verified loan defaulters are more although non-verified and verified loans are equal in numbers.
#     
#     6. loan for the purpose of debt_consolidations have higher proportions of defaulters. Followed by those in others category and credit card loans.
# 
#      Numerical columns - 
# 
#     1. The median loan amount for both defaulters and fully paid are similar to 10k USD.The third quartiles and outliers amount are more in defaulters than fully paid loans.
# 
#     2. funded_amnt and funded_amnt_inv have similar readings to that of loan amnt, so we will not further use them in analysis.
#     
#     3. Interest rate is a distinctor for defaulters, who have higher median int_rate than those who have fully paid their loans.
#     
#     4. Annual income, delinq_2yrs, have huge outliers which have to correct
#     
#     5. Revol_util is an important indiactor as it has a s higher median for defaulters.
#     
#     6. Total_payment is as such not that useful, we have to look at the balance and int_rate along with annual
#     income of such individuals to get a clear picture.
#     
#     
#     
#     Out of the 23 numerican cols:
#     
#         - we can check the following against:
# 
# `'loan_amnt', 'int_rate', 'annual_inc', 'installment', 'revol_bal', 'revol_util', 'dti', 'total_pymnt'` 
# 
#     Out of the categories:
#         
#         -we can check the following:
# `'term', 'grade', 'purpose', 'emp_length', 'home_ownership', 'verification_status'`

# In[8]:


final_cat = ['term', 'grade', 'purpose', 'emp_length', 'home_ownership', 'verification_status']
final_num = ['loan_amnt', 'int_rate', 'annual_inc',
             'installment', 'revol_bal', 'revol_util',
             'dti', 'total_pymnt']


# ### 2.3 analysis of categorical columns over various numerical cols with loan status

# In[9]:





# In[10]:


    
    
    
    
                  
            
    
    


# In[11]:


    


# #### 2.3.1 Loan amount

# In[16]:


#Loan_amnt vs various categories
draw_pivot(df, 'loan_amnt')


# In[17]:


#Loan_amnt vs purpose

get_pivot_plots(data = df, num = 'loan_amnt', cat = 'purpose', palette = 'tab20c') 


# In[18]:


# Loan amount vs grade
get_pivot_plots(data = df, num = 'loan_amnt', cat = 'grade', palette = 'tab20c')


# In[19]:


#loan amount vs home_ownership
get_pivot_plots(data = df, num = 'loan_amnt', cat = 'home_ownership')


# In[20]:


#loan amount vs verification_status
get_pivot_plots(df, 'loan_amnt', 'verification_status')


# In[21]:


#loan_amnt vs emp_length
get_pivot_plots(df, 'loan_amnt', 'emp_length')


# #### 2.3.2 Interest rates

# In[22]:


#Interest vs various categories
draw_pivot(df, 'int_rate')


# In[23]:


#int_rate vs term
get_pivot_plots(df, 'int_rate', 'term')


# In[24]:


#int_rate vs purpose
get_pivot_plots(df, 'int_rate', 'purpose', palette = 'tab20c')


# In[25]:


#int_rates vs emp_length
get_pivot_plots(df, 'int_rate', 'emp_length')


# In[26]:


#int_rates vs verification_status
get_pivot_plots(df,'int_rate', 'verification_status')


# In[27]:


#int_rate vs home_ownership
get_pivot_plots(df, 'int_rate', 'home_ownership')


# #### 2.3.3 Annual_inc
# 

# In[12]:


draw_pivot(df, 'annual_inc')


# In[13]:


for i in final_num:
    get_pivot_plots(df, 'annual_inc', i)


#     From all the sub categories in categories the median annual income is always low for those who are charged 
#     off to those who have fully paid.
# 
#     Also the annual income has huge outliers so will not print the distribution plots

# #### 2.3.4 Revol_util

# In[29]:


draw_pivot(df, 'revol_util')


# In[30]:


for i in final_cat:
    get_pivot_plots(df, 'revol_util', i)


# #### 2.3.5 Installments

# In[31]:


draw_pivot(df, 'installment')


# In[32]:


for i in final_cat:
    get_pivot_plots(df, 'installment', i)


#     Installments are simialar for various sub categories of the categories for those who are charged off to those who have fully paid.
#     
#     But among the sub categoris the installment amount is different.
#     
#     This indicator is inconclusive and only feedback is that various sub categories have different
#     median installments

# #### 2.3.6 dti

# In[33]:


draw_pivot(df, 'dti')


# In[34]:


for i in final_cat:
    get_pivot_plots(df, 'dti', i)


# #### 2.3.7 Revol_bal

# In[35]:


draw_pivot(df, 'revol_bal')


# In[36]:


for i in final_cat:
    get_pivot_plots(df, num = 'revol_bal', cat = i)


# #### 2.3.8 total_pymnt

# In[37]:


draw_pivot(df, 'total_pymnt')


# In[38]:


for i in final_cat:
    get_pivot_plots(df, num = 'total_pymnt', cat = i)


# In[26]:


for i in final_cat:
    print(i.upper())
    print('--'*50)
    print(pd.pivot_table(df, values = final_num, columns = 'loan_status', index = i,
            aggfunc = np.median))
    print('\n\n')


# In[39]:


final_report = pd.pivot_table(df, values = final_num, columns = 'loan_status', index = final_cat,
            aggfunc = np.median)


# In[40]:


#final_report.to_csv('final_report.csv', sep = ',', index = True )


# #### Analysis:
# 
#     Loan amount, interest rate, Dti, revol_bal and revol_util are generally more in each category for charged
#     off than those who have fully paid the loans. Whereas, annual income and total payment are high for those
#     who have fully paid the loans.
#     
#     Interest rates are always higher for those who have defaulted.
#     
#     
#     Term:
#         loans of 60 months have high median for income, int_rate, total_pymnt, revol_bal, revol_util,
#         dti. Also those that have been charged off have low income and payment but high int_rate, dti,
#         revol_bal and revol_util.
#         
#     Grade:
#         Grade G loans are highest medians in all numeric. Also charged off loans have comparatively higher 
#         int_rate, dti, revol_bal and revol_util, with low income and payment.
#         
#     Purpose:
#         
#          Loans for small business, debt_consolidation, home_improvement have highest amounts. They have higher
#          income, and interest rates are highest for credit cards. Also charged off loans have low annual income
#          but high int_rate, dti, revol_bal and revol_util.
#          
#          
#     Emp_length:
#         Older employees have higher loans, higher income, higher payments as well as higher dti.
#         But int_rate across employment years are same. Also charged off loans have lower income but higher 
#         int_rate, dti, revol_bal and revol_util.
#         
#     Home_ownership:
#         Those that have mortagage have high income, loan amount and revol_bal, but int_rates are 
#         similar across home_ownership. Also charged off have higher int_rates, dti, revol_bal
#         and revol_util but low income.
#         
#     Verification status:
#         Verified loans are higher in amount, int_rates, income and all other numerics.
#         Also charged off loans have comparatively higher 
#         int_rate, dti, revol_bal and revol_util, with low income and payment.
#     

# In[ ]:




