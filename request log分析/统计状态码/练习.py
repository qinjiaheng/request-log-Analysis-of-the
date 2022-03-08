import pandas as pd
from sqlalchemy import create_engine
from pyecharts.charts import Line, Map, Pie, Bar
from pyecharts import options as opts

engine = create_engine('mssql+pymssql://sa:123456@127.0.0.1/web')
sql = """select status_code from website_log"""

df = pd.read_sql(sql, con=engine)

df_code = df.value_counts()
# print(df_code.values.tolist())
attr = []
for i in df_code.index.tolist():
    for j in i:
        attr.append(j)

pie = (
    Pie()
        .add("统计", [list(z) for z in zip(attr, df_code.values.tolist())])
        .set_global_opts(title_opts=opts.TitleOpts(title="状态码"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
)

pie.render('统计状态码.html')
