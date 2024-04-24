import base64
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts

st.set_page_config(
    page_title="学途教育",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={

    }
)




# 考试概览
with st.container(height=160, border=True):
    st.write("**我的考试**")
    data2 = {'排名': ['1'], '姓名': ['小明'], '总用时': ['1.33h'], '总分': ['98'], '选择题': ['30'], '填空题': ['10'],
             '简答题': ['20'], '画图题': ['15'], '成绩等级': ['优秀'], '书写卷面': ['良好'], '书写区域': ['合格']}
    df = pd.DataFrame(data2, columns=(
        ['排名', '姓名', '总用时', '总分', '选择题', '填空题', '简答题', '画图题', '成绩等级', '书写卷面', '书写区域']))
    st.dataframe(df, use_container_width=True)

# 分数/时间
with st.container(height=585, border=True):
    st.write("**分数/题型**")
    bar = Bar()
    bar.add_xaxis(['总分', '选择题', '填空题', '简答题', '画图题'])
    bar.add_yaxis('班级最高分', [100, 20, 15, 40, 25])
    bar.add_yaxis('班级平均分', [76, 12, 9, 35, 20])
    bar.add_yaxis('个人分', [80, 16, 9, 31, 24])
    bar.add_yaxis('班级最低分', [42, 8, 3, 20, 11])
    bar.set_series_opts(markline_opts=opts.MarkLineOpts(
        data=[opts.MarkLineItem(type_='max', name='最大值')]
        ))
    barHtml = bar.render_embed()  # 将折线组件转换成html文本
    components.html(barHtml, height=500, width=900)
        
with st.container(height=585, border=True):
    st.write("**书写时长**")
    bar2 = Bar()
    bar2.add_xaxis(['班级最低', '班级平均', '个人时长', '班级最高'])
    bar2.add_yaxis('总时长', [82, 102, 90, 120])
    bar2.add_yaxis('书写时长', [71, 80, 75, 92])
    bar2.add_yaxis('停顿时长', [11, 22, 15, 35])
    bar2.set_series_opts(markline_opts=opts.MarkLineOpts(
        data=[opts.MarkLineItem(type_='max', name='最大值')]
        ))
    bar2Html = bar2.render_embed()  # 将折线组件转换成html文本
    components.html(bar2Html, height=500, width=900)

