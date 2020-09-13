# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 22:03:54 2020

@author: jider
"""

import pandas as pd

df= pd.read_csv('vehicles.csv')

df.columns

df2= df.head(100)

df2.rename(index= str, columns= {'region':'new_region'},inplace = True)


#Single Column
df['region']

#Selecting Rows
df[0:100]

#Select multiple columns

url_region_price = df[['url','region','price']]

url_region_price2 = df.loc[:,['url','region','price']]

url_region_price2 = df.loc[0:100,['url','region','price']] 

url_region_price2 = df.iloc[0:100,0:3] 


#Drop Columns

df_no_url= df.drop('url', axis= 1)

#Adding Columns

df['age']= 2019 - df['year']
df['current year']= 2019

#Filtering the data frame

new_car= df[df.age<=10]
new_car_price= df[(df.age<=10) | (df.price> 5000)]

#Using Location(Loc) for same
df.loc[df.age<=10,:]

#Additional Feature creation

df['price per mile']=df['price']/df['odometer']

#Supply Function: f(x)= x*2; Price doubled

def price2x(x):
    return x*2

df['price2']= df['price'].apply(price2x)

df.price.head()

df.price2.head()

#Lambda Function

df['price3']= df.price.apply(lambda x: x*3)
df.price3.head()


#To categorize from price > 10000 is Expensive

df['isexpensive']= df. price.apply (lambda x: 'Expensive' if x>10000 else 'cheap')

df.isexpensive.head(100).value_counts()

# Creating feature based on information in other fields

df['new_and_cheap']= df.apply(lambda x: "yes" if x['price'] < 10000 and x['age']<10 else "no", axis =1)

df.new_and_cheap.head(100)

#Quantiles- Grouping prices into quantiles- use-case quantiles

df['price_quantiles']= pd.qcut(df.price,5)

df.price_quantiles.value_counts()


# To ensure that the data points are grouped in same-size bins

df['price_quantiles']= pd.cut(df.price, 5)

df.price_quantiles.value_counts()


#Identifying Categorical variables to prepare data for algorithm/modelling

dummy_variables= pd.get_dummies(df[['price', 'year','fuel','transmission','type']])

dummy_variables= pd.get_dummies(df[['price', 'year','fuel','transmission','type']].head(1000))

#Certain information in defined columns and row.e.g. price of car based on years and type of car
pd.pivot_table(df, index = 'year', columns ='type', values= 'price', aggfunc ='mean')

#When sorted based on column values, instead of index....

pd.pivot_table(df, index = 'year', columns ='type', values= 'price', aggfunc ='mean').sort_index(ascending= False)

pd.pivot_table(df, index = 'year', columns ='type', values= 'price', aggfunc ='count').sort_index(ascending= False)

# When graphed...

pd.pivot_table(df, index = 'year', columns ='type', values= 'price', aggfunc ='count').sort_index(ascending= False).plot()

#Using SQL 'Group By" 

Grouped_data= df.groupby('type').mean()

# As we did not want to index by the type, we :

Grouped_data= df.groupby(['type','year'], as_index= False).mean()

#Merging Multiple Dataframes Using Panda Merge

df1= df[['url','region']]
df2 =df[['url', 'price']]

df_inner_joined= pd.merge(df1,df2,on= 'url')


#Appending

Samp11 = df.sample(100, random_state =1)
Samp12 = df.sample(100, random_state =2)

Samp11.append(Samp12)

#Writing to CSV

df.head(1000).to_csv('TopAfeez1000.csv')






