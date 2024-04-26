"""
This script is a simple web demo based on Streamlit, showcasing the use of the ChatGLM3-6B model. For a more comprehensive web demo,
it is recommended to use 'composite_demo'.

Usage:
- Run the script using Streamlit: `streamlit run web_demo_streamlit.py`
- Adjust the model parameters from the sidebar.
- Enter questions in the chat input box and interact with the ChatGLM3-6B model.

Note: Ensure 'streamlit' and 'transformers' libraries are installed and the required model checkpoints are available.
"""

import os
import streamlit as st
import torch
from transformers import AutoModel, AutoTokenizer

MODEL_PATH = os.environ.get('MODEL_PATH', '/root/autodl-tmp/ChatGLM3/finetune_demo/outputdir')
TOKENIZER_PATH = os.environ.get("TOKENIZER_PATH", MODEL_PATH)

st.set_page_config(
    page_title="智汇中医",
    page_icon="🧊",
    layout="wide"
)

st.subheader('智汇中医')

st.markdown("***智汇中医教育，开启智慧之旅，成就未来之星***:+1: ***智汇中医点亮您前行的路***.:sunglasses:")


@st.cache_resource
def get_model():

    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH, trust_remote_code=True)
    model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True, device_map="auto").eval()
    return tokenizer, model


# 加载Chatglm3的model和tokenizer
tokenizer, model = get_model()


if "history" not in st.session_state:
    st.session_state.history = [{"role":"user","content":"你好！"},{"role":"assistant","content":"你好👋！我是智汇中医教育助手学途AI，很高兴见到你，欢迎问我任何问题。"}]
if "past_key_values" not in st.session_state:
    st.session_state.past_key_values = None

max_length =8192
top_p =0.8
temperature=0.6
st.sidebar.title("AI助手")
option = st.sidebar.selectbox(
    '**您想使用的模型助手？**',
    ('文本助手', '图像助手',))
if option=='图像助手':
    st.switch_page("coview.py")
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

prompt_text = st.chat_input("请输入您的问题")
if prompt_text:
    input_placeholder.markdown(prompt_text)
    history = st.session_state.history
    past_key_values = st.session_state.past_key_values
    for response, history, past_key_values in model.stream_chat(
            tokenizer,
            prompt_text,
            history,
            past_key_values=past_key_values,
            max_length=max_length,
            top_p=top_p,
            temperature=temperature,
            return_past_key_values=True,
    ):
        message_placeholder.markdown(response)
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
