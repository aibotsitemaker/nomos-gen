import streamlit as st
from datetime import date

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
    input, textarea { border: 1px solid #1a2a40 !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header-panel"><h1>Qanun-AI</h1><p>Rəsmi Sənəd və Ərizə Portalı</p></div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown("### **Sənəd Parametrləri**")
    
    # Sənəd növləri
    doc_type = st.selectbox("Sənədin növü", [
        "İstifa Ərizəsi", 
        "Məzuniyyət Ərizəsi", 
        "Ödənişsiz Məzuniyyət Ərizəsi",
        "Ezamiyyət Təqdimatı",
        "İzahata",
        "Arayış (İş yerindən)",
        "Xüsusi (Sərbəst mətn)"
    ])
    
    ad = st.text_input("Sizin Tam Adınız")
    vezife = st.text_input("Vəzifəniz")
    muesise = st.text_input("Müəssisə / Şirkət")
    rehber = st.text_input("Rəhbərin Vəzifəsi və Adı")
    
    # Detallar hissəsi sənəd növünə görə dəyişir
    detal = st.text_area("Sənədin qısa məzmunu / Səbəbi", placeholder="Məs: Ailə vəziyyəti ilə bağlı 2 günlük...")
    
    tarix = st.date_input("Sənəd Tarixi", date.today())
    hazirla = st.button("✨ Rəsmi Sənədi Hazırla")

with col2:
    if hazirla and ad and muesise:
        # Beyin hissəsi (Hələlik mühəndis şablonları ilə, AI bir saniyəlik məsafədədir)
        # Sənəd mətnini hazırlayan məntiq
        if "İstifa" in doc_type:
            content = f"Xahiş edirəm, {detal if detal else 'öz istəyimlə'} tutduğum {vezife} vəzifəsindən azad olunmağım barədə müvafiq göstəriş verəsiniz."
        elif "Məzuniyyət" in doc_type:
            content = f"Xahiş edirəm, {tarix} tarixdən başlayaraq mənə {detal if detal else 'növbəti'} məzuniyyətimin verilməsinə icazə verəsiniz."
        else:
            content = f"Məlumat üçün bildirirəm ki, {detal}. Bununla bağlı müvafiq qərar verməyinizi xahiş edirəm."

        st.markdown('<div class="paper-preview">', unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:right;'><b>{muesise} {rehber}nə</b></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:right;'>{vezife} {ad} tərəfindən</p>", unsafe_allow_html=True)
        st.markdown(f"<br><br><h3 style='text-align:center;'>{doc_type.upper()}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-indent:50px; text-align:justify;'>{content}</p>", unsafe_allow_html=True)
        st.markdown("<br><br><br><br>", unsafe_allow_html=True)
        st.markdown(f"<p style='display:flex; justify-content:space-between;'><span>Tarix: {tarix}</span><span>İmza: ________________</span></p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Əlavə düymələr
        st.download_button("📥 Word formatında yüklə", "Test", file_name="sened.doc")
    else:
        st.markdown('<div class="paper-preview" style="display:flex; align-items:center; justify-content:center; opacity:0.3; text-align:center;"><h3>Məlumatları daxil edin və sənədi yaradın</h3></div>', unsafe_allow_html=True)
