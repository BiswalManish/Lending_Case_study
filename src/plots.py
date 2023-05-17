from functions import *
import seaborn as sns
import matplotlib.pyplot as plt

path = '/Users/manish/Documents/Projects/data_science/Lending_club_case_study/data/clean_data/loan_for_analysis.csv'

df = pd.read_csv(path)

cat_cols = list(df.columns[df.dtypes == 'object'])
num_cols = list(df.columns[df.dtypes != 'object'])

#final_list
final_cat = ['term', 'grade', 'purpose', 'emp_length', 
             'home_ownership', 'verification_status']
final_num = ['loan_amnt', 'int_rate', 'annual_inc',
             'installment', 'revol_bal', 'revol_util',
             'dti', 'total_pymnt']

#countplots for categorical data
def plot_categorical(df, hue = None):

    
    for i in cat_cols:
        if i != 'purpose':
            sns.catplot(data = df,
                   x =  i, 
                   kind = 'count', palette = sns.color_palette('Pastel1', n_colors = 3),
                   height = 5, hue = hue,
                   aspect = 1.5, order = df[i].value_counts().index,
                   )
        else:
            sns.catplot(data = df,
                   y =  i, 
                   kind = 'count', palette = sns.color_palette('Pastel1', n_colors = 3),
                   height = 5, hue = hue,
                   aspect = 1.5, order = df[i].value_counts().index,
                   )
        if input('Save image?\n(y/n):\n').lower() == 'y':
            plt.savefig(f'{i}.png', dpi = 500)

        else:
            plt.show()


#violin and density plots for numerical data
def plot_numerical(df, y = None):
    
    for i in num_cols:
    
        
        plt.figure(figsize = (8,10))
        plt.subplot(2,1, 1)
        sns.violinplot(data = df,
             x = i,
             y = y,
             palette = sns.color_palette('Pastel1', n_colors = 3)
             )
        
        plt.subplot(2,1,2)
        sns.distplot(
            x = df[i],
            color = 'teal',
            bins = 10
            )
        plt.xlabel(i)

        if input('Save image?\n(y/n):\n').lower() == 'y':
            plt.savefig(f'{i}.png', dpi = 500)
        
        else:
            plt.show()


#plot combination of inputs
def plot_combo(data = None, x = None, row = None, y = None, palette = None, col = None):
    
    sns.catplot(data = df,
               y = y,
               x = x,
               col = col, row = 'loan_status',
               kind = 'violin',
               palette = palette,
               height = 5, aspect = 1.5,
               order = df[y].value_counts().index
               )
    
    if input('Save image?\n(y/n):\n').lower() == 'y':
        plt.savefig(f'Loan status vs {x} for various {y}.', dpi = 1000)
   
    else:
        plt.show()


#plotting pivots
def get_pivot_plots(data, num = None, cat = None, palette = None):   
    
    print(f'{cat}'.upper())
    
    
    print('---'*20)
    
    print(pd.pivot_table(data = data, 
              values = num,
              index = cat, columns = 'loan_status',
              
              aggfunc = np.median))
    
    print('---'*20)
    
    print('\n'*2)
    
    plot_combo(data, x = num, y = cat, palette = palette)


#drawing pivot tables
def draw_pivot(data, num):
    for i in final_cat:
        print(i.upper())
        print('--'*50)
        print(pd.pivot_table(data, columns = i, index = 'loan_status',
               values = num,
               aggfunc = 'median'))
        print('\n'*3)
    
