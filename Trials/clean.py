#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:21:27 2022

@author: edgartome83
"""

import pandas as pd
import numpy as np
import datetime

pj = pd.read_excel(r'/Users/edgartome_1/IronHack/IronProjects/Project6/Payments.xlsx')

pjdate = pj['Date'].unique()
list(pjdate)
dicdates = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}

pj['Date']
for y in list(pjdate):
    if type(y) == str:
        val = [x.lower() for x in y]
        for x in val:
            day = val[:2]
            day1 = val[0] + val[1]
            year = val[-2:]
            year1 = year[0] + year[1]
            month = val[3:6]
            month1 = month[0] + month[1] + month[2]
            correctdate = datetime.datetime(2000 + int(year1), dicdates[month1] , int(day1), 0, 0)
            print(correctdate)
            pj['Date'] = np.where(pj['Date'] == y,correctdate,0)
            break
pj['Date'].unique()


#Check columns
pj.columns

#Check types
pj.dtypes

#Convert the float in to interger
pj['Initial Amount'] = pj['Initial Amount'].astype('int64')

#Check if converted
pj.dtypes

#Remove dot from Creditor column
pj['Creditor'].str.replace(r'[^0-9a-zA-Z:,]+', '', regex=True)

#Create new column code
pj['Rf_Am'] = pj['Reference']+str(pj['Initial Amount'])

pj['Date']

for x in range(len(pj['Bank'])):
    pj['Country'][x] = pj['Bank'][x][4:6]
