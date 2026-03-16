import streamlit as st
import google.generativeai as genai
from datetime import date

# Streamlit Secrets-dən API Key-i götürürük
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("API Key tapılmadı. Secrets bölməsini yoxlayın!")

# Səhifə tənzimləmələri
st.set_page_config(page_title="Qanun-AI - Universal Generator", layout="wide")

# CSS (Gizli Streamlit elementləri və Rəsmi Stil)
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
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header-panel"><h1>Qanun-AI</h1><p>Süni İntellektli Rəsmi Sənəd Portalı</p></div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown("### **Sənəd Parametrləri**")
    
    doc_type = st.selectbox("Sənədin növü", [
        "İstifa Ərizəsi", "Məzuniyyət Ərizəsi", "Ödənişsiz Məzuniyyət Ərizəsi",
        "İzahata", "Təqdimat", "Arayış", "Müqavilə", "Xüsusi Sənəd"
    ])
    
    ad = st.text_input("Sizin Tam Adınız")
    vezife = st.text_input("Vəzifəniz")
    muesise = st.text_input("Müəssisə / Şirkət")
    rehber = st.text_input("Rəhbərin Vəzifəsi və Adı")
    detal = st.text_area("Sənədin qısa məzmunu (AI bunu rəsmiləşdirəcək)", placeholder="Məs: Ailə vəziyyəti ilə bağlı 3 günlük icazə...")
    tarix = st.date_input("Sənəd Tarixi", date.today())
    
    hazirla = st.button("✨ Süni İntellektlə Hazırla")

with col2:
    if hazirla and ad and muesise:
        with st.spinner("AI sənədi hüquqi normalara uyğunlaşdırır..."):
            # Gemini AI-a göndərilən təlimat (Prompt Engineering)
            prompt = f"""
            Sən peşəkar hüquqşünas və kargüzarlıq ekspertisən. 
            Aşağıdakı məlumatlara əsasən Azərbaycan Respublikasının qanunvericiliyinə uyğun rəsmi {doc_type} mətni hazırla.
            Mətn rəsmi, ciddi və hüquqi terminlərlə zəngin olmalıdır.
            
            İstifadəçi məlumatları:
            Ad: {ad}
            Vəzifə: {vezife}
            Müəssisə: {muesise}
            Rəhbər: {rehber}
            Məzmun: {detal}
            
            Yalnız sənədin əsas mətn hissəsini qaytar.
            """
            
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(prompt)
                ai_content = response.text
                
                st.markdown('<div class="paper-preview">', unsafe_allow_html=True)
                st.markdown(f"<p style='text-align:right;'><b>{muesise} {rehber}nə</b></p>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-align:right;'>{vezife} {ad} tərəfindən</p>", unsafe_allow_html=True)
                st.markdown(f"<br><br><h3 style='text-align:center;'>{doc_type.upper()}</h3>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-indent:50px; text-align:justify;'>{ai_content}</p>", unsafe_allow_html=True)
                st.markdown("<br><br><br>", unsafe_allow_html=True)
                st.markdown(f"<p style='display:flex; justify-content:space-between;'><span>Tarix: {tarix}</span><span>İmza: ________________</span></p>", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Xəta baş verdi: {e}")
    else:
        st.info("Məlumatları doldurun və AI-ın gücünü görün.")
