import streamlit as st
import os
import base64
from importlib import import_module

st.set_page_config(page_title="Football All history", page_icon="⚽", layout="wide")

# دالة لتحويل الصورة المحلية إلى Base64 لضمان عملها كخلفية بدون مشاكل روابط
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

local_bg = get_base64_image("bg.jpg")

if local_bg:
    bg_css = f"data:image/jpg;base64,{local_bg}"
else:
    # خلفية استاديوم جرافيك نيون افتراضية تناسب EA FC 25
    bg_css = "https://images.unsplash.com/photo-1518091043644-c1d4457512c6?q=80&w=1920&auto=format&fit=crop"

# CSS لتصميم الجيمينج والواجهة الزجاجية
st.markdown(f"""
    <style>
    /* 1. خلفية الصفحة بالكامل مع طبقة تعتيم نيون شفافة */
    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(rgba(7, 12, 22, 0.78), rgba(7, 12, 22, 0.88)), 
                    url('{bg_css}') no-repeat center center fixed !important;
        background-size: cover !important;
    }}

    /* 2. إزالة أي خلفيات أو بلوكات مفصولة تجعل الشكل غير موحد */
    [data-testid="stHeader"], .stAppHeader, .main, [data-testid="stMain"], .block-container {{
        background: transparent !important;
    }}
    
    .block-container {{
        padding-top: 2rem !important;
        max-width: 1050px !important;
    }}

    /* 3. الشريط الجانبي بتصميم زجاجي شفاف (Glassmorphism) */
    [data-testid="stSidebar"] {{
        background: rgba(10, 16, 28, 0.82) !important;
        backdrop-filter: blur(16px) !important;
        border-right: 1px solid rgba(0, 255, 135, 0.2) !important;
    }}
    [data-testid="stSidebar"] * {{
        color: #ffffff !important;
    }}

    /* 4. كارت العنوان الرئيسي بلمسات FC 25 النيون */
    .hero-card {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(14px);
        border: 1px solid rgba(0, 255, 135, 0.3);
        border-radius: 20px;
        padding: 28px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), 0 0 20px rgba(0, 255, 135, 0.15);
    }}
    
    .hero-title {{
        color: #00ff87 !important;
        font-size: 3.2rem !important;
        font-weight: 900 !important;
        letter-spacing: 1px;
        margin-bottom: 6px !important;
        text-shadow: 0 0 25px rgba(0, 255, 135, 0.6);
    }}
    
    .hero-subtitle {{
        color: #e2e8f0 !important;
        font-size: 1.2rem !important;
        font-weight: 500;
        margin-bottom: 0px !important;
    }}

    /* 5. صندوق الإدخال وتأثير الـ Hover الاحترافي */
    .stTextInput > div > div > input {{
        background-color: rgba(255, 255, 255, 0.95) !important;
        color: #080f1e !important;
        border-radius: 14px !important;
        border: 2px solid #00ff87 !important;
        padding: 16px 20px !important;
        font-size: 17px !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4) !important;
        transition: all 0.3s ease-in-out !important;
    }}
    .stTextInput > div > div > input:hover {{
        border-color: #00d2ff !important;
        box-shadow: 0 0 25px rgba(0, 255, 135, 0.8) !important;
        background-color: #ffffff !important;
        transform: translateY(-2px);
    }}
    .stTextInput > div > div > input:focus {{
        border-color: #00ff87 !important;
        box-shadow: 0 0 30px rgba(0, 255, 135, 0.9) !important;
        background-color: #ffffff !important;
    }}

    /* 6. نصوص وعناوين الصفحة */
    h1, h2, h3, p, label {{
        color: #ffffff !important;
    }}

    /* 7. زر التحديث في الشريط الجانبي */
    .stButton button {{
        background: linear-gradient(135deg, #00ff87 0%, #00d2ff 100%) !important;
        color: #080f1e !important;
        font-weight: 800 !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 12px !important;
        transition: all 0.3s ease !important;
        width: 100%;
        text-transform: uppercase;
    }}
    .stButton button:hover {{
        box-shadow: 0 0 20px rgba(0, 255, 135, 0.8) !important;
        transform: translateY(-2px);
    }}
    </style>
""", unsafe_allow_html=True)

# الشريط الجانبي لمعلومات المطور
with st.sidebar:
    st.markdown("<div style='text-align: center; margin-top: 10px;'>", unsafe_allow_html=True)
    if os.path.exists("profile.png"):
        st.image("profile.png", width=120)
    else:
        st.markdown("<h1 style='font-size: 60px; margin:0;'>⚽</h1>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='margin-bottom: 0px; font-size: 22px;'>Moustafa Ghanem</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00ff87 !important; font-weight: 600; font-size: 13px;'>Senior AI & RAG Developer</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.divider()
    
    if st.button("🔄 تحديث قاعدة البيانات"):
        with st.spinner("جاري معالجة الملفات..."):
            try:
                create_store = import_module("05_create_chroma_store")
                create_store.create_vector_store()
                st.success("تم التحديث بنجاح!")
            except Exception as e:
                st.error(f"خطأ: {e}")

# كارت العنوان
st.markdown("""
    <div class="hero-card">
        <div class="hero-title">⚽ Football All history</div>
        <div class="hero-subtitle"> البوابة الذكية الشاملة لتاريخ وأرشيف كرة القدم العالمية حتي 2023</div>
    </div>
""", unsafe_allow_html=True)

def get_text_direction(text):
    if not text:
        return "ltr"
    arabic_range = range(0x0600, 0x06FF)
    for char in text:
        if ord(char) in arabic_range:
            return "rtl"
    return "ltr"

user_query = st.text_input("اطرح سؤالك في كرة القدم (عربي / English):", placeholder="مثال: مين هداف كأس العالم 2022؟")

if user_query:
    dir_lang = get_text_direction(user_query)
    
    with st.spinner("جاري البحث في الأرشيف وتحليل البيانات..."):
        try:
            retriever = import_module("06_retrieve_context")
            prompter = import_module("07_prompting")
            
            contexts = retriever.retrieve_relevant_context(user_query, n_results=3)
            answer = prompter.generate_rag_answer(user_query, contexts)
            
            st.markdown("### ⚽ الإجابة:")
            st.markdown(
                f'''<div style="
                    direction: {dir_lang}; 
                    text-align: {"right" if dir_lang=="rtl" else "left"}; 
                    background: rgba(10, 16, 28, 0.85); 
                    backdrop-filter: blur(14px);
                    padding: 24px; 
                    border-radius: 16px; 
                    border: 1px solid rgba(0, 255, 135, 0.4); 
                    box-shadow: 0 10px 30px rgba(0,0,0,0.6);
                    font-size: 17px; 
                    line-height: 1.7;
                    color: #ffffff;">
                    {answer}
                </div>''', 
                unsafe_allow_html=True
            )
            
            st.write("")
            with st.expander("🔍 عرض المصادر والسياق المسترجع (Context)"):
                for idx, c in enumerate(contexts):
                    st.markdown(f"**المصدر:** `{c['source']}`")
                    st.text(c['content'])
                    st.divider()
        except Exception as e:
            st.error(f"حدث خطأ أثناء المعالجة: {e}")
