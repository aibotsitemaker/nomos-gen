import streamlit as st
from datetime import date
import google.generativeai as genai
from io import BytesIO
from xhtml2pdf import pisa

# 1. API Ayarları (Secrets-dən oxuyur)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

def create_pdf(html_content):
    result = BytesIO()
    # UTF-8 dəstəyi ilə PDF yaratmaq
    pisa_status = pisa.CreatePDF(BytesIO(html_content.encode("utf-8")), dest=result, encoding='utf-8')
    return result.getvalue() if not pisa_status.err else None

st.set_page_config(page_title="Qanun-AI", layout="wide")

# Reklam yerləri üçün CSS
st.markdown("<style>.ad-box {background:#f1f3f4; border:1px dashed #444; text-align:center; padding:10px; margin:10px 0; color:#666;}</style>", unsafe_allow_html=True)

# YUXARI REKLAM
st.markdown('<div class="ad-box">GOOGLE ADS - TOP BANNER</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.2])

with col1:
    st.header("Sənəd Parametrləri")
    doc_type = st.selectbox("Növ", ["İstifa Ərizəsi", "Məzuniyyət Ərizəsi", "İzahata", "Arayış"])
    ad = st.text_input("Ad", value="Əli Əlizadə")
    vezife = st.text_input("Vəzifə", value="Mühəndis")
    muesise = st.text_input("Müəssisə", value="Aztelekom MMC")
    rehber = st.text_input("Rəhbər", value="Rəşad Dostuyev")
    detal = st.text_area("Məzmun", placeholder="Səbəbi bura yazın...")
    
    # ORTA REKLAM
    st.markdown('<div class="ad-box">GOOGLE ADS - MIDDLE SIDEBAR</div>', unsafe_allow_html=True)
    hazirla = st.button("✨ Sənədi Hazırla")

with col2:
    if hazirla:
        # AI ilə mətn hazırlama (Failover logic)
        ai_text = f"{detal} ilə əlaqədar olaraq {doc_type} təqdim edirəm."
        try:
            model = genai.GenerativeModel('gemini-1.5-flash-latest') # Stabil model adı
            prompt = f"Azərbaycan dilində rəsmi kargüzarlıq üslubunda {doc_type} mətni yaz: {detal}"
            response = model.generate_content(prompt)
            ai_text = response.text
        except:
            st.info("AI qoşulmadı, standart şablona keçildi.")

        # PDF üçün HTML (Dil qaydalarına uyğun)
        html_sened = f"""
        <div style="font-family: 'Arial'; color: black; padding: 20px;">
            <p style="text-align: right;"><b>{muesise} {rehber}nə</b></p>
            <p style="text-align: right;">{vezife} {ad} tərəfindən</p>
            <br><h2 style="text-align: center;">{doc_type.upper()}</h2><br>
            <p style="text-align: justify; text-indent: 40px;">{ai_text}</p>
            <br><br>
            <p>Tarix: {date.today()} <span style="float: right;">İmza: ________________</span></p>
        </div>
        """
        st.markdown(html_sened, unsafe_allow_html=True)
        
        pdf_bytes = create_pdf(html_sened)
        if pdf_bytes:
            st.download_button("📥 PDF Yüklə", data=pdf_bytes, file_name="sened.pdf", mime="application/pdf")

# AŞAĞI REKLAM
st.markdown('<div class="ad-box">GOOGLE ADS - BOTTOM FOOTER</div>', unsafe_allow_html=True)
