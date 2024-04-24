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
import time
st.set_page_config(
    page_title="学途教育",
    page_icon="?",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={

    }
)
col1,col2,col3,col4=st.columns(4)
with col1:
    st.write('**学号：202101010101**')
with col2:
    st.write('**班级：中医1班**')
with col3:
    st.write('**姓名：小明**')
with col4:
    st.write('**截止时间：2023/3/15 24:00**')

st.subheader('作业一')
st.sidebar.title("我的作业")
st.sidebar.write('**中医诊断学**')
st.sidebar.write('作业一')
st.sidebar.write('作业二')

genre1= st.radio("**1.血瘀证的主要脉症是（   ）**",
    ["**A. 各种出血症状，脉数**", "**B. 面色萎黄，脉虚而细**", "**C. 痛如针刺，痛有定处，脉涩**","**D. 少气懒言，身倦乏力，脉虚无力**"],
    
)
st.write("**你选择的答案是:**", "<h6 style='color: red;'>"+str(genre1)+"</h6>",unsafe_allow_html=True)

genre2= st.radio("**2.病人头晕目眩，少气懒言，倦怠乏力，腹泻，腹部坠胀，脱肛，舌淡苔白，脉弱，属于下列哪一证候(   )**",
    ["**A. 气虚证**", "**B. 气血两虚证**", "**C. 气逆证**","**D. 气陷证**"],
    index=1
)
st.write("**你选择的答案是:**", "<h6 style='color: red;'>"+str(genre2)+"</h6>",unsafe_allow_html=True)
genre3= st.radio("**3.病人胸胁胀闷或走窜疼痛，性情急躁，胁下痞块，刺痛拒按，入夜甚，舌紫暗或有 瘀斑，脉弦涩，属于下列哪一证候（   ）**",
    ["**A. 气滞证**", "**B. 气滞血瘀证**", "**C. 气虚血瘀证**","**D. 血瘀证**"],
    index=2
)
st.write("**你选择的答案是:**", "<h6 style='color: red;'>"+str(genre3)+"</h6>",unsafe_allow_html=True)

genre4= st.radio("**4.气陷证发生的主要原因是（   ）**",
    ["**A. 情志不遂**", "**B. 气虚证进一步发展**", "**C. 外感六淫**","**D. 气逆证进一步发展**"],
    index=3
)
st.write("**你选择的答案是:**", "<h6 style='color: red;'>"+str(genre4)+"</h6>",unsafe_allow_html=True)

genre5= st.radio("**5.血瘀证的主要脉症是（   ）**",
    ["**A. 各种出血症状，脉数**", "**B. 面色萎黄，脉虚而细**", "**C. 痛如针刺，痛有定处，脉涩**","**D. 少气懒言，身倦乏力，脉虚无力**"],
    index=2
)
st.write("**你选择的答案是:**", "<h6 style='color: red;'>"+str(genre5)+"</h6>",unsafe_allow_html=True)

genre6= st.radio("**6.下列哪项不是血虚证形成的原因（   ）**",
    ["**A. 失血过多**", "**B. 思虑过度，暗耗阴血**", "**C. 生血不足**","**D. 虫积肠道，耗吸营养**"],
    index=3
)
st.write("**你选择的答案是:**", "<h6 style='color: red;'>"+str(genre6)+"</h6>",unsafe_allow_html=True)

title1 = st.text_input('**7. 气陷证是指气虚无力升举而反（   ）所表现的证候**', '')
st.write('**当前填空的内容是**', "<h6 style='color: red;'>"+title1+"</h6>",unsafe_allow_html=True)

title2 = st.text_input('**8. 津液不足证是指体内的津液不足，脏腑组织官窍失其濡养所表现的证候，属（   ）证**', '')
st.write('**当前填空的内容是**', "<h6 style='color: red;'>"+title2+"</h6>",unsafe_allow_html=True)

title3 = st.text_input('**9. 饮证常由外邪侵袭，或（  ）等脏腑机能衰退或障碍等原因所引起**', '')
st.write('**当前填空的内容是**', "<h6 style='color: red;'>"+title3+"</h6>",unsafe_allow_html=True)

title4 = st.text_input('**10. 阴盛证是指阴气偏盛，脏腑机能障碍或减退，（  ）过盛所表现的证候**', '')
st.write('**当前填空的内容是**', "<h6 style='color: red;'>"+title4+"</h6>",unsafe_allow_html=True)

st.write("<h6>11. 舌诊”之描述下图是由什么引起的？</h6>",unsafe_allow_html=True)
st.image('./pic/1.png')
title5 = st.text_input('作答', '')

st.write("<h6>12. 画图题:画出舌体脏腑图。</h6>",unsafe_allow_html=True)
st.image('./pic/2.png')
uploaded_files = st.file_uploader("Choose a image", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
col4,col5,col6,col7,col8,col9=st.columns(6)
with col6:
    if st.button('暂时保存',type="primary"):
        st.toast('保存成功✅!')
with col7:
    st.button('提交作业',type="primary")
            
progress_text = "**正在批改作业，请稍等...**"
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.05)
    my_bar.progress(percent_complete + 1, text=progress_text)
my_bar.empty()
time.sleep(1)
st.write("<h4 style='color: red;'>作业得分:90分</h4>",unsafe_allow_html=True)


   