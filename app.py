import streamlit as st
from datetime import date
import google.generativeai as genai
from fpdf import FPDF

# PDF Hazırlama Funksiyası
def create_pdf(muesise, rehber, vezife, ad, doc_type, content, tarix):
    pdf = FPDF()
    pdf.add_page()
    # Azərbaycan şriftləri üçün standart font (Unicode problemi olmaması üçün)
    pdf.set_font("Arial", size=12)
    
    # Sağ tərəf (Başlıq hissəsi)
    pdf.cell(0, 10, f"{muesise} {rehber}ne", ln=True, align='R')
    pdf.cell(0, 10, f"{vezife} {ad} terefinden", ln=True, align='R')
    
    # Orta (Sənəd adı)
    pdf.ln(20)
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, doc_type.upper(), ln=True, align='C')
    
    # Mətn hissəsi
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    
    # Sonluq (Tarix və İmza)
    pdf.ln(30)
    pdf.cell(100, 10, f"Tarix: {tarix}", align='L')
    pdf.cell(0, 10, "Imza: ________________", align='R')
    
    return pdf.output(dest='S').encode('latin-1')

st.set_page_config(page_title="Qanun-AI - Rəsmi Portal", layout="wide")

# CSS və Reklam Stilləri
st.markdown("""
    <style>
    header, footer, #MainMenu, .stDeployButton {visibility: hidden;}
    .ad-slot {
        background-color: #f0f2f6;
        border: 1px dashed #1a2a40;
        text-align: center;
        padding: 10px;
        margin: 10px 0;
        color: #666;
        font-size: 12px;
    }
    .paper-preview {
        background-color: white !important;
        padding: 40px;
        border: 1px solid #e5e7eb;
        color: black !important;
        font-family: 'Times New Roman', serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. YUXARI REKLAM YERİ
st.markdown('<div class="ad-slot">GOOGLE ADS - TOP BANNER</div>', unsafe_allow_html=True)

st.title("Qanun-AI - Universal Sənəd Portalı")

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown("### **Sənəd Parametrləri**")
    doc_type = st.selectbox("Sənədin növü", ["İstifa Ərizəsi", "Məzuniyyət Ərizəsi", "İzahata", "Arayış"])
    ad = st.text_input("Tam Adınız", value="Əli Əlizadə")
    vezife = st.text_input("Vəzifəniz", value="Mühəndis")
    muesise = st.text_input("Müəssisə", value="Aztelekom MMC")
    rehber = st.text_input("Rəhbərin Vəzifəsi", value="Direktor")
    detal = st.text_area("Məzmun", placeholder="Qısa məlumat yazın...")
    tarix = st.date_input("Tarix", date.today())
    
    # 2. ORTA REKLAM YERİ
    st.markdown('<div class="ad-slot">GOOGLE ADS - MIDDLE SIDEBAR</div>', unsafe_allow_html=True)
    
    hazirla = st.button("✨ Sənədi Hazırla")

with col2:
    if hazirla:
        # Şablon mətni (AI qoşulmasa da işləsin)
        ai_content = f"Xahis edirem, {detal} sebebinden {doc_type} qebul edesiniz."
        
        # Sənədin ekranda görünüşü
        st.markdown('<div class="paper-preview">', unsafe_allow_html=True)
        st.write(f"<p style='text-align:right;'><b>{muesise} {rehber}ne</b></p>", unsafe_allow_html=True)
        st.write(f"<p style='text-align:right;'>{vezife} {ad} terefinden</p>", unsafe_allow_html=True)
        st.write(f"<h3 style='text-align:center;'>{doc_type.upper()}</h3>", unsafe_allow_html=True)
        st.write(f"<p style='text-indent:50px;'>{ai_content}</p>", unsafe_allow_html=True)
        st.write(f"<br><p>Tarix: {tarix} <span style='float:right;'>Imza: ________________</span></p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # PDF Yükləmə Düyməsi
        pdf_data = create_pdf(muesise, rehber, vezife, ad, doc_type, ai_content, tarix)
        st.download_button(label="📥 PDF kimi yüklə", data=pdf_data, file_name=f"{doc_type}.pdf", mime="application/pdf")

# 3. AŞAĞI REKLAM YERİ
st.markdown('<div class="ad-slot">GOOGLE ADS - BOTTOM FOOTER</div>', unsafe_allow_html=True)
