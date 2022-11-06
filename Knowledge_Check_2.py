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

#Funtion for cleaning
def clean_df():
    #Remove gross column
    df.pop('Gross')
    #Remove rows with nan or empty
    #df.dropna(inplace = True)
    # remove duplicates; the inplace =True makes the changes to the orginal dataframe vs a creating a new one
    df.drop_duplicates(inplace = True) 
    
    #Display dataframe 
    print(df)
    print("Record count per column:", df.count())

#Calling function     
clean_df()




#print(df.count(axis='columns'))

#print(pd.options.display.max_rows) 
#print(df.to_string())


