import pandas as pd
import plotly.graph_objs as go
import streamlit as st
from pyecharts.charts import Pie, Line, Bar
from pyecharts import options as opts
import streamlit.components.v1 as components
from pyecharts.components import Table
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.options import ComponentTitleOpts
st.set_page_config(
    page_title="智汇中医",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={

    }
)
tab1, tab2, tab3, tab4, tab5 = st.tabs(["题型分布", "班级均分", "分数分布", "变化率", "成绩详情"])

with tab1:
    label = ['选择题分值占比', '填空题分值占比', '简答题分值占比', '画图题分值占比','综合题分值占比']
    values = [30, 10, 20, 15,25]
    def pie_base():
        c = (
            Pie()
            .add("", [list(z) for z in zip(label, values)])
            .set_global_opts(title_opts=opts.TitleOpts(title="题型分布占比"),

                             )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c} {d}%"))
                             )# 值得一提的是，{d}%为百分比

        return c
    components.html(pie_base().render_embed(), height=600, width=1000)
with tab2:

    x = ['中医1班', '中医2班', '中医3班', '中医4班', '中西医1班', '中西医2班', '中西医3班']
    y1 = [80, 77, 85, 75, 76, 81, 83]
    y2 = [81, 75, 83, 76, 74, 90, 85]
    y3 = [86, 74, 82, 73, 76, 92, 80]
    y4 = [85, 78, 84, 77, 73, 93, 87]
    y5 = [89, 79, 88, 78, 72, 95, 81]
    y6 = [83, 76, 81, 71, 77, 96, 88]
    y7 = [82, 72, 87, 74, 79, 98, 82]
    line = (
        Line()
        .add_xaxis(xaxis_data=x)
        .add_yaxis("作业1", y1, color='blue',
                   markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
                   )
        .add_yaxis("作业2", y_axis=y2,
                   markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),)
        .add_yaxis("作业3", y_axis=y3,
                   markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]), )
        .add_yaxis("期中", y_axis=y4,
                   markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]), )
        .add_yaxis("作业4", y_axis=y5,
                   markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]), )
        .add_yaxis("作业5", y_axis=y6,
                   markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]), )
        .add_yaxis("期末", y_axis=y7,
                   markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),)
        .set_global_opts(title_opts=opts.TitleOpts(title="班级平均分"),
                         brush_opts=opts.BrushOpts(),  # 设置操作图表的画笔功能
                         toolbox_opts=opts.ToolboxOpts(),  # 设置操作图表的工具箱功能
                         yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter=""), name="分数"),
                         # 设置Y轴名称、定制化刻度单位
                         xaxis_opts=opts.AxisOpts(name="班级"),  # 设置X轴名称
                         )

    )
    components.html(line.render_embed(), height=600, width=1000)
with ((tab3)):
    # 柱状图
    # st.subheader("分数分布", divider='red')
    # df3 = pd.DataFrame([2, 23, 16, 25, 20, 12], index=['缺考', '不合格', '60-70', '70-80', '80-90', '90-100'])
    # # st.bar_chart(df3, use_container_width=True, color='#8BE09C')
    bar = Bar()
    bar.add_xaxis(['90-100分','80-90分','70-80分','60-70分','40-60','0-40分'])
    bar.add_yaxis('中医1班', [15, 21, 18, 14, 9, 2],itemstyle_opts=opts.ItemStyleOpts(color="#00CD96"))
    bar.add_yaxis('中医2班', [19, 18, 15, 24, 7, 0], )
    bar.add_yaxis('中医3班', [25, 19, 14, 9, 3, 0], )
    bar.add_yaxis('中医4班', [17, 24, 16, 17, 10, 1],)
    bar.set_series_opts(markline_opts=opts.MarkLineOpts(
        data=[opts.MarkLineItem(type_='max', name='最大值')]
    ))
    bar.set_global_opts(
        title_opts={"text": "分数分布情况"},
        brush_opts=opts.BrushOpts(),  # 设置操作图表的画笔功能
        toolbox_opts=opts.ToolboxOpts(),  # 设置操作图表的工具箱功能
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter=""), name="人数"),
        # 设置Y轴名称、定制化刻度单位
        xaxis_opts=opts.AxisOpts(name="分数段"),  # 设置X轴名称

    )
    barHtml = bar.render_embed()  # 将折线组件转换成html文本
    components.html(barHtml, height=600, width=1000)

