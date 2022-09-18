import email
from traceback import print_tb
import pandas as pd

df=pd.read_csv('F:\MyData\survey_results_public.csv')
rows=df.shape
print(rows)
data_info=df.info()
print(data_info)
data_option=pd.set_option('display.max_columns',79)
data_option=pd.set_option('display.max_rows',79)
print(df)

schema_df=pd.read_csv('F:\MyData\survey_results_schema.csv')
# print(schema_df)
schema_option=pd.set_option('display.max_rows',79)
print(schema_df)
certain_rows=df.head(15)
print(certain_rows)
last_rows=df.tail(10)
print(last_rows)

person={
    "name":["sanjay kumar",'Sam bansal','sashi kumar'],
    'last':['sahoo','kumar','tharoor'],
    'email':['sanjaya.sahoo@gmail.com','samb@gmail.com','sashitharoor@gmail.com']
}

df=pd.DataFrame(person)
print(df[['name','last','email']])

print(df.columns)
print(df.iloc[[1,2]])
print(df.iloc[[1,2],[0,2]])
print(df.loc[[0,2],['email','name']])

df=pd.read_csv('F:\MyData\survey_results_public.csv')
print(df.columns)
print(df['Age'].value_counts())
print(df.loc[[0,1,2],'Employment'])
index_data=df.set_index('email')
index_default=df.set_index('email',inplace=True)
print(df)
print(df.index)

reset_place=df.reset_index(inplace=True)
print(df)

df=pd.read_csv('F:\MyData\survey_results_public.csv')
df=pd.read_csv('F:\MyData\survey_results_public.csv',index_col='Age')

schema_df=pd.read_csv('F:\MyData\survey_results_schema.csv')
pd.set_option('display.max_columns',79)
some_data=df.head(10)
print(some_data)
set_index_data=df.set_index(['Age'],inplace=True)
sort_data_index=df.sort_index()
print(sort_data_index)
age_index=df.head()
print(age_index)














































