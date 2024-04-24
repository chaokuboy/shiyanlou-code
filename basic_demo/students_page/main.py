import base64

import streamlit as st
import streamlit.components.v1 as components
from st_pages import Page, show_pages


st.set_page_config(
    page_title="学途教育",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={

    }
)


st.sidebar.title("首页")
st.sidebar.image("./static/4.png")
st.header("学途无忧")
st.markdown(":balloon: ***学途教育***  ***智慧教学***:+1: ***学途点亮您前行的路***.:balloon:")
with st.container(height=160):
    colx,coly,colz,c1,c3,c2=st.columns(6)
    with colx:
        st.image("./static/Al-Chatbot1.png")
        if st.button("智能答疑",type="primary"):
            st.switch_page("web_demo_streamlit.py")
    with coly:
        st.image("./static/作业-选中.png")
        if st.button("我的作业",type="primary"):
            st.switch_page("homework.py")
    with colz:
        st.image("./static/成绩管理-01.png")
        if st.button("我的成绩",type="primary"):
            st.switch_page("exam.py")
    with c1:
        st.image("./static/学堂.png")
        if st.button("我的学堂",type="primary"):
            st.switch_page("exam.py")
    with c3:
        st.image("./static/课程.png")
        if st.button("我的课程",type="primary"):
            st.switch_page("exam.py")
    with c2:
        st.image("./static/个人中心.png")
        if st.button("个人中心",type="primary"):
            st.switch_page("exam.py")
st.image("./static/img_3.png")
st.image("./static/img_4.png")


st.divider()
st.write("<h4>已选课程</h4>",unsafe_allow_html=True)
col1, col2, col3,col4,col5= st.columns(5)



with col1:

    
    st.image("./static/img_7.png")
    st.markdown("**:gray[中医诊断学]**")

with col2:
    
    st.image("./static/img_6.png")
    st.markdown("**:gray[中医食疗学]**")

with col3:
    
    st.image("./static/img_8.png")
    st.markdown("**:gray[中医药与中华传统文化]**")
with col4:
    
    st.image("./static/img_9.png")
    st.markdown("**:gray[走进神奇的中医药]**")
with col5:
    
    st.image("./static/img_10.png")
    st.markdown("**:gray[解密黄帝内经]**")

st.divider()
st.write("<h4>推荐课程</h4>",unsafe_allow_html=True)
colx, coly, colz,colm,coln= st.columns(5)

with colx:

    
    st.image("./static/pic1.png")
    st.markdown("**:gray[常见中医护理技术]**")

with coly:
    
    st.image("./static/pic2.png")
    st.markdown("**:gray[中医养生]**")

with colz:
    
    st.image("./static/pic3.png")
    st.markdown("**:gray[中医护理基础]**")
with colm:
    
    st.image("./static/pic4.png")
    st.markdown("**:gray[中医美容实用技术]**")
with coln:
    
    st.image("./static/pic5.png")
    st.markdown("**:gray[高黎贡山中医药食智慧]**")
    
st.divider()

st.image("./static/img_11.png")

st.divider()

st.image("./static/img_12.png")


show_pages(
    [
        Page("main.py", "首页", "🏠"),
        # Can use :<icon-name>: or the actual icon
        # Since this is a Section, all the pages underneath it will be indented
        # The section itself will look like a normal page, but it won't be clickable
        # The pages appear in the order you pass them
        Page("web_demo_streamlit.py", "智能答疑", "🧊"),
        Page("homework.py", "我的作业", "📖"),
        Page("exam.py", "我的成绩", "📊"),
        Page("coview.py", "我的学堂", "🏫")
       
        # Will use the default icon and name based on the filename if you don't
        # pass them
        # You can also pass in_section=False to a page to make it un-indented
    
    ]
)


st.markdown(f"""<style>
  .st-emotion-cache-10trblm{{
    position: ;
    flex: 1 1 0%;
    margin-left: calc(3rem);
    text-align:left
    }}
    </style>""",
    unsafe_allow_html=True)
