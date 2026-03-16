import streamlit as st

# Saytın başlığı və dizayn tənzimləmələri
st.set_page_config(page_title="Nomos - Sənəd Generatoru", page_icon="⚖️")

# Gələcəkdə dizayner dostunun loqosunu bura qoyacağıq
st.title("⚖️ Nomos")
st.subheader("Süni İntellektli Sənəd Generatoru")

st.info("Məlumatları daxil edin, mən sizin üçün rəsmi ərizəni hazırlayım.")

# İstifadəçidən alınan məlumatlar
with st.form("erize_form"):
    ad_soyad = st.text_input("Tam Adınız və Soyadınız")
    vezife = st.text_input("Vəzifəniz")
    shirket = st.text_input("Müəssisənin Adı")
    rehber = st.text_input("Rəhbərin Vəzifəsi və Adı (məs: Direktor cənab X)")
    sebeb = st.text_area("İstifa səbəbi (qısa)")
    
    submit = st.form_submit_button("Sənədi Hazırla")

if submit:
    if ad_soyad and shirket:
        # Bu hissə hələlik sadə prototipdir, AI-ı bura birləşdirəcəyik
        st.success("Sənəd hazırdır!")
        st.markdown(f"""
        ---
        **KİMƏ:** {rehber}  
        **KİMDƏN:** {vezife} {ad_soyad}  
        
        **Ə R İ Z Ə** Xahiş edirəm, {sebeb} səbəbi ilə məni {shirket} müəssisəsindəki vəzifəmdən azad edəsiniz.  
        
        **İmza:** ____________  
        **Tarix:** 16.03.2026
        ---
        """)
        st.button("PDF kimi yüklə (Tezliklə)")
    else:
        st.error("Zəhmət olmasa vacib xanaları doldurun!")