with tab4:
    # 数据变化率
    st.subheader("班级变化率", divider='red')
    col0,col1, col2, col3,col4= st.columns(5)
    col0.metric("中医1班","作业一","2024.1.18",)
    col1.metric("平均分", "85", "0")
    col2.metric("优秀率(>80)", "78%", "0%")
    col3.metric("及格率(>=60)", "87%", "0%")
    col4.metric("不及格率(<60)", "13%", "0%")

    col0.metric("中医1班","作业二","2024.1.25")
    col1.metric("平均分", "88", "3")
    col2.metric("优秀率(>80)", "81%", "3%")
    col3.metric("及格率(>=60)", "93%", "6%")
    col4.metric("不及格率(<60)", "7%", "-6%")

    col0.metric("中医1班", "作业三","2024.2.2")
    col1.metric("平均分", "81", "-7")
    col2.metric("优秀率(>80)", "75%", "-6%")
    col3.metric("及格率(>=60)", "82%", "-11%")
    col4.metric("不及格率(<60)", "18%", "11%")

    col0.metric("中医1班", "期中测试","2024.2.15")
    col1.metric("平均分", "84", "3")
    col2.metric("优秀率(>80)", "58%", "0%")
    col3.metric("及格率(>=60)", "88%", "0%")
    col4.metric("不及格率(<60)", "12%", "0%")

    col0.metric("中医1班", "期末测试", "2024.2.27")
    col1.metric("平均分", "80", "-4")
    col2.metric("优秀率(>80)", "60%", "2%")
    col3.metric("及格率(>=60)", "79%", "-9%")
    col4.metric("不及格率(<60)", "21%", "9%")

    col0.metric("中医2班", "作业一","2024.1.18")
    col1.metric("平均分", "84", "0")
    col2.metric("优秀率(>80)", "75%", "0%")
    col3.metric("及格率(>=60)", "93%", "0%")
    col4.metric("不及格率(<60)", "7%", "0%")

    col0.metric("中医2班", "作业二","2024.1.25")
    col1.metric("平均分", "80", "-4")
    col2.metric("优秀率(>80)", "81%", "6%")
    col3.metric("及格率(>=60)", "92%", "-1%")
    col4.metric("不及格率(<60)", "8%", "1%")

    col0.metric("中医2班", "作业三","2024.2.2")
    col1.metric("平均分", "81", "1")
    col2.metric("优秀率(>80)", "77%", "-4%")
    col3.metric("及格率(>=60)", "86%", "-6%")
    col4.metric("不及格率(<60)", "14%", "-6%")

    col0.metric("中医2班", "期中测试","2024.2.15")
    col1.metric("平均分", "75", "0")
    col2.metric("优秀率(>80)", "57%", "0%")
    col3.metric("及格率(>=60)", "78%", "0%")
    col4.metric("不及格率(<60)", "22%", "0%")

    col0.metric("中医2班", "期末测试", "2024.2.27")
    col1.metric("平均分", "72", "-3")
    col2.metric("优秀率(>80)", "46%", "-11%")
    col3.metric("及格率(>=60)", "72%", "-6%")
    col4.metric("不及格率(<60)", "28%", "6%")

    col0.metric("中医3班", "作业一", "2024.1.18")
    col1.metric("平均分", "72", "0")
    col2.metric("优秀率(>80)", "75%", "0%")
    col3.metric("及格率(>=60)", "93%", "0%")
    col4.metric("不及格率(<60)", "7%", "0%")

    col0.metric("中医3班", "作业二", "2024.1.25")
    col1.metric("平均分", "76", "-4")
    col2.metric("优秀率(>80)", "81%", "6%")
    col3.metric("及格率(>=60)", "92%", "-1%")
    col4.metric("不及格率(<60)", "8%", "1%")

    col0.metric("中医3班", "作业三", "2024.2.2")
    col1.metric("平均分", "81", "1")
    col2.metric("优秀率(>80)", "77%", "-4%")
    col3.metric("及格率(>=60)", "86%", "-6%")
    col4.metric("不及格率(<60)", "14%", "-6%")

    col0.metric("中医3班", "期中测试", "2024.2.15")
    col1.metric("平均分", "75", "0")
    col2.metric("优秀率(>80)", "57%", "0%")
    col3.metric("及格率(>=60)", "78%", "0%")
    col4.metric("不及格率(<60)", "22%", "0%")

    col0.metric("中医3班", "期末测试", "2024.2.27")
    col1.metric("平均分", "72", "-3")
    col2.metric("优秀率(>80)", "46%", "-11%")
    col3.metric("及格率(>=60)", "72%", "-6%")
    col4.metric("不及格率(<60)", "28%", "6%")

