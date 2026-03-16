import streamlit as st
import google.generativeai as genai
from datetime import date

# API Key Tənzimləməsi
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key tapılmadı! Lütfən Secrets bölməsini yoxlayın.")

st.set_page_config(page_title="Qanun-AI - Rəsmi Portal", layout="wide")

# CSS (Streamlit-i peşəkar portala çevirmək üçün)
st.markdown("""
    <style>
    header, footer, #MainMenu, .stDeployButton {visibility: hidden;}
    .stApp { background-color: white !important; color: #1a2a40 !important; }
    .header-panel {
        background-color: #1a2a40; padding: 25px; color: white !important;
        text-align: center; border-radius: 0 0 15px 15px; margin: -60px -50px 30px -50px;
    }
    .paper-preview {
        background-color: white !important; padding: 40px; border: 1px solid #e5e7eb;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05); min-height: 550px;
        color: black !important; font-family: 'Times New Roman', serif;
    }
    /* Qaranlıq rejim xətalarını önləmək üçün məcburi rənglər */
    input, textarea, div[data-baseweb="select"] > div {
        background-color: #f8f9fa !important; color: black !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header-panel"><h1>Qanun-AI</h1><p>Süni İntellektli Rəsmi Sənəd Portalı</p></div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown("### **Sənəd Parametrləri**")
    doc_type = st.selectbox("Sənədin növü", ["İstifa Ərizəsi", "Məzuniyyət Ərizəsi", "İzahata", "Təqdimat", "Müqavilə"])
    ad = st.text_input("Tam Adınız", placeholder="Məs: Əli Əlizadə")
    vezife = st.text_input("Vəzifəniz", placeholder="Məs: Mühəndis")
    muesise = st.text_input("Müəssisə", placeholder="Məs: Aztelekom MMC")
    rehber = st.text_input("Rəhbər (Vəzifə və Ad)", placeholder="Məs: Direktor Rəşad Dostuyev")
    detal = st.text_area("Məzmun", placeholder="Məs: Toyumla bağlı 10 günlük məzuniyyət...")
    tarix = st.date_input("Tarix", date.today())
    
    hazirla = st.button("✨ Süni İntellektlə Hazırla")

with col2:
    if hazirla and ad and muesise:
        try:
            model = genai.GenerativeModel('gemini-pro')
            prompt = f"Azərbaycan dilində, rəsmi kargüzarlıq üslubunda {doc_type} üçün əsas mətn hissəsi yaz. Mövzu: {detal}. Şəxs: {ad}, Vəzifə: {vezife}. Yalnız əsas mətni qaytar."
            
            response = model.generate_content(prompt)
            
            st.markdown('<div class="paper-preview">', unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:right;'><b>{muesise} {rehber}nə</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:right;'>{vezife} {ad} tərəfindən</p>", unsafe_allow_html=True)
            st.markdown(f"<br><h3 style='text-align:center;'>{doc_type.upper()}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-indent:50px; text-align:justify;'>{response.text}</p>", unsafe_allow_html=True)
            st.markdown(f"<br><br><p style='display:flex; justify-content:space-between;'><span>Tarix: {tarix}</span><span>İmza: ________________</span></p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Sistem xətası: {e}")
    else:
        st.info("Məlumatları daxil edin və düyməni sıxın.")
