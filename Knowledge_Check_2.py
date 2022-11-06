#Import pandas libary 
import pandas as pd 

#Reading csv movie dataset https://www.kaggle.com/datasets/bharatnatrayn/movies-dataset-for-feature-extracion-prediction?select=movies.csv into pandas dataframe 
df = pd.read_csv('movies.csv')

#Print dataframe before cleaning
print('Raw data before cleaning')
print(df)
print("Record count per column:", df.count())


#Print dataframe after cleaning 
# Gross column is empty. Column will be dropped 
print('Data after cleaning')

def clean_col():
    #Remove gross column
    df.pop('Gross')
    #Remove rows with nan or empty
    new_df = df.dropna()

    print(new_df)
    print("Record count per column:", new_df.count())
    
clean_col()






#print(df.count(axis='columns'))

#print(pd.options.display.max_rows) 
#print(df.to_string())