# 考试分析
with st.container(height=390, border=True):
    st.write("**考试分析**")
    col1, col2 = st.columns(2)
    with col1:
        with st.container(height=320, border=True):
            colq, colw, cole, colr = st.columns(4)
            with colq:
                if st.button("第一题(问疼痛)",type="secondary",key="1"):
                     with col2:
                         with st.container(height=320, border=True):
                            st.write("**错题分析**")
                            st.write("<h6 style='color: blue;'>第十三题、气滞证的疼痛特点是(  )</h6>",unsafe_allow_html=True)
                            colx, coly = st.columns(2)
                            with colx:
                                st.write("<h6 style='color: blue;'>A. 攻痛</h6>",unsafe_allow_html=True)
                                st.write("<h6 style='color: blue;'>C. 窜痛</h6>",unsafe_allow_html=True)
                                st.write("<h6 style='color: blue;'>正确答案 ABC</h6>",unsafe_allow_html=True)
                            with coly:
                                st.write("<h6 style='color: blue'>B. 胀痛</h6>",unsafe_allow_html=True)
                                st.write("<h6 style='color: blue;'>D. 刺痛</h6>",unsafe_allow_html=True)
                                st.write("<h6 style='color: blue;'>你的答案 ABC</h6>",unsafe_allow_html=True)
                            st.write("**解析：气滞证以胀痛、窜痛、攻痛为主要疼痛特点**")
                    
                st.button("第五题(问症状)",type="secondary",key="2")
                st.button("第九题(问依据)",type="secondary",key="3")
                
                if st.button("第十三题(脉数)",type="primary",key="4"):
                     with col2:
                         with st.container(height=320, border=True):
                            st.write("**错题分析**")
                            st.write("<h6 style='color: red;'>第十三题、病人头晕目眩，少气懒言，倦怠乏力，腹泻，腹部坠胀，脱肛，舌淡苔白，脉弱，属于下列哪一证候(   )</h6>",unsafe_allow_html=True)
                            colx, coly = st.columns(2)
                            with colx:
                                st.write("<h6 style='color: red;'>A. 气虚证</h6>",unsafe_allow_html=True)
                                st.write("<h6 style='color: red;'>C. 气逆证</h6>",unsafe_allow_html=True)
                                st.write("<h6 style='color: red;'>正确答案 D</h6>",unsafe_allow_html=True)
                            with coly:
                                st.write("<h6 style='color: red;'>B. 气血两虚证</h6>",unsafe_allow_html=True)
                                st.write("<h6 style='color: red;'>D. 气陷证</h6>",unsafe_allow_html=True)
                                st.write("<h6 style='color: red;'>你的答案 A</h6>",unsafe_allow_html=True)
                            st.write("**解析：气陷证是指气虚无力升举而反下陷所表现的证候。临床表现为久泻久痢，伴见头晕目眩、少气懒 言、倦怠乏力、舌淡苔白、脉弱**")
                st.button("第十七题(发展)",type="secondary",key="05")
            with colw:
                st.button("第二题(问瘀斑)",type="secondary",key="6")
                st.button("第六题(问脏腑)",type="secondary",key="7")
                st.button("第十题(问阴虚)",type="secondary",key="8")
                st.button("第十四题(辨证)",type="secondary",key="9")
                if st.button("第十八题(气虚)",type="primary",key="10"):
                     with col2:
                         with st.container(height=320, border=True):
                            st.write("**错题分析**")
                            st.write("<h6 style='color: red;'>第十八题、病人胸胁胀闷或走窜疼痛，性情急躁，胁下痞块，刺痛拒按，入夜甚，舌紫暗或有 瘀斑，脉弦涩，属于下列哪一证候(   )</h6>",unsafe_allow_html=True)
                            colx, coly = st.columns(2)
                            with colx:
                                st.write("<h6 style='color: red;'>A. 气滞证</h6>",unsafe_allow_html=True)
                                st.write("<h6 style='color: red;'>C. 气虚血瘀证</h6>",unsafe_allow_html=True)
                                st.write("<h6 style='color: red;'>正确答案 B</h6>",unsafe_allow_html=True)
                            with coly:
                                st.write("<h6 style='color: red;'>B. 气滞血瘀证</h6>",unsafe_allow_html=True)
                                st.write("<h6 style='color: red;'>D. 血瘀证</h6>",unsafe_allow_html=True)
                                st.write("<h6 style='color: red;'>你的答案 C</h6>",unsafe_allow_html=True)
                            st.write("**解析：气滞血瘀证是指气机阻滞而致血行瘀阻所表现的证候。其临床表现为胸胁胀满或走窜疼痛，性情急躁，胁下痞块，刺痛拒按舌,紫暗或有瘀斑，脉弦涩**")
            with cole:
                if st.button("第三题(问实证)",type="primary",key="11"):
                    with col2:
                         with st.container(height=320, border=True):
                            st.write("**错题分析**")
                            st.write("<h6 style='color: red;'>第三题、下列各项气机失调的证候中，属于实证的是</h6>",unsafe_allow_html=True)
                            colx, coly = st.columns(2)
                            with colx:
                                st.write("<h6 style='color: red;'>A. 气脱</h6>",unsafe_allow_html=True)
                                st.write("<h6 style='color: red;'>C. 气虚</h6>",unsafe_allow_html=True)
                                st.write("<h6 style='color: red;'>正确答案 B</h6>",unsafe_allow_html=True)
                            with coly:
                                st.write("<h6 style='color: red;'>B. 气逆</h6>",unsafe_allow_html=True)
                                st.write("<h6 style='color: red;'>D. 气不固</h6>",unsafe_allow_html=True)
                                st.write("<h6 style='color: red;'>你的答案 D</h6>",unsafe_allow_html=True)
                            st.write("**解析：气滞、气逆多属于实证**")
                st.button("第七题(问饮食)",type="secondary",key="12")
                st.button("第十一题(舌诊)",type="secondary",key="13")
                st.button("第十五题(问诊)",type="secondary",key="14")
            with colr:
                st.button("第四题(问口味)",type="secondary",key="15")
                st.button("第八题(问二便)",type="secondary",key="16")
                st.button("第十二题(闻诊)",type="primary",key="18")
                st.button("第十六题(经带)",type="secondary",key="17")
                # st.write("**第四题(问饮食口味)**")
                # st.write("**第八题(问二便)**")
                # st.write("<h6 style='color: red;'>第十二题(发展简史)</h6>",unsafe_allow_html=True)
                # st.write("**第十六题(问经带)**")
        

# 习题推荐
with st.container(height=250, border=True):
    st.write("**学习要点**")
    st.write("**1、明确寒热产生的类型有四类：恶寒发热、但寒不热、但热不寒、寒热往来。**")
    st.write("**2、恶寒发热的临床意义。**")
    st.write("**3、但寒不热的临床意义。**")
    st.write(
        "**4、但热不寒（壮热、潮热、微热）的临床意义；潮热三种类型（阳明潮热、湿温潮热、阴虚潮热）的特点及临床意义；阴虚发热的机理。**")

# 视频推荐
with st.container(height=250, border=True):
    st.write("**视频推荐**")
    components.html("""
<style>
video{
height:120px;
width:200px;
}
.video ul{
list-style: none;
}
.video ul li{
float: left;
margin-left:50px;
}
.video ul li p{
text-align:center;
font-size:16px;
color:  # 2A2A2A;
}
</style>

<div class="video">
<ul>
<li><video src="./app/static/p1.mp4" controls="controls"></video><p>创新与人文教育</p></li>
<li><video src="./app/static/p2.mp4" controls="controls"></video><p>创新与人文教育</p></li>
<li><video src="./app/static/p3.mp4" controls="controls"></video><p>创新与人文教育</p></li>
<li><video src="./app/static/p4.mp4" controls="controls"></video><p>创新与人文教育</p></li>
<li><video src="./app/static/p5.mp4" controls="controls"></video><p>创新与人文教育</p></li>
</ul>
</div>
""", height=150, width=1500)

