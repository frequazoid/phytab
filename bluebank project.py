# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 09:56:55 2023

@author: welcome
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

json_file=open('loan_data_json.json')
data=json.load(json_file)

loandata=pd.DataFrame(data)

loandata['purpose'].unique()

loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

income=np.exp(loandata['log.annual.inc'])
loandata['annualincome']=income


length=len(loandata)
ficocat=[]
for x in range (0,length):
    category=loandata['fico'][x]
    if category>=300 and category<400:
        cat='Very Poor'
    elif category>=400 and category<600:
        cat='Poor'
    elif category>=601 and category<660:
         cat='Fair'
    elif category>=660 and category<700:
         cat='Good'
    elif category>=700:
         cat='Excellent'
    else:
        cat='Unknown'
    ficocat.append(cat)
    
ficocat=pd.Series(ficocat)
loandata['fico.category']=ficocat

loandata.loc[loandata['int.rate']>0.12,'int.rate.type']='High'
loandata.loc[loandata['int.rate']<=0.12,'int.rate.type']='Low'

catplot=loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='green',width=0.1)
plt.show()

purposecount=loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='blue',width=0.1)
plt.show()

loandata.to_csv('loan_cleaned.csv', index=True)


















