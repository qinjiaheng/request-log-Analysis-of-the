import pandas as pd
from sqlalchemy import create_engine
from pyecharts.charts import Line, Map, Pie, Bar
from pyecharts import options as opts

engine = create_engine('mssql+pymssql://sa:123456@127.0.0.1/web')
sql = """select time_s,website from website_log"""

df = pd.read_sql(sql, con=engine)


def df_website():
    """
    1，提取数据并处理
    2，可视化处理
    """
    df_web = df[df['website'].str.contains('Baiduspider')]
    df_day = df_web.groupby(df_web['time_s']).size()
    # print(df_day.index.tolist())

    # 图
    c = (
        Line()
            .add_xaxis(df_day.index.tolist())
            .add_yaxis('来访次数', df_day.values.tolist())
            .set_global_opts(title_opts=opts.TitleOpts(title="百度蜘蛛"),
                             datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")]
                             )
            .render("百度蜘蛛来访次数统计.html")
    )


df_website()
