# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 07:01:45 2023

@author: welcome
"""

#file_name=pd.read_csv(file.csv')

import pandas as pd
data=pd.read_csv('transaction.csv')
data=pd.read_csv('transaction.csv',sep=';')

CostPerItem=11.73
SellingPricePerItem=21.11
NumberOfItemsPurchased=6

ProfitPerItem=21.11-11.73
ProfitPerTransaction=NumberOfItemsPurchased*ProfitPerItem
CostPerTransaction=NumberOfItemsPurchased*CostPerItem
SalesPerTransaction=NumberOfItemsPurchased*SellingPricePerItem
ProfitPerItem=SellingPricePerItem-CostPerItem

CostPerItem=data['CostPerItem']
NumberOfItemsPurchased=data['NumberOfItemsPurchased']
CostPerTransaction=NumberOfItemsPurchased*CostPerItem

#adding a new column to a dataframe
data['CostPerTransaction']=CostPerTransaction
data['SalesPerTransaction']=data['NumberOfItemsPurchased']*data['SellingPricePerItem']

#profit Calculation = sales-cost
data['ProfitPerTransaction']=data['SalesPerTransaction']-data['CostPerTransaction']

#markup= (sales-cost)/cost
data['Markup']=data['ProfitPerTransaction']/data['CostPerTransaction']

#how to rounding up decimals
data['Markup']=round(data['Markup'],2)

day=data['Day'].astype(str)
year=data['Year'].astype(str)
print(day.dtype)
print(year.dtype)
my_date=day+'-'+data['Month']+'-'+year
data['date']=my_date

data.iloc[0]

split_col=data['ClientKeywords'].str.split(',' ,expand=True)
data['ClientAge']=split_col[0]
data['ClientType']=split_col[1]
data['LenghtofContract']=split_col[2]

data['ClientAge']=data['ClientAge'].str.replace('[','')
data['LenghtofContract']=data['LenghtofContract'].str.replace(']','')

data['ItemDescription']=data['ItemDescription'].str.lower()

seasons=pd.read_csv('value_inc_seasons.csv',sep=';')
data=pd.merge(data,seasons,on='Month')

data=data.drop('ClientKeywords',axis=1)
data=data.drop('Day',axis=1)
data=data.drop(['Year','Month'],axis=1)

data.to_csv('ValueInc_Cleaned.csv',index=False)















