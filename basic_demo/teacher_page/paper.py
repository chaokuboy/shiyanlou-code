import streamlit as st
import datetime
from streamlit_modal import Modal
st.set_page_config(
    page_title="智汇中医",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={

    }
)
with st.sidebar:
    text=""
    st.title("题库")
    option = st.selectbox('',
   ("试卷", "作业", "实验"),
   index=0,
   placeholder="请选择题目的用途",label_visibility="collapsed",)
    st.write('你选择的是:', "<h4 style='color: blue;'>"+str(option)+"</h4>",unsafe_allow_html=True)
    if option=="试卷":
        col1, col2= st.columns(2)
        with col1:
            if st.button("保存", type="primary"):
                st.toast('保存成功✅!')
        with col2:
            st.download_button("导出文档",text,file_name="题目.txt",type="primary")
    if option=="作业":
        st.markdown("<h4 style='color: blue;'>选择时间</h4>",unsafe_allow_html=True)
        start = st.date_input("起始日期", "today")
        t = st.time_input('起始时间', "now")
        end = st.date_input("截止日期", "today")
        t1 = st.time_input('截至时间', "now")
        if st.button("发布作业", type="primary"):
            st.toast('发布成功✅!')



ans = 1
cnt = 1
bns=1
with st.container():
    st.write("<h4 style='color: blue;'>选择题</h4>",unsafe_allow_html=True)
    one = st.checkbox(str(ans))
    ans += 1
    st.write("**病人头晕目眩，少气懒言，倦怠乏力，腹泻，腹部坠胀，脱肛，舌淡苔白，脉弱，属于下列哪一证候(   )**")
    colx, coly ,colz= st.columns(3)
    with colx:
        st.write("**A. 气虚证**")
        st.write("**C. 气逆证**")
    with coly:
        st.write("**B. 气血两虚证**")
        st.write("**D. 气陷证**")
    two = st.checkbox(str(ans))
    ans += 1
    st.write("**病人胸胁胀闷或走窜疼痛，性情急躁，胁下痞块，刺痛拒按，入夜甚，舌紫暗或有 瘀斑，脉弦涩，属于下列哪一证候（   ）**")
    colx, coly, colz = st.columns(3)
    with colx:
        st.write("**A. 气滞证**")
        st.write("**C. 气虚血瘀证**")
    with coly:
        st.write("**B. 气滞血瘀证**")
        st.write("**D. 血瘀证**")
    third = st.checkbox(str(ans))
    ans += 1
    st.write("**气陷证发生的主要原因是（   ）**")
    colx, coly, colz = st.columns(3)
    with colx:
        st.write("**A. 情志不遂**")
        st.write("**C. 外感六淫**")
    with coly:
        st.write("**B. 气虚证进一步发展**")
        st.write("**D. 气逆证进一步发展**")
    four = st.checkbox(str(ans))
    ans += 1
    st.write("**下列各项气机失调的证候中，属于实证的是（   ）**")
    colx, coly, colz = st.columns(3)
    with colx:
        st.write("**A. 气脱**")
        st.write("**C. 气逆**")
    with coly:
        st.write("**B. 气虚**")
        st.write("**D. 气不固**")
    five = st.checkbox(str(ans))
    ans += 1
    st.write("**下列哪项不是血虚证形成的原因（   ）**")
    colx, coly, colz = st.columns(3)
    with colx:
        st.write("**A. 失血过多**")
        st.write("**C. 生血不足**")
    with coly:
        st.write("**B. 思虑过度，暗耗阴血**")
        st.write("**D. 虫积肠道，耗吸营养**")
    six = st.checkbox(str(ans))
    ans += 1
    st.write("**血瘀证的主要脉症是（   ）**")
    colx, coly, colz = st.columns(3)
    with colx:
        st.write("**A. 各种出血症状，脉数**")
        st.write("**C. 痛如针刺，痛有定处，脉涩**")
    with coly:
        st.write("**B. 面色萎黄，脉虚而细**")
        st.write("**D. 少气懒言，身倦乏力，脉虚无力**")
    senven = st.checkbox(str(ans))
    ans += 1
    st.write("**病人胸胁脘腹胀闷、疼痛、症状时轻时重，部位常不固定，或窜痛、攻痛，嗳气或 矢气后胀痛减轻，舌淡红，脉弦，其证属(   )**")
    colx, coly, colz = st.columns(3)
    with colx:
        st.write("**A. 血瘀证**")
        st.write("**C. 气滞血瘀证**")
    with coly:
        st.write("**B. 气滞证   **")
        st.write("**D. 气虚血瘀证**")
    eight = st.checkbox(str(ans))
    ans += 1
    st.write("**病人神倦乏力，少气懒言，自汗，胸胁刺痛固定不移，拒按，或胁下痞块，或肢体 瘫痪，半身不遂，舌淡紫，或紫斑，脉涩，其证属(   )**")
    colx, coly, colz = st.columns(3)
    with colx:
        st.write("**A. 气滞血瘀证**")
        st.write("**C. 气血两虚证**")
    with coly:
        st.write("**B. 血瘀证**")
        st.write("**D. 气虚证**")
    night = st.checkbox(str(ans))
    ans += 1
    st.write("**病人畏寒肢冷，神倦乏力，少气懒言，口燥咽干，自汗或盗汗，低热，消瘦，失眠， 尿少水肿，溲清便溏，面色淡白或颧红，脉沉迟无力或虚数，其证属(   )**")
    colx, coly, colz = st.columns(3)
    with colx:
        st.write("**A. 阴阳两虚证**")
        st.write("**C. 阴虚证**")
    with coly:
        st.write("**B. 阳虚证**")
        st.write("**D. 亡阳证**")
    ten = st.checkbox(str(ans))
    ans += 1
    st.write("**病人形体消瘦，午后潮热，五心烦热，或骨蒸劳热，颧红盗汗，大便干燥，尿少色 黄，舌红绛少苔或无苔，脉细数，证属(   )**")
    colx, coly, colz = st.columns(3)
    with colx:
        st.write("**A. 阳虚证**")
        st.write("**C. 阳盛证**")
    with coly:
        st.write("**B. 阴阳两虚证**")
        st.write("**D. 亡阴证**")

    st.write("<h6 style='color: blue;'>填空题</h6>",unsafe_allow_html=True)
    seve = st.checkbox(str(cnt) + ' **. 气陷证是指气虚无力升举而反（   ）所表现的证候**')
    cnt += 1
    eigh = st.checkbox(str(cnt) + ' **. 气逆证是指气机（   ），脏腑之气上逆所表现的证候**')
    cnt += 1
    nigh = st.checkbox(str(cnt) + ' **. 津液不足证是指体内的津液不足，脏腑组织官窍失其濡养所表现的证候，属（   ）证**')
    cnt += 1
    nig = st.checkbox(str(cnt) + ' **. 亡阴证是指机体阴液突然大量(  )，而致全身机能严重衰竭所表现的危重证候**')
    cnt += 1
    ni= st.checkbox(str(cnt) + ' **. 阴阳两虚证以阴液不足和（  ）并见为主要病机**')
    cnt += 1
    nif = st.checkbox(str(cnt) + ' **. 阴盛证是指阴气偏盛，脏腑机能障碍或减退，（   ）过盛所表现的证候**')
    cnt += 1
    nighf = st.checkbox(str(cnt) + ' **. 气随津脱证常由高热、大汗耗伤津液，或严重 （  ）所引起**')
    cnt += 1
    nighft = st.checkbox(str(cnt) + ' **. 气虚血瘀证是指气虚不足，推动血行无力，以致（  ）所表现的证候**')
    cnt += 1

    
    st.write("<h6 style='color: blue;'>简答题</h6>",unsafe_allow_html=True)
    te = st.checkbox(str(bns) + ' **. 气虚证的辨证要点是什么？**')
    bns+=1
    te1 = st.checkbox(str(bns) + ' **. 气陷证的主要临床表现有哪些？**')
    bns+=1
    te2 = st.checkbox(str(bns) + ' **. 何谓血虚证？临床表现有哪些？**')
    bns+=1
    te3 = st.checkbox(str(bns) + ' **. 何谓血热证？其临床表现如何？**')
    bns+=1
    te4= st.checkbox(str(bns) + ' **. 何谓痰证？其临床表现如何？**')
    bns+=1
    te5 = st.checkbox(str(bns) + ' **. 试比较气虚血瘀证和气滞血瘀证的临床表现有何异同？**')
    bns+=1
    te6 = st.checkbox(str(bns) + ' **. 临床上如何鉴别亡阴证和亡阳证？**')
    bns+=1


    
    
    
 
