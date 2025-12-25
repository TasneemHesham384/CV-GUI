import streamlit as st
from PIL import Image

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Bone Vision", layout="centered")

# --- إضافة منطق إظهار الأسماء (الجزء الجديد فقط) ---
if 'show_group' not in st.session_state:
    st.session_state.show_group = False

def toggle_group():
    st.session_state.show_group = not st.session_state.show_group
# -----------------------------------------------

# 2. تحميل الصور
LOGO_PATH = "photo_2025-12-20_00-23-05.jpg"
HAND_PATH = "photo_2025-12-20_02-41-37.jpg"

# 3. الـ CSS الكامل والمعدل
st.markdown("""
<style>
    /* إخفاء الهيدر وتقليل المسافات العلوية */
    [data-testid="stHeader"] {display: none !important;}
    .block-container {padding-top: 1rem !important; padding-bottom: 0rem !important;}
    .stApp {background-color: black;}

    /* تصفير الفراغات بين بلوكات ستريمليت */
    [data-testid="stVerticalBlock"] {gap: 0rem !important;}
            
    /* (1) اللوجو – حجم مناسب للويب + مسافة أقل */
    .logo-container {
        text-align: center;
        width: 100%;
        display: block;
    }
    .logo-container img {
        width: 300px !important;              /* تم تصغير الحجم */
        height: auto !important;
        margin-bottom: -10px !important;     /* تم تقليل المسافة */
        display: block;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* (2) تنسيق العنوان الأزرق */
    .sub-title {
        color: #6091F3;
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        line-height: 1.1;
        margin-top: -20px !important;        /* تقليل المسافة */
        margin-bottom: 20px;
    }

    /* (3) تنسيق الزرار (بدون أي تغيير) */
    div.stButton > button {
        background-color: rgba(0,0,0,0.5) !important;
        color: white !important;
        border: 2px solid white !important;
        border-radius: 50px !important;
        padding: 8px 50px !important;
        font-size: 18px !important;
        display: block;
        margin: 0 auto !important;
        transform: translate(280px, 220px); 
        position: relative;
        z-index: 999;
        backdrop-filter: blur(5px);
    }
    div.stButton > button:hover {
        background-color: rgba(96,145,243,0.15) !important; /* أزرق خفيف */
        border-color: #6091F3 !important;
        color: #6091F3 !important;
        transform: translate(280px, 220px) scale(1.05); /* تكبير بسيط */
        transition: all 0.3s ease;
        cursor: pointer;
    }

    /* (4) رفع صورة الإيد لفوق */
    div[data-testid="stColumn"] img {
        margin-top: -20px !important; 
    }
    .hand-img img {
    margin-top: -20px !important;
            
    }

    /* (5) تنسيق الفوتر */
    .footer-container {
        position: fixed;
        bottom: 120px;
        left: 5%;
        right: 5%;
        display: flex;
        justify-content: space-between;
        z-index: 100;
    }

    /* (6) تنسيق قائمة الأسماء (زي الصورة بالضبط) */
    .names-box {
        position: fixed;
        bottom: 180px;
        left: 40px;
        background-color: black;
        border: 2px solid white;
        border-radius: 20px;
        padding: 20px;
        color: white;
        z-index: 1000;
        text-align: center;
        min-width: 200px;
    }
    .names-box h3 {
        margin: 10px 0;
        font-family: sans-serif;
        font-size: 18px;
    }

    /* زر شفاف فوق أيقونة الجروب */
    .group-trigger {
        position: fixed;
        bottom: 120px;
        left: 5%;
        width: 80px;
        height: 60px;
        cursor: pointer;
        z-index: 1001;
        background: transparent;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# --- التنفيذ الفعلي للعناصر ---

# 1. اللوجو
col1, col2, col3 = st.columns([2, 3, 2])
with col2:
    try:
        st.image(LOGO_PATH, width=800)
    except:
        st.error("Logo not found")

# 2. العنوان الفرعي
st.markdown(
    '<p class="sub-title">Ai-Powered Bone Fracture<br>Detection System</p>',
    unsafe_allow_html=True
)

# 3. الزرار
if st.button("Try Now!"):
    try:
        st.switch_page("pages/upload.py")
    except Exception as e:
        st.error(f"Error: {e}")

# 4. صورة الإيد
col_h1, col_h2, col_h3 = st.columns([1.6, 1, 1.6])
with col_h2:
    try:
        img = Image.open(HAND_PATH)
        st.image(img, use_container_width=True)
    except:
        st.error("Hand image not found")

# --- قائمة الأسماء (تظهر عند الضغط) ---
if st.session_state.show_group:
    st.markdown("""
    <div class="names-box">
        <h3>Salma Khalil</h3>
        <h3>Alaa Ahmed</h3>
        <h3>Tasneem Hisham</h3>
        <h3>Esraa Kamel</h3>
        <h3>Maya Mohamed</h3>
        <h3>Fatima Abdelazim</h3>
    </div>
    """, unsafe_allow_html=True)

# 5. الفوتر (مع زر مخفي فوق كلمة Group)
st.markdown("""
<div class="footer-container">
    <div style="text-align: center;">
        <div style="color: #FFFFFF; font-size: 24px;">⠿</div>
        <div style="color: #6091F3; font-weight: bold;">Group</div>
    </div>
    <div style="text-align: center;">
        <div style="color: #FFFFFF; font-size: 24px;">➔</div>
        <div style="color: #6091F3; font-weight: bold;">Exit</div>
    </div>
</div>
""", unsafe_allow_html=True)

# إضافة زر ستريمليت غير مرئي فوق أيقونة المجموعة للتحكم في الإظهار
if st.button(" ", key="group_btn", help="Click to see names", on_click=toggle_group):
    pass

# تحريك زر ستريمليت الشفاف لمكانه فوق كلمة Group
st.markdown("""
<style>
    div[data-testid="stButton"]:nth-of-type(2) button {
        position: fixed !important;
        bottom: 120px !important;
        left: 5% !important;
        width: 70px !important;
        height: 60px !important;
        background: transparent !important;
        border: none !important;
        color: transparent !important;
        z-index: 1002 !important;
        transform: none !important;
    }
</style>
""", unsafe_allow_html=True)

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