with tab5:

    table = Table()
    headers = ["班级","姓名", "总分", "选择题", "填空题", "简答题", "画图题","综合题", "班级排名", "专业排名"]
    rows = [
        ["中医1班","小明", 98, 30, 10, 20, 15,23,1,1],
        ["中医1班", "小理", 97, 30, 9, 20, 14, 25, 2, 2],
        ["中医2班", "小王", 96, 30, 10, 18, 13, 25, 1, 3],
        ["中医3班", "小张", 95, 30, 7, 20, 15, 23, 1, 4],
        ["中医2班","小胡", 94, 28, 9, 17, 15,25,2,5],
        ["中医1班", "张三", 93, 27, 8, 18, 15, 25, 3, 6],
        ["中医2班", "李四", 92, 26, 10, 20, 12, 24, 3, 7],
        ["中医3班", "王五", 90, 30, 5, 18, 13, 25, 2, 8],
        ["中医1班","李刚", 88, 26, 10, 15, 12,25,4,9],
        ["中医3班", "王琪", 84, 22, 8, 20, 15, 19, 3, 10],
        ["中医2班", "白明", 83, 30, 5, 14, 10, 24, 4, 11],

    ]
    attributes = {"class": "fl-table"}
    table.add(headers, rows)
    table.set_global_opts(
        {"title": "成绩详情",
         "subtitle": "期末考试",
         "title_style": "style='color:blue'",
         "subtitle_style": "style='color:blue'"
         })
    # table.title_opts={"style":"font-size:10px;font-weight:bold;"}
    components.html(table.render_embed(), height=600, width=1000)

st.markdown(
    '<style>'
    # 题型分布的字体样式
    'p{color: black;font-weight: 700;font-size: 20;}'
    '#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.stTabs.st-emotion-cache-0.esjhkag0 > div > div:nth-child(1){height:60px}'
    '#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.stTabs.st-emotion-cache-0.esjhkag0 > div > div:nth-child(1) > div{height:60px}'
    '#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.stTabs.st-emotion-cache-0.esjhkag0 > div > div:nth-child(1) > div button{height:60px;width:70px}'
    '#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.stTabs.st-emotion-cache-0.esjhkag0 > div > div:nth-child(1) > div button div{height:60px;width:70px}'
    '#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.stTabs.st-emotion-cache-0.esjhkag0 > div > div:nth-child(1) > div button div p{height:60px;width:70px}'

    # 饼状图的样式
    '.main-svg{height:400px;}'
    # 变化率的图的样式
    'div[data-testid="stHorizontalBlock"]{height:350px}'
    'div[data-testid="stVerticalBlockBorderWrapper"]{height:350px}'
    'div[data-testid="stMetricValue"] div{color:blue}'

    '</style>',
    unsafe_allow_html=True)
