import pandas as pd

df = pd.DataFrame({'Name': ['Real Madrid']})
df.to_excel('./rm.xlsx', sheet_name='BestClub', index=False)
df = pd.read_excel('rm.xlsx', 'BestClub')
df.to_csv('rm.csv')