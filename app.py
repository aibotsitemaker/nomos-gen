import streamlit as st
from datetime import date

# Səhifə tənzimləmələri
st.set_page_config(page_title="Qanun-AI - Rəsmi Portal", layout="wide")

# Şəkildəki dizayna uyğun CSS
st.markdown("""
    <style>
    /* Ümumi fon */
    .stApp {
        background-color: #f4f7f9;
    }
    /* Üst göy panel */
    .header-panel {
        background-color: #1a2a40;
        padding: 20px;
        color: white;
        text-align: center;
        border-radius: 0 0 15px 15px;
        margin: -50px -50px 30px -50px;
    }
    /* Giriş xanaları və Form */
    .stTextInput input, .stDateInput input {
        border-radius: 8px !important;
        border: 1px solid #d1d5db !important;
    }
    /* "Sənədi Hazırla" düyməsi */
    div.stButton > button:first-child {
        background-color: #1a2a40;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: bold;
        width: 100%;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    /* Kağız (Preview) hissəsi */
    .paper-preview {
        background-color: white;
        padding: 40px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
        min-height: 500px;
        font-family: 'Times New Roman', serif;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

# Üst Header
st.markdown('<div class="header-panel"><h1>Qanun-AI</h1><p>Azərbaycan Respublikası Hüquq Köməkçisi</p></div>', unsafe_allow_html=True)

# Sol və Sağ sütunlar (Şəkildəki kimi 1:1 nisbətində)
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### **İstifa Ərizəsi Generatoru**")
    
    st.markdown("##### **1. Şəxsi Məlumatlar**")
    ad = st.text_input("Tam Adınız", placeholder="Məs: Əli Əlizadə")
    vezife = st.text_input("Vəzifəniz", placeholder="Məs: Baş Mütəxəssis")
    
    st.markdown("##### **2. İşəgötürən Məlumatları**")
    muesise = st.text_input("Müəssisə Adı", placeholder="Məs: Aztelekom MMC")
    rehber_vezife = st.text_input("Rəhbər Vəzifəsi", placeholder="Məs: Direktor")
    
    st.markdown("##### **3. Ərizə Tarixi**")
    tarix = st.date_input("Tarix seçin", date.today())
    
    hazirla = st.button("✨ Sənədi Hazırla")

with col2:
    # Sağ tərəfdəki kağız önizləməsi
    if hazirla:
        st.markdown('<div class="paper-preview">', unsafe_allow_html=True)
        st.write(f"<p style='text-align:right;'><b>{muesise} {rehber_vezife}nə</b></p>", unsafe_allow_html=True)
        st.write(f"<p style='text-align:right;'>{vezife} {ad} tərəfindən</p>", unsafe_allow_html=True)
        st.markdown("<br><br><h3 style='text-align:center;'>Ə R İ Z Ə</h3>", unsafe_allow_html=True)
        st.write(f"<p style='text-indent:50px; text-align:justify;'>Xahiş edirəm, tutduğum {vezife} vəzifəsindən öz istəyimlə azad olunmağım barədə müvafiq göstəriş verəsiniz.</p>", unsafe_allow_html=True)
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.write(f"<p style='display:flex; justify-content:space-between;'><span>Tarix: {tarix}</span><span>İmza: ________________</span></p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Alt düymələr
        c1, c2 = st.columns(2)
        with c1: st.button("📄 Word kimi Yüklə")
        with c2: st.button("🖨️ Çap et")
    else:
        # Boş halda görünən yer
        st.info("Məlumatları doldurub 'Sənədi Hazırla' düyməsini sıxdıqda, rəsmi sənəd burada görünəcək.")
        st.markdown('<div style="opacity: 0.1; text-align: center; padding-top: 100px;"><h1>📄</h1><p>Önizləmə Sahəsi</p></div>', unsafe_allow_html=True)
