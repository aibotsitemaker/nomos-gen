import streamlit as st
from datetime import date
import google.generativeai as genai

# Səhifə Ayarları
st.set_page_config(page_title="Qanun-AI - Rəsmi Portal", layout="wide")

# CSS - Vizual xətaları aradan qaldırmaq üçün
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

st.markdown('<div class="header-panel"><h1>Qanun-AI</h1><p>Rəsmi Sənəd Hazırlama Portalı</p></div>', unsafe_allow_html=True)

# Şablon Bazası (AI işləməsə belə sayt sənəd hazırlayacaq)
templates = {
    "İstifa Ərizəsi": "Xahiş edirəm, tutduğum {vezife} vəzifəsindən öz istəyimlə azad olunmağım barədə müvafiq göstəriş verəsiniz.",
    "Məzuniyyət Ərizəsi": "Xahiş edirəm, {tarix} tarixdən etibarən mənə növbəti əmək məzuniyyətinin verilməsi barədə sərəncam verəsiniz.",
    "İzahata": "Məlumat üçün bildirirəm ki, {detal} səbəbindən iş prosesində yaranmış gecikməyə görə izahatımı təqdim edirəm.",
    "Arayış": "Bu arayış həqiqətən də təsdiq edir ki, {ad} {muesise} müəssisəsində {vezife} vəzifəsində çalışır."
}

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown("### **Sənəd Parametrləri**")
    doc_type = st.selectbox("Sənədin növü", list(templates.keys()))
    ad = st.text_input("Tam Adınız", value="Əli Əlizadə")
    vezife = st.text_input("Vəzifəniz", value="Mühəndis")
    muesise = st.text_input("Müəssisə", value="Aztelekom MMC")
    rehber = st.text_input("Rəhbər (Vəzifə və Ad)", value="Direktor Rəşad Dostuyev")
    detal = st.text_area("Məzmun / Səbəb", placeholder="Məs: Ailə vəziyyəti ilə bağlı...")
    tarix = st.date_input("Tarix", date.today())
    hazirla = st.button("✨ Sənədi Hazırla")

with col2:
    if hazirla:
        # Əvvəlcə şablonu hazırlayaq
        final_text = templates[doc_type].format(ad=ad, vezife=vezife, muesise=muesise, tarix=tarix, detal=detal)
        
        # Əgər API Key varsa, AI ilə zənginləşdirməyə çalışaq
        if "GOOGLE_API_KEY" in st.secrets:
            try:
                genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"Azərbaycan dilində rəsmi kargüzarlıq dildində bu mətni daha peşəkar et: {final_text}"
                response = model.generate_content(prompt)
                final_text = response.text
                st.toast("AI tərəfindən təkmilləşdirildi!")
            except:
                st.toast("Şablon rejimi aktivdir (AI qoşulmadı).")

        # Sənədi Göstər
        st.markdown('<div class="paper-preview">', unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:right;'><b>{muesise} {rehber}nə</b></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:right;'>{vezife} {ad} tərəfindən</p>", unsafe_allow_html=True)
        st.markdown(f"<br><h3 style='text-align:center;'>{doc_type.upper()}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-indent:50px; text-align:justify;'>{final_text}</p>", unsafe_allow_html=True)
        st.markdown(f"<br><br><p style='display:flex; justify-content:space-between;'><span>Tarix: {tarix}</span><span>İmza: ________________</span></p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("Məlumatları daxil edin və düyməni sıxın.")
