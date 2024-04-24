import os
import streamlit as st
from zhipuai import ZhipuAI

st.set_page_config(
    page_title="学途无忧",
    page_icon="🧊",
    layout="wide"
)


st.subheader('智汇中医')
st.markdown("**智汇教育，智慧汇聚，教育创新 智汇点亮您前行的路.:+1::+1::+1:**")

if "history" not in st.session_state:
    st.session_state.history = [{"role":"user","content":"你好！"},{"role":"assistant","content":"你好👋！我是智汇中医教育教育助手智汇AI，很高兴见到你。"}]
if "past_key_values" not in st.session_state:
    st.session_state.past_key_values = None

max_length =8192
top_p =0.8
temperature=0.6
st.sidebar.title("智能答疑")
option = st.sidebar.selectbox(
    '**您想使用的模型助手？**',
    ('图像助手', '文本助手',))
if option=='文本助手':
    st.switch_page("web_demo_streamlit.py")

uploaded_file = st.sidebar.file_uploader("上传一张图像",help="选择一张.jpg或.png")

image_url=st.sidebar.text_input("或者请输入图片的网络地址或base64编码")
buttonClean = st.sidebar.button("清理历史会话", key="clean")
if buttonClean:
    st.session_state.history = []
    st.session_state.past_key_values = None
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    st.rerun()

for i, message in enumerate(st.session_state.history):
    if message["role"] == "user":
        with st.chat_message(name="user", avatar="🧑"):
            st.markdown(message["content"])
    else:
        with st.chat_message(name="assistant", avatar="🧊"):
            st.markdown(message["content"])

with st.chat_message(name="user", avatar="🧑"):
    input_placeholder = st.empty()
with st.chat_message(name="assistant", avatar="🧊"):
    message_placeholder = st.empty()

prompt_text = st.chat_input("请输入您分析图片的问题")

client = ZhipuAI(api_key="173d3bb4228d3548729c16e01390ecaa.6TizfSQXnP4ROXmI") # 填写您自己的APIKey

if prompt_text and image_url:
    input_placeholder.markdown(prompt_text)
    history = st.session_state.history
    past_key_values = st.session_state.past_key_values
    response = client.chat.completions.create(
    model="glm-4v",  # 填写需要调用的模型名称
    messages=[
       {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": prompt_text
          },
          {
            "type": "image_url",
            "image_url": {
                "url" : image_url
            }
          }
        ]
      }
    ]
)
    message_placeholder.markdown(response.choices[0].message.content)
    st.session_state.history = history
    st.session_state.past_key_values = past_key_values
elif prompt_text:
    input_placeholder.markdown(prompt_text)
    history = st.session_state.history
    past_key_values = st.session_state.past_key_values
    response = client.images.generations(
    model="cogview-3", #填写需要调用的模型名称
    prompt=prompt_text
    )
    message_placeholder.markdown(response.data[0].url)
    st.session_state.history = history
    st.session_state.past_key_values = past_key_values
st.markdown(f"""<style>
  .stChatFloatingInputContainer{{
    position: fixed;
    bottom: 50px;
    padding-bottom: 0px;
    padding-top: 0em;
    z-index: 99;
    }}
    </style>""",
    unsafe_allow_html=True)

