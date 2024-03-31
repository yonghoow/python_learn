import pandas as pd

#read in 2 csv files
df = pd.read_csv('testexcel.csv')
df2 = pd.read_csv('testexcel2.csv')

#prints out excel.csv dataframe
print(df)


company_name = df2.iloc[1,0]
print("first company: " + company_name)

#loop through the dataframe
for x, y in zip(df2['Company'], df2['Nationality']):
  #if the company name changes
  if x != company_name:
    print("New company: " + x)
    
    #set the new company name
    company_name = x

  #assign company name to mask
  mask = df['Company'] == company_name
    

  if x == company_name and y == 'BURMESE':
    #minus 1 from BURMESE
    df.loc[mask, 'BURMESE'] = df.loc[mask, 'BURMESE'] - 1
  if x == company_name and y == 'VIETNAM':
    #minus 1 from VIETNAM
    df.loc[mask, 'VIETNAM'] = df.loc[mask,'VIETNAM'] - 1
  if x == company_name and y == 'INDONESIAN':
    #minus 1 from INDONESIAN
    df.loc[mask, 'INDONESIAN'] = df.loc[mask, 'INDONESIAN'] - 1
  if x == company_name and y == 'SRI LANKA':
    #minus 1 from SRI LANKA
    df.loc[mask, 'SRI LANKA'] = df.loc[mask, 'SRI LANKA'] - 1
  if x == company_name and y == 'BANGLADESHI':
    #minus 1 from BANGLADESHI
    df.loc[mask, 'BANGLADESHI'] = df.loc[mask, 'BANGLADESHI'] - 1
  if x == company_name and y == 'THAI':
    #minus 1 from THAI
    df.loc[mask, 'THAI'] = df.loc[mask, 'THAI'] - 1
  if x == company_name and y == 'CHINESE':
    #minus 1 from CHINESE
    df.loc[mask, 'CHINESE'] = df.loc[mask, 'CHINESE'] - 1
  if x == company_name and y == 'MYANMAR':
    #minus 1 from MYANMAR
    df.loc[mask, 'MYANMAR'] = df.loc[mask, 'MYANMAR'] - 1
  if x == company_name and y == 'FILIPINO':
    #minus 1 from FILIPINO
    df.loc[mask, 'FILIPINO'] = df.loc[mask, 'FILIPINO'] - 1
  if x == company_name and y == 'MALAYSIAN':
    #minus 1 from MALAYSIAN
    df.loc[mask, 'MALAYSIAN'] = df.loc[mask, 'MALAYSIAN'] - 1
  if x == company_name and y == 'INDIAN':  
    #minus 1 from INDIAN
    df.loc[mask, 'INDIAN'] = df.loc[mask, 'INDIAN'] - 1


#print out new dataframe
print(df.iloc[0:3, 0:12])


#write to excel file
df.to_excel("output.xlsx", index=False)
