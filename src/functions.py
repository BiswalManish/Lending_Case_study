
import numpy as np
import pandas as pd


#1. function to get null counts
def get_Null_counts(df):
    """
    get_Null_counts:
    ----------------------------
        
        This function takes 1 argument as pandas dataframe 

    args
    ----------------------------
        
        df : pandas datframe like object
        

    Returns
     -----------------------------

        Returns a pandas series like object with column name and its percent null values
    """
    
    Null_counts = round(100 * df.isnull().sum()/df.isnull().count(), 2)
    
    return Null_counts



#2. checking unique and null values
def get_null_unique(df, columns):
    """
    get_null_colums:
    ----------------------------
        
        This function takes 2 arguments as pandas dataframe and list of columns and

    args
    ----------------------------
        
        df : pandas datframe like object
        columns : list of column in the dataframe

    Returns
     -----------------------------

        prints the unique values in each column and the percent of null in each column
    """

    for i in range(len(columns)):
        #prints column name and 1st 10 unique characters
        print(columns[i], ': ',df[columns[i]].unique()[:10])


        #prints #unique char.
        print('Unique: ', len(df[columns[i]].unique()))

        #prints per_cent of null entries
        print('Null per_cent: ', get_Null_counts(df)[columns[i]])
        print('---'*20)


#3. Remove trailing %
def remove_trailing(df, col = None):
    
    return df[col].applymap(lambda x: float(x.rstrip('%')))


#4. Creating bins
def to_bins(df, col = None):
    
    resolve = []
    
    k = max(df[col])/3
    
    
    for x in df[col]:
        
        if x < k:
            
            z =  'new'
        
        elif x >= k and x <= 2 * k :
            
            z =  'mid'
    
        else:
            z =  'old'
        
        resolve.append(z)
        
    return resolve