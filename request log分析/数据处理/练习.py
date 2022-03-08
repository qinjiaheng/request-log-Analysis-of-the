from datetime import datetime

import pandas as pd

lst_log = []
log_dir = r'F:\project\Python\journal\j.txt'
with open(log_dir, encoding='utf-8') as log_etl:
    for i in log_etl:
        if ' - - ' in i:
            lst_log.append(i.strip())

df = pd.DataFrame({'message': lst_log})

df_1 = df['message'].str.split(' - - ', expand=True)
# df_2 = df_1['message'].str.split('] "',expand=True)
df_1.columns = ['url', 'time', 'i']
df_3 = df_1.join(df)

df_6 = df_3.drop(['i', 'message'], axis=1)
df_4 = df_6['time'].str.split('] "', expand=True)
df_4.columns = ['times', 'website']
df_5 = df_4.join(df_6)

df_7 = df_5.drop('time', axis=1)
df_8 = df_7['times'].str.split('[', expand=True)
df_8.columns = ['1', 'time_s']
df_9 = df_8.join(df_7)

df_website = df_9.drop('1', axis=1)

df_time = df_website['time_s'].str.split(':', expand=True)
df_time.columns = ['times', 'q', 'w', 'e']
df_time_1 = df_time.join(df_website)
df_time_3 = df_time_1.drop(['q', 'w', 'e', 'time_s'], axis=1)

df_time_3['time_s'] = time_s
df_time_4 = df_time_3.drop('times', axis=1)
data = df_time_4['website'].str.split('"-"', expand=True)
data.columns = ['q', 'w', 'e']
data_1 = data.join(df_time_4)

data_2 = data_1['q'].str.split(' ', expand=True)[3].reset_index(name = 'status_code')
data_3 = data_2.drop('index',axis=1)

data_1['status_code'] = data_3

data_s = data_1.drop(['q','w','e'],axis=1)

data_sd = data_s.replace({'"':''}, regex=True)
data_sd.to_csv('df_web.csv',index=0)
