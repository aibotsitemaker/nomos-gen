import streamlit as st
from datetime import date

# Səhifə tənzimləmələri
st.set_page_config(page_title="Qanun-AI - Rəsmi Portal", layout="wide")

# Məcburi Açıq Rejim və Rəsmi Dizayn CSS-i
st.markdown("""
    <style>
    /* Bütün səhifəni ağ və yazıları qara edirik */
    .stApp {
        background-color: white !important;
        color: #1a2a40 !important;
    }
    /* Üst göy panel */
    .header-panel {
        background-color: #1a2a40;
        padding: 30px;
        color: white !important;
        text-align: center;
        border-radius: 0 0 15px 15px;
        margin: -60px -50px 30px -50px;
    }
    .header-panel h1, .header-panel p {
        color: white !important;
    }
    /* Giriş xanalarının başlıqları (label) */
    .stMarkdown h3, .stMarkdown h5, label {
        color: #1a2a40 !important;
        font-weight: bold !important;
    }
    /* İnput xanalarının içini ağ, çərçivəsini tünd edirik */
    input, div[data-baseweb="select"] > div {
        background-color: white !important;
        color: black !important;
        border: 1px solid #1a2a40 !important;
    }
    /* "Sənədi Hazırla" düyməsi */
    div.stButton > button:first-child {
        background-color: #1a2a40 !important;
        color: white !important;
        border-radius: 8px;
        padding: 15px;
        font-weight: bold;
        width: 100%;
        border: none;
    }
    /* Kağız (Preview) hissəsi */
    .paper-preview {
        background-color: white !important;
        padding: 40px;
        border: 2px solid #e5e7eb;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        min-height: 500px;
        font-family: 'Times New Roman', serif;
        color: black !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Üst Header
st.markdown('<div class="header-panel"><h1>Qanun-AI</h1><p>Azərbaycan Respublikası Hüquq Köməkçisi</p></div>', unsafe_allow_html=True)

# Sol və Sağ sütunlar
col1, col2 = st.columns([1, 1.2], gap="large")

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
    
    st.write("") # Boşluq
    hazirla = st.button("✨ Sənədi Hazırla")

with col2:
    if hazirla:
        if ad and muesise:
            st.markdown('<div class="paper-preview">', unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:right; color:black;'><b>{muesise} {rehber_vezife}nə</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:right; color:black;'>{vezife} {ad} tərəfindən</p>", unsafe_allow_html=True)
            st.markdown("<br><br><h3 style='text-align:center; color:black;'>Ə R İ Z Ə</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-indent:50px; text-align:justify; color:black;'>Xahiş edirəm, tutduğum {vezife} vəzifəsindən öz istəyimlə azad olunmağım barədə müvafiq göstəriş verəsiniz.</p>", unsafe_allow_html=True)
            st.markdown("<br><br><br><br>", unsafe_allow_html=True)
            st.markdown(f"<p style='display:flex; justify-content:space-between; color:black;'><span>Tarix: {tarix}</span><span>İmza: ________________</span></p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error("Zəhmət olmasa, adınızı və müəssisəni qeyd edin.")
    else:
        st.markdown('<div class="paper-preview" style="display:flex; align-items:center; justify-content:center; opacity:0.5;"><h3>Sənəd Önizləməsi</h3></div>', unsafe_allow_html=True)
