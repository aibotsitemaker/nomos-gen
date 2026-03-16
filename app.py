import streamlit as st
import google.generativeai as genai
from datetime import date

# 1. Konfiqurasiya və API Yoxlanışı
st.set_page_config(page_title="Qanun-AI - Rəsmi Portal", layout="wide")

if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("XƏTA: API Key 'Secrets' bölməsində tapılmadı!")

# 2. Dizayn (Səliqəli və Rəsmi)
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
    input, textarea { background-color: #f8f9fa !important; color: black !important; border: 1px solid #d1d5db !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header-panel"><h1>Qanun-AI</h1><p>Süni İntellektli Rəsmi Sənəd Portalı</p></div>', unsafe_allow_html=True)

# 3. İnterfeys
col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown("### **Sənəd Parametrləri**")
    doc_type = st.selectbox("Sənədin növü", ["İstifa Ərizəsi", "Məzuniyyət Ərizəsi", "İzahata", "Təqdimat", "Müqavilə", "Arayış"])
    ad = st.text_input("Tam Adınız", value="Əli Əlizadə")
    vezife = st.text_input("Vəzifəniz", value="Mühəndis")
    muesise = st.text_input("Müəssisə", value="Aztelekom MMC")
    rehber = st.text_input("Rəhbər (Vəzifə və Ad)", value="Direktor Rəşad Dostuyev")
    detal = st.text_area("Məzmun", placeholder="Məs: Ailə vəziyyəti ilə bağlı 5 günlük ödənişsiz məzuniyyət...")
    tarix = st.date_input("Tarix", date.today())
    hazirla = st.button("✨ Süni İntellektlə Hazırla")

with col2:
    if hazirla:
        if not detal:
            st.warning("Zəhmət olmasa məzmun hissəsini doldurun.")
        else:
            with st.spinner("AI sənədi tərtib edir..."):
                prompt = f"Azərbaycan dilində, rəsmi kargüzarlıq üslubunda {doc_type} üçün əsas mətn hissəsi yaz. Mövzu: {detal}. Şəxs: {ad}, Vəzifə: {vezife}. Yalnız mətni qaytar."
                
                # Model xətalarını keçmək üçün ardıcıl yoxlama (Failover logic)
                success = False
                for model_name in ['gemini-1.5-flash', 'gemini-pro', 'models/gemini-1.5-flash-latest']:
                    try:
                        model = genai.GenerativeModel(model_name)
                        response = model.generate_content(prompt)
                        ai_text = response.text
                        success = True
                        break 
                    except:
                        continue
                
                if success:
                    st.markdown('<div class="paper-preview">', unsafe_allow_html=True)
                    st.markdown(f"<p style='text-align:right;'><b>{muesise} {rehber}nə</b></p>", unsafe_allow_html=True)
                    st.markdown(f"<p style='text-align:right;'>{vezife} {ad} tərəfindən</p>", unsafe_allow_html=True)
                    st.markdown(f"<br><h3 style='text-align:center;'>{doc_type.upper()}</h3>", unsafe_allow_html=True)
                    st.markdown(f"<p style='text-indent:50px; text-align:justify;'>{ai_text}</p>", unsafe_allow_html=True)
                    st.markdown(f"<br><br><p style='display:flex; justify-content:space-between;'><span>Tarix: {tarix}</span><span>İmza: ________________</span></p>", unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.error("AI Modelləri ilə əlaqə qurula bilmədi. API Key-in statusunu Google AI Studio-da yoxlayın.")
    else:
        st.info("Məlumatları daxil edin və 'Hazırla' düyməsini sıxın.")
