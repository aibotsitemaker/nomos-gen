import streamlit as st
from datetime import date
import google.generativeai as genai
from fpdf import FPDF

# Azərbaycan hərflərini PDF-in başa düşəcəyi formata salmaq üçün funksiya
def fix_az_chars(text):
    rep = {
        "ə": "e", "ə": "e", "sh": "sh", "s": "s", "i": "i", "g": "g", "o": "o", "u": "u", "c": "c",
        "Ə": "E", "Ş": "S", "İ": "I", "Ğ": "G", "Ö": "O", "Ü": "U", "Ç": "C"
    }
    for search, replace in rep.items():
        text = text.replace(search, replace)
    return text

def create_pdf(muesise, rehber, vezife, ad, doc_type, content, tarix):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Məlumatları təmizləyirik (Unicode xətası almamamaq üçün)
    muesise = fix_az_chars(muesise)
    rehber = fix_az_chars(rehber)
    vezife = fix_az_chars(vezife)
    ad = fix_az_chars(ad)
    content = fix_az_chars(content)
    
    # Sağ tərəf
    pdf.cell(0, 10, f"{muesise} {rehber}ne", ln=True, align='R')
    pdf.cell(0, 10, f"{vezife} {ad} terefinden", ln=True, align='R')
    
    # Başlıq
    pdf.ln(20)
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, doc_type.upper(), ln=True, align='C')
    
    # Mətn
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    
    # Sonluq
    pdf.ln(30)
    pdf.cell(100, 10, f"Tarix: {tarix}", align='L')
    pdf.cell(0, 10, "Imza: ________________", align='R')
    
    return pdf.output(dest='S').encode('latin-1', 'ignore')

st.set_page_config(page_title="Qanun-AI - Rəsmi Portal", layout="wide")

# Reklam və Dizayn Stilləri
st.markdown("""
    <style>
    header, footer, #MainMenu, .stDeployButton {visibility: hidden;}
    .ad-slot {
        background-color: #f1f3f4; border: 1px solid #d1d5db;
        text-align: center; padding: 15px; margin: 15px 0;
        color: #5f6368; font-weight: bold; border-radius: 8px;
    }
    .paper-preview {
        background-color: white !important; padding: 40px; border: 1px solid #e5e7eb;
        color: black !important; font-family: 'Times New Roman', serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. YUXARI REKLAM
st.markdown('<div class="ad-slot">GOOGLE ADS - TOP BANNER (Horizontal)</div>', unsafe_allow_html=True)

st.title("Qanun-AI - Sənəd Portalı")

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown("### **Sənəd Məlumatları**")
    doc_type = st.selectbox("Sənəd növü", ["İstifa Ərizəsi", "Məzuniyyət Ərizəsi", "İzahata", "Arayış"])
    ad = st.text_input("Adınız", value="Əli Əlizadə")
    vezife = st.text_input("Vəzifəniz", value="Mühəndis")
    muesise = st.text_input("Müəssisə", value="Aztelekom MMC")
    rehber = st.text_input("Rəhbər Vəzifəsi", value="Direktor")
    detal = st.text_area("Məzmun", placeholder="Qısa səbəb yazın...")
    tarix = st.date_input("Tarix", date.today())
    
    # 2. ORTA REKLAM (Sidebar/İnput altı)
    st.markdown('<div class="ad-slot">GOOGLE ADS - MIDDLE SQUARE</div>', unsafe_allow_html=True)
    
    hazirla = st.button("✨ Hazırla və PDF-ə Çevir")

with col2:
    if hazirla:
        content = f"Xahis edirem, {detal} ile elaqedar {doc_type} qebul edesiniz."
        
        st.markdown('<div class="paper-preview">', unsafe_allow_html=True)
        st.write(f"<p style='text-align:right;'><b>{muesise} {rehber}nə</b></p>", unsafe_allow_html=True)
        st.write(f"<p style='text-align:right;'>{vezife} {ad} tərəfindən</p>", unsafe_allow_html=True)
        st.write(f"<h3 style='text-align:center;'>{doc_type.upper()}</h3>", unsafe_allow_html=True)
        st.write(f"<p style='text-indent:50px;'>{content}</p>", unsafe_allow_html=True)
        st.write(f"<br><p>Tarix: {tarix} <span style='float:right;'>İmza: ________________</span></p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        try:
            pdf_data = create_pdf(muesise, rehber, vezife, ad, doc_type, content, tarix)
            st.download_button("📥 PDF-i Yüklə", data=pdf_data, file_name="sened.pdf", mime="application/pdf")
        except Exception as e:
            st.error(f"PDF xətası: {e}")

# 3. AŞAĞI REKLAM
st.markdown('<div class="ad-slot">GOOGLE ADS - BOTTOM FOOTER (Long)</div>', unsafe_allow_html=True)
