import pandas as pd #importing pandas
import warnings
warnings.filterwarnings('ignore')
data = pd.read_csv('transaction.csv' , sep= ';') #reading csv file
data.info()

#Defining Variables
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased*ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased*CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased*CostPerItem
CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
#adding new column to a dataframe
data['CostPerTransaction'] = CostPerTransaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']
#Profit, markup calculation
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']
data['Markup'] = data['ProfitPerTransaction']/data['CostPerTransaction']


#rounding markup 
roundmarkup = round(data['Markup'],2)
data['Markup'] = round(data['Markup'],2)

print(data['Day'].dtype)
Day = data['Day'].astype(str)
Year = data['Year'].astype(str)
print(Day.dtype)
my_date = Day + '-' + data['Month'] + '-' + Year
data['Date'] = my_date


data.iloc[0] #First row
data.iloc[0:3] #first 3 rows
data.iloc[-7:] #last 7 rows
data.head(0) #all the columns
data.iloc[:,0] #first column
data.iloc[1,1] #row 1 col 1 element

#Split Column
split_col = data['ClientKeywords'].str.split(',' , expand = True)


#creating new columns for split_col
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['ClientContract'] = split_col[2]


#Replace item
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['ClientContract'] = data['ClientContract'].str.replace(']', '')


#Lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#df = df.drop('Columnname' , axis=1)
data = data.drop('ClientKeywords',axis = 1)
data = data.drop(['Day','Year','Month'],axis = 1)
df = pd.read_csv("transaction.csv", delimiter=';')
df2 = pd.read_csv("value_inc_seasons.csv", delimiter=';')
df_new = df.merge(df2, left_on='Month', right_on='Month')

data.to_csv('ValueInc_Cleaned.csv', index = False)
#print(df_new)
df_new.to_csv('ValueInc_Clean.csv', index = False)











