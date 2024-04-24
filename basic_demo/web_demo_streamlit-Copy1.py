"""
This script is a simple web demo based on Streamlit, showcasing the use of the ChatGLM3-6B model. For a more comprehensive web demo,
it is recommended to use 'composite_demo'.

Usage:
- Run the script using Streamlit: `streamlit run web_demo_streamlit.py`
- Adjust the model parameters from the sidebar.
- Enter questions in the chat input box and interact with the ChatGLM3-6B model.

Note: Ensure 'streamlit' and 'transformers' libraries are installed and the required model checkpoints are available.
"""
import base64
import os
import streamlit as st
import torch
from typing import Union
from pathlib import Path

from peft import AutoPeftModelForCausalLM, PeftModelForCausalLM
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    PreTrainedModel,
    PreTrainedTokenizer,
    PreTrainedTokenizerFast,
)

ModelType = Union[PreTrainedModel, PeftModelForCausalLM]
TokenizerType = Union[PreTrainedTokenizer, PreTrainedTokenizerFast]

MODEL_PATH = os.environ.get('MODEL_PATH', '/root/autodl-tmp/ChatGLM3/chatglm3-6b')
TOKENIZER_PATH = os.environ.get("TOKENIZER_PATH", MODEL_PATH)
                               
model_dir = "/root/autodl-tmp/ChatGLM3/finetune_demo/output/checkpoint-3000"
st.set_page_config(
    page_title="学途教育",
    page_icon="🧊",
    layout="wide"
)

st.title('学途教育')
'### 学途无忧，开启智慧之旅，成就未来之星！'

# def sidebar_bg(side_bg):
 
#    side_bg_ext = 'png'
 
#    st.markdown(
#       f"""
#       <style>
#       [data-testid="stSidebar"] > div:first-child {{
#           background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
#       }}
#       </style>
#       """,
#       unsafe_allow_html=True,
#       )
 
# #调用
# sidebar_bg('./pic/background1.jpg')


@st.cache_resource    
def _resolve_path(path: Union[str, Path]) -> Path:
    return Path(path).expanduser().resolve()
    
def get_model(model_dir: Union[str, Path], trust_remote_code: bool = True) -> tuple[ModelType, TokenizerType]:
    model_dir = _resolve_path(model_dir)
    if (model_dir / 'adapter_config.json').exists():
        model = AutoPeftModelForCausalLM.from_pretrained(
            model_dir, trust_remote_code=trust_remote_code, device_map='auto'
        )
        tokenizer_dir = model.peft_config['default'].base_model_name_or_path
    else:
        model = AutoModelForCausalLM.from_pretrained(
            model_dir, trust_remote_code=trust_remote_code, device_map='auto'
        )
        tokenizer_dir = model_dir
    tokenizer = AutoTokenizer.from_pretrained(
        tokenizer_dir, trust_remote_code=trust_remote_code
    )
    return model, tokenizer

# 加载Chatglm3的model和tokenizer
model,tokenizer= get_model(model_dir, trust_remote_code=True)

if "history" not in st.session_state:
    st.session_state.history = [{"role":"user","content":"你好！"},{"role":"assistant","content":"你好👋！我是学途无忧教育助手学途AI，很高兴见到你，欢迎问我任何问题。"}]
     
if "past_key_values" not in st.session_state:
    st.session_state.past_key_values = None

max_length = st.sidebar.slider("Max_length", 0, 32768, 8192, step=1)
top_p = st.sidebar.slider("Top P", 0.0, 1.0, 0.8, step=0.01)
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.6, step=0.01)

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
    
with st.empty():
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
        message_placeholder.markdown('初步诊断'+response[:5]+'、'+response[5:])
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
st.markdown(f"""<style>
  .st-emotion-cache-10trblm{{
    position: ;
    flex: 1 1 0%;
    margin-left: calc(3rem);
    text-align:center
    }}
    </style>""",
    unsafe_allow_html=True)

