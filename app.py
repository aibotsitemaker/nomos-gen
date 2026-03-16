import streamlit as st
from datetime import date
import google.generativeai as genai
from fpdf import FPDF

# API Ayarları
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# PDF Funksiyası (Stabil versiya)
def create_pdf(muesise, rehber, vezife, ad, doc_type, content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=12) # Standart font
    
    # Azərbaycan hərfləri üçün sadələşdirilmiş format (Unicode xətası verməməsi üçün)
    def clean_text(t):
        return t.replace('ə', 'e').replace('Ə', 'E').replace('ı', 'i').replace('İ', 'I').replace('ş', 's').replace('Ş', 'S').replace('ğ', 'g').replace('Ğ', 'G').replace('ö', 'o').replace('Ö', 'O').replace('ü', 'u').replace('Ü', 'U').replace('ç', 'c').replace('Ç', 'C')

    pdf.cell(0, 10, clean_text(f"{muesise} {rehber}ne"), ln=True, align='R')
    pdf.cell(0, 10, clean_text(f"{vezife} {ad} terefinden"), ln=True, align='R')
    pdf.ln(20)
    pdf.set_font("helvetica", 'B', 16)
    pdf.cell(0, 10, clean_text(doc_type.upper()), ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("helvetica", size=12)
    pdf.multi_cell(0, 10, clean_text(content))
    pdf.ln(20)
    pdf.cell(0, 10, f"Tarix: {date.today()}                                   Imza: ________________", ln=True)
    return pdf.output()

st.set_page_config(page_title="Qanun-AI", layout="wide")

# REKLAM YERLƏRİ (Dizayn)
st.markdown("<style>.ad-box {background:#f1f3f4; border:1px solid #ddd; text-align:center; padding:15px; margin:15px 0; color:#888; border-radius:8px;}</style>", unsafe_allow_html=True)

st.markdown('<div class="ad-box">GOOGLE ADS - YUXARI REKLAM</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.2])

with col1:
    st.header("Sənəd Parametrləri")
    doc_type = st.selectbox("Növ", ["Istifa Erizei", "Mezuniyyet Erizei", "Izahat", "Arayis"])
    ad = st.text_input("Ad Soyad", value="Ali Alizada")
    vezife = st.text_input("Vezife", value="Muhendis")
    muesise = st.text_input("Muessise", value="Aztelekom MMC")
    rehber = st.text_input("Rehber", value="Resad Dostuyev")
    detal = st.text_area("Mezmun (AI bunu rəsmiləşdirəcək)", placeholder="Məsələn: Öz istəyimlə işdən çıxıram...")
    
    st.markdown('<div class="ad-box">GOOGLE ADS - ORTA REKLAM</div>', unsafe_allow_html=True)
    hazirla = st.button("✨ Sənədi Hazırla")

with col2:
    if hazirla:
        ai_text = f"Xahis edirem, {detal} ile elaqedar muracietimi qebul edesiniz."
        try:
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            prompt = f"Azərbaycan dilində rəsmi kargüzarlıq üslubunda {doc_type} mətni yaz. Mövzu: {detal}. Şəxs: {ad}."
            response = model.generate_content(prompt)
            ai_text = response.text
        except:
            st.warning("AI modelinə qoşulmaq alınmadı, standart mətndən istifadə olunur.")

        # Ekranda Azərbaycan hərfləri ilə göstəririk
        st.markdown(f"""
        <div style="background:white; padding:30px; border:1px solid #eee; color:black;">
            <p style="text-align:right;"><b>{muesise} {rehber}nə</b></p>
            <p style="text-align:right;">{vezife} {ad} tərəfindən</p>
            <h3 style="text-align:center;">{doc_type.upper()}</h3>
            <p style="text-align:justify;">{ai_text}</p>
            <p>Tarix: {date.today()} <span style="float:right;">İmza: ________________</span></p>
        </div>
        """, unsafe_allow_html=True)
        
        pdf_output = create_pdf(muesise, rehber, vezife, ad, doc_type, ai_text)
        st.download_button("📥 PDF Yüklə", data=bytes(pdf_output), file_name="sened.pdf", mime="application/pdf")

st.markdown('<div class="ad-box">GOOGLE ADS - AŞAĞI REKLAM</div>', unsafe_allow_html=True)
