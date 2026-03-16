import streamlit as st
from datetime import date
import google.generativeai as genai
from io import BytesIO
from xhtml2pdf import pisa

# PDF Hazırlama Funksiyası (Azərbaycan şriftləri üçün)
def create_pdf(html_content):
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_content.encode("UTF-8")), result)
    if not pdf.err:
        return result.getvalue()
    return None

st.set_page_config(page_title="Qanun-AI - Rəsmi Portal", layout="wide")

# CSS və Dizayn
st.markdown("""
    <style>
    header, footer, #MainMenu, .stDeployButton {visibility: hidden;}
    .ad-slot {
        background-color: #f8f9fa; border: 1px dashed #1a2a40;
        text-align: center; padding: 15px; margin: 15px 0;
        color: #6c757d; font-size: 14px; border-radius: 5px;
    }
    .paper-preview {
        background-color: white !important; padding: 40px; border: 1px solid #e5e7eb;
        color: black !important; font-family: 'DejaVu Sans', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. YUXARI REKLAM
st.markdown('<div class="ad-slot">GOOGLE ADS - YUXARI BANNER</div>', unsafe_allow_html=True)

st.title("Qanun-AI - Rəsmi Sənəd Portalı")

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown("### **Sənəd Parametrləri**")
    doc_type = st.selectbox("Sənəd növü", ["İstifa Ərizəsi", "Məzuniyyət Ərizəsi", "İzahata", "Arayış"])
    ad = st.text_input("Tam Adınız", value="Əli Əlizadə")
    vezife = st.text_input("Vəzifəniz", value="Mühəndis")
    muesise = st.text_input("Müəssisə", value="Aztelekom MMC")
    rehber = st.text_input("Rəhbər Vəzifəsi və Adı", value="Direktor Rəşad Dostuyev")
    detal = st.text_area("Məzmun (Səbəb)", placeholder="Məs: Şəxsi işlərimlə əlaqədar...")
    tarix = st.date_input("Tarix", date.today())
    
    # 2. ORTA REKLAM
    st.markdown('<div class="ad-slot">GOOGLE ADS - ORTA REKLAM</div>', unsafe_allow_html=True)
    
    hazirla = st.button("✨ Sənədi Hazırla")

with col2:
    if hazirla:
        # Rəsmi Azərbaycan dilində mətn
        ai_content = f"Məlumat üçün bildirirəm ki, {detal} ilə əlaqədar olaraq {doc_type.lower()} ilə bağlı müraciət edirəm. Xahiş edirəm bu barədə müvafiq göstəriş verəsiniz."
        
        # Sənədin HTML formatı (PDF-ə bu formatda köçəcək)
        html_template = f"""
        <div style="font-family: Arial, sans-serif; padding: 20px; color: black;">
            <div style="text-align: right; font-weight: bold;">{muesise} {rehber}nə</div>
            <div style="text-align: right;">{vezife} {ad} tərəfindən</div>
            <br><br>
            <h2 style="text-align: center;">{doc_type.upper()}</h2>
            <br>
            <p style="text-indent: 40px; text-align: justify;">{ai_content}</p>
            <br><br><br>
            <div style="display: flex; justify-content: space-between;">
                <span>Tarix: {tarix}</span>
                <span style="float: right;">İmza: ________________</span>
            </div>
        </div>
        """
        
        # Ekranda göstər
        st.markdown('<div class="paper-preview">', unsafe_allow_html=True)
        st.markdown(html_template, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # PDF Yükləmə
        pdf_file = create_pdf(html_template)
        if pdf_file:
            st.download_button(label="📥 Azərbaycan dilində PDF yüklə", data=pdf_file, file_name=f"{doc_type}.pdf", mime="application/pdf")

# 3. AŞAĞI REKLAM
st.markdown('<div class="ad-slot">GOOGLE ADS - AŞAĞI REKLAM</div>', unsafe_allow_html=True)
