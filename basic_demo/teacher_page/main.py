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
        if st.button("AI助手",type="primary"):
            st.switch_page("web_demo_streamlit.py")
    with coly:
        st.image("./static/成绩分析.png")
        if st.button("成绩分析",type="primary"):
            st.switch_page("charts.py")
    with colz:
        st.image("./static/智能教学平台.png")
        if st.button("智能教学",type="primary"):
            st.switch_page("exam.py")
    with c1:
        st.image("./static/学堂.png")
        if st.button("我的题库",type="primary"):
            st.switch_page("paper.py")
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

col1, col2, col3,col4,col5= st.columns(5)



with col1:

    st.markdown("**:gray[中医诊断学]**")
    st.image("./static/img_7.png")

with col2:
    st.markdown("**:gray[中医食疗学]**")
    st.image("./static/img_6.png")

with col3:
    st.markdown("**:gray[中医药与中华传统文化]**")
    st.image("./static/img_8.png")
with col4:
    st.markdown("**:gray[走进神奇的中医药]**")
    st.image("./static/img_9.png")
with col5:
    st.markdown("**:gray[解密黄帝内经]**")
    st.image("./static/img_10.png")

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
        Page("web_demo_streamlit.py", "AI助手", "🧊"),
        Page("charts.py", "成绩分析", "📈"),
        Page("coview.py", "智能教学", "💻"),
         Page("paper.py", "我的题库", "📑")
       
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
