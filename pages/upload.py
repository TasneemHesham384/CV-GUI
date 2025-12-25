import streamlit as st
import base64
import time

st.set_page_config(page_title="Bone Vision", layout="wide")

# ================== session state ==================
if "uploaded" not in st.session_state:
    st.session_state.uploaded = None
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

# ================== إخفاء عناصر Streamlit و FileUploader ==================
st.markdown("""
<style>
header, footer, .stAppHeader {display:none !important;}
.stApp {
    background-color: black;
}
.stFileUploader {
    position: absolute;
    top: 660px;         /* المكان اللي فيه زرار Browse Files في شاشتك */
    left: 50%;
    transform: translate(-50%, -50%);
    width: 210px;       /* عرض الزرار */
    height: 50px;       /* طول الزرار */
    opacity: 0;        
    z-index: 10000;    
    cursor: pointer;
}
div.stButton > button {
   border: 2px solid #6091F3;
    color: #6091F3 !important;
    padding: 12px 45px;
    border-radius: 30px;
    font-weight: bold;
    display: inline-block;
    font-size: 18px;
    cursor:pointer;    
    opacity: 1 !important;              
    visibility: visible !important;       
</style>
""", unsafe_allow_html=True)

# ================== base64 ==================
def get_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

logo = get_base64("photo_2025-12-20_00-52-09.jpg")
cloud = get_base64("cloud upload.png")

# ================== File uploader المخفي ==================
uploaded_file = st.file_uploader("", type=["jpg","png"], label_visibility="collapsed")
if uploaded_file:
    st.session_state.uploaded = uploaded_file
    st.session_state.analyzed = False

# ================== محتوى الكارد ==================
if st.session_state.uploaded:
    uploaded_b64 = base64.b64encode(st.session_state.uploaded.read()).decode()
    st.session_state.uploaded.seek(0)
    
    card_inner = f"""
        <img src="data:image/png;base64,{uploaded_b64}" 
             style="width:500px; border-radius:20px; margin-bottom:20px;">
    """
    
    analyze_button = st.button("Analyze X-ray")
    if analyze_button:
        progress = st.progress(0)
        for i in range(101):
            time.sleep(0.01)
            progress.progress(i)
        st.success("Analysis completed successfully")

else:
    card_inner = f"""
        <img src="data:image/png;base64,{cloud}" class="cloud-img">
        <div class="drag-text">Drag & Drop your X-ray Image</div>
        <div class="formats">Supported formats: JPG, PNG</div>
        <div class="browse-btn" onclick="document.querySelector('.stFileUploader').click();">
            Browse Files
        </div>
    """
# ================== HTML ==================
html_content = f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{
    background-color: black;
    color: white;
    font-family: Arial, sans-serif;
    margin: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
}}

.logo {{
    width: 261px;
    margin-top: 40px;
}}

.subtitle {{
    color: #6091F3;
    font-size: 18px;
    margin: 15px 0 40px;
    text-align: center;
}}

.card {{
    border: 2px solid white;
    border-radius: 40px;
    padding: 60px 20px;
    width: 750px;
    text-align: center;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
}}

.cloud-img {{
    width: 214px;
    margin-bottom: 20px;
}}

.drag-text {{
    font-size: 26px;
    font-weight: bold;
    margin-bottom: 5px;
}}

.formats {{
    color: #888;
    font-size: 14px;
    margin-bottom: 30px;
}}

.browse-btn {{
    border: 2px solid #6091F3;
    color: #6091F3;
    padding: 12px 45px;
    border-radius: 30px;
    font-weight: bold;
    display: inline-block;
    font-size: 18px;
    cursor:pointer;
}}

.nav-container {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 850px;
    margin-top: 30px;
}}

.nav-item {{
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #6091F3;
    font-weight: bold;
}}

.icon-box {{
    background: white;
    color: black;
    width: 45px;
    height: 35px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 5px;
    font-size: 20px;
}}

.footer {{
    color: #444;
    font-size: 12px;
}}
</style>
</head>

<body>

<img src="data:image/png;base64,{logo}" class="logo">

<div class="subtitle">
Upload your X-ray image for instant fracture detection using our AI Algorithm
</div>

<div class="card">
    {card_inner}
</div>

<div class="nav-container">
    <div class="nav-item">
        <div class="icon-box">↩</div>
        Back
    </div>

    <div class="footer">
        Developed by BoneVision Team © 2025
    </div>

    <div class="nav-item">
        <div class="icon-box">➡</div>
        Exit
    </div>
</div>

<script>
window.addEventListener("message", function(event) {{
    if(event.data.analyze === "true") {{
        fetch("/analyze_trigger", {{method:"POST"}});
    }}
}});
</script>

</body>
</html>
"""

st.components.v1.html(html_content, height=900)

# ================== تحليل الصورة ==================
if st.session_state.uploaded and not st.session_state.analyzed:
    analyze_trigger = st.button("", key="hidden_trigger")  # زرار مخفي فقط لتمثيل التحليل
    if analyze_trigger:
        st.session_state.analyzed = True
        progress = st.progress(0)
        for i in range(101):
            time.sleep(0.01)
            progress.progress(i)
        st.success("Analysis completed successfully")

st.markdown("""
<style>
    /* إخفاء القائمة الجانبية بالكامل */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* إخفاء زرار القائمة الجانبية (السهم الصغير) */
    [data-testid="stSidebarNav"] {
        display: none;
    }
    
    /* توسيع الصفحة لتأخذ المساحة كاملة بعد إخفاء الشريط */
    [data-testid="stAppViewBlockContainer"] {
        width: 100% !important;
        max-width: 100% !important;
        margin-left: 0 !important;
    }
</style>
""", unsafe_allow_html=True)