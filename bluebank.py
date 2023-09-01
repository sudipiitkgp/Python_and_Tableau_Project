import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)
#method2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)

#transform to dataframe
loandata = pd.DataFrame(data)

#finding unique values for purpose column
loandata['purpose'].unique()

#describe data
loandata.describe()
#describe column
loandata.columns
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using EXP() to get annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income
print(income)


#FICO score
# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# fico >=780: 'Excellent'
length = len(loandata)
ficocat = []
for i in range(0,length):
    category = loandata['fico'][i]
    
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 780:
            cat = 'Good' 
        elif category >=780:
            cat = 'Excellent'
    except:
            cat = 'Unknown'
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

#df.loc as conditional statements
#df.loc[df[columnname] condition, newcolumname] = 'value if the condition is met'
#for interest rates, a new column is required. rate >0.12 is high else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

# number of loans/rows by fico.category
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.5)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'red', width = 0.5)
plt.show()

#scatter plots
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = '#4cad50')
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv', index = True)






























































