import pandas as pd
import pymssql

file = 'F:\project\Python\journal\df_web.csv'

df = pd.read_csv(file, encoding='gbk')
# print(df.info())

# 连接数据库
conn = pymssql.connect('127.0.0.1', 'sa', '123456', 'web', charset='utf8')
cursor = conn.cursor()

# 导入数据
for index, row in df.iterrows():
    sql = """insert into website_log(
        id,
        website,
        url,
        time_s,
        status_code
        )
        values (%d,'%s','%s','%s',%s)

    """ % (
        index + 1,
        row['website'],
        row['url'],
        row['time_s'],
        row['status_code']
    )
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        pass

# 关闭数据库连接
conn.close()
