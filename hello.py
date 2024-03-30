import pandas as pd

#read in 2 csv files
df = pd.read_csv('testexcel.csv')
df2 = pd.read_csv('testexcel2.csv')

#prints out excel.csv dataframe
print(df)












#set all nationality count to 0
burmese = 0
vietnam = 0
indonesian = 0
sri_lanka = 0
bangladeshi = 0
thai = 0
chinese = 0
myanmar = 0
filipino = 0
malaysian = 0
indian = 0

company_name = df2.iloc[1,0]
print("first company: " + company_name)

#loop through the dataframe
for x, y in zip(df2['Company'], df2['Nationality']):
  #if the company name changes
  if x != company_name:
    print("New company: " + x)
    #reset the nationality count  
    indian = 0
    bangladeshi = 0
    #set the new company name
    company_name = x

  #assign company name to mask
  mask = df['Company'] == company_name
    

  if x == company_name and y == 'BURMESE':
    burmese = burmese + 1
    df.loc[mask, 'BURMESE'] = df.loc[mask, 'BURMESE'] - 1
  if x == company_name and y == 'VIETNAM':
    vietnam = vietnam + 1
    df.loc[mask, 'VIETNAM'] = df.loc[mask,'VIETNAM'] - 1
  if x == company_name and y == 'INDONESIAN':
    indonesian = indonesian + 1
    df.loc[mask, 'INDONESIAN'] = df.loc[mask, 'INDONESIAN'] - 1
  if x == company_name and y == 'SRI LANKA':
    sri_lanka = sri_lanka + 1
    df.loc[mask, 'SRI LANKA'] = df.loc[mask, 'SRI LANKA'] - 1
  if x == company_name and y == 'BANGLADESHI':
    bangladeshi = bangladeshi + 1
    df.loc[mask, 'BANGLADESHI'] = df.loc[mask, 'BANGLADESHI'] - 1
  if x == company_name and y == 'THAI':
    thai = thai + 1
    df.loc[mask, 'THAI'] = df.loc[mask, 'THAI'] - 1
  if x == company_name and y == 'CHINESE':
    chinese = chinese + 1
    df.loc[mask, 'CHINESE'] = df.loc[mask, 'CHINESE'] - 1
  if x == company_name and y == 'MYANMAR':
    myanmar = myanmar + 1
    df.loc[mask, 'MYANMAR'] = df.loc[mask, 'MYANMAR'] - 1
  if x == company_name and y == 'FILIPINO':
    filipino = filipino + 1
    df.loc[mask, 'FILIPINO'] = df.loc[mask, 'FILIPINO'] - 1
  if x == company_name and y == 'MALAYSIAN':
    malaysian = malaysian + 1
    df.loc[mask, 'MALAYSIAN'] = df.loc[mask, 'MALAYSIAN'] - 1
  if x == company_name and y == 'INDIAN':
    indian = indian + 1  
    df.loc[mask, 'INDIAN'] = df.loc[mask, 'INDIAN'] - 1

  
  

  #check if the nationality count is correct
  print("Bangladeshi: " + str(bangladeshi))
  print("Indian: " + str(indian))    

#manipulate data in df
#mask = df['Company'] == company_name
#df.loc[mask, 'BURMESE'] = df.loc[mask, 'BURMESE'] - burmese
#df.loc[mask, 'VIETNAM'] = df.loc[mask,'VIETNAM'] - vietnam
#df.loc[mask, 'INDONESIAN'] = df.loc[mask, 'INDONESIAN'] - indonesian
#df.loc[mask, 'SRI LANKA'] = df.loc[mask, 'SRI LANKA'] - sri_lanka
#df.loc[mask, 'BANGLADESHI'] = df.loc[mask, 'BANGLADESHI'] - bangladeshi
#df.loc[mask, 'THAI'] = df.loc[mask, 'THAI'] - thai
#df.loc[mask, 'CHINESE'] = df.loc[mask, 'CHINESE'] - chinese
#df.loc[mask, 'MYANMAR'] = df.loc[mask, 'MYANMAR'] - myanmar
#df.loc[mask, 'FILIPINO'] = df.loc[mask, 'FILIPINO'] - filipino
#df.loc[mask, 'MALAYSIAN'] = df.loc[mask, 'MALAYSIAN'] - malaysian
#df.loc[mask, 'INDIAN'] = df.loc[mask, 'INDIAN'] - indian

#print out new dataframe
print(df.iloc[0:3, 0:12])