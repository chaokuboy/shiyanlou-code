import base64

import pages
import streamlit as st
import streamlit.components.v1 as components
from st_pages import Page, show_pages
st.sidebar.title("导航栏")

with st.container():
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16 = st.columns(
        16)
    # with col9:
    #     # st.image("static/img.png")
    # with col10:
    #     # st.write("课程建设")
    # with col11:
    #     # st.image("static/img.png")
    # with col12:
    #     # st.write("教学准备")
    # with col13:
    #     # st.image("static/img.png")
    # with col14:
    #     # st.write("授课运行")
    with col15:
        st.image("static/himg.jpg")
    with col16:
        st.write("李老师")
st.title("学途教育")
st.subheader('学途无忧，智慧教学，学途点亮您前行的路')
st.markdown(
    '<style>'
    '#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5{margin-left:-990px}'
    '#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div{width:1700px;}'

    '#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-r421ms.e1f1d6gn0{height:80px}'
    'img{height:50px;width:50px;border-radius:50%}'
    '#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-0.e1f1d6gn0 > div > div > div > div:nth-child(15){margin-left:16px}'
    '#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-0.e1f1d6gn0 > div > div > div > div:nth-child(16){margin-left:-50px;margin-top:10px}'

    '#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-0.e1f1d6gn0 > div > div > div > div:nth-child(16) > div > div > div > div > div > div > p{font-weight:bold}'
    '</style>',
    unsafe_allow_html=True)


# def bg(headimg):
#     main_bg_ext = "png"
#     st.markdown(
#         f"""
#          <style>
#          #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-0.e1f1d6gn0{{
#              background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(headimg, "rb").read()).decode()});
#              /*  */
#              background-size:contain;
#              height:100px
#          }}
#          </style>
#          """,
#         unsafe_allow_html=True
#     )
# bg('static/classroom.png')


# video_file = open('static/pig.mp4', 'rb')
# video_bytes = video_file.read()
#
# st.video(video_bytes)


components.html("""
<style>
.banner {
width: 1500px;
margin-left:100px ;
height: 350px;
position: relative;
overflow: hidden;}

.imgList {
list-style: none;
width:6900px;
/* width: 2480px;*/
position: absolute;
margin-left:0px
/* left:-620px; */
}

.imgList img {
margin-top:-10px;
margin-left:-40px;
width: 1700px;
height: 350px;
}

.imgList li {
width:1700px;
float: left;
display:inline;
margin-right: 20px;
}

.circle {
position: absolute;
bottom: 15px;
left: 850px;
transform: translateX(-50%);
}

.circle a {
width: 15px;
height: 15px;
background: yellow;
display: block;
border-radius: 50%;
opacity: .5;
float: left;
margin-right: 5px;
cursor: pointer;
}

.circle a.hover {
background: black;
opacity: .8;
}
video{
height:150px;
width:240px;
}
.video ul{
list-style: none;
}
.video ul li{
float: left;
margin-left:100px;
}
.video ul li p{
text-align:center;
font-size:20px;
color:  # 2A2A2A;
}
.videoicon{
width:1900px;
margin-left:-80px;
}
</style>
<div class="banner">
<ul class="imgList">
<li><img src="./app/static/1.png" alt=""></li>
<li><img src="./app/static/2.png" alt=""></li>
<li><img src="./app/static/3.png" alt=""></li>
<li><img src="./app/static/4.png" alt=""></li>
</ul>
<div class="circle">
<!-- <a href=""></a> 
<a href=""></a> 
<a href=""></a> 
<a href=""></a>  -->
</div>
</div>
<div>
<img class="videoicon" src="./app/static/video.png" alt="">
</div>

<div class="video">
<ul>
<li><video src="./app/static/p1.mp4" controls="controls"></video><p>中医诊脉绝学</p></li>
<li><video src="./app/static/p2.mp4" controls="controls"></video><p>中药活血化瘀药</p></li>
<li><video src="./app/static/p3.mp4" controls="controls"></video><p>防治原则</p></li>
<li><video src="./app/static/p4.mp4" controls="controls"></video><p>中医诊断学</p></li>
<li><video src="./app/static/p5.mp4" controls="controls"></video><p>中医学的虚与实</p></li>
</ul>
</div>


<script>
window.onload = function () {
var imgList = document.querySelector('.imgList');
var circle = document.querySelector('.circle');
var thisIndex = 0;
var imgListLi = imgList.children;
var circleA = circle.children;
var flag = true;
//imgList.style.width = imgList.children.length * 620 + 'px';
for (var i = 0; i < imgList.children.length; i++) {
var aNode = document.createElement('a');
aNode.setAttribute('index', i);	//设置自定义属性
if (i == 0) {
aNode.className = 'hover';
}
circle.appendChild(aNode);
}
circle.addEventListener('click', function (e) {
if (flag) {
flag = false;
// console.log(e.target);
if (e.target.nodeName != 'A') {
return false;
}
thisIndex = e.target.getAttribute('index');
// imgList.style.left = -thisIndex * 620 + 'px';
slow(imgList, -thisIndex * 1720, function () {
flag = true;
});
circleChange();
}
})
function antoChange() {
setInterval(function () {
if (flag) {
flag = false;
if (thisIndex >= circleA.length) {
thisIndex = 0;
}
slow(imgList, -thisIndex * 1720, function () {
flag = true;
});
circleChange();
thisIndex++;
}
}, 3000);
}
function circleChange() {
for (var i = 0; i < circleA.length; i++) {
circleA[i].className = '';
}
circleA[thisIndex].className = 'hover';
}
function slow(obj, target, callback) {
obj.myInter = setInterval(function () {
var offsetLeft = obj.offsetLeft;
var num = (target - offsetLeft) / 10;
console.log(offsetLeft+"&"+num)
num > 0 ? num = Math.ceil(num) : num = Math.floor(num);
if (offsetLeft == target) {
clearInterval(obj.myInter);
callback && callback();
} else {
obj.style.left = offsetLeft + num + 'px';
}
}, 10)
}
antoChange();
}
</script>
""", height=800, width=1800)

show_pages(
    [
        Page("main.py", "Home", "🏠"),
        # Can use :<icon-name>: or the actual icon
        # Since this is a Section, all the pages underneath it will be indented
        # The section itself will look like a normal page, but it won't be clickable
        # The pages appear in the order you pass them
        Page("charts.py", "charts", "✏️"),
        Page("exam.py", "Exam", "📖"),
        # Will use the default icon and name based on the filename if you don't
        # pass them
        # You can also pass in_section=False to a page to make it un-indented
        Page("paper.py", "Example Three", "🧰", ),
    ]
)
