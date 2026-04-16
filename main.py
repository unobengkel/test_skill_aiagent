import os
import requests
import streamlit as st
from openai import OpenAI

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Marketing AI Agent", page_icon="🚀")
st.title("🚀 Marketing AI Agent (DeepSeek)")
st.caption("Custom Agent menggunakan Framework Marketing Corey Haines")

# --- FUNGSI MENGAMBIL SKILL DARI GITHUB ---
@st.cache_data
def get_marketing_skill(category):
    # Mengarah ke folder /skills/ sesuai struktur terbaru
    raw_url = f"https://raw.githubusercontent.com/coreyhaines31/marketingskills/main/skills/{category}/SKILL.md"
    try:
        response = requests.get(raw_url)
        if response.status_code == 200:
            return response.text
        return "You are a professional marketing expert."
    except:
        return "You are a professional marketing expert."

# --- SIDEBAR: PENGATURAN ---
with st.sidebar:
    st.header("Konfigurasi")
    api_key = st.text_input("DeepSeek API Key", type="password", value=os.environ.get('DEEPSEEK_API_KEY', ''))
    
    # DAFTAR KATEGORI LENGKAP DARI SCREENSHOT ANDA
    all_categories = [
        "ab-test-setup", "ad-creative", "ai-seo", "analytics-tracking", 
        "aso-audit", "churn-prevention", "cold-email", "community-marketing",
        "competitor-alternatives", "content-strategy", "copy-editing", 
        "copywriting", "customer-research", "email-sequence", "form-cro",
        "free-tool-strategy", "launch-strategy", "lead-magnets", 
        "marketing-ideas", "marketing-psychology", "onboarding-cro", 
        "page-cro", "paid-ads", "paywall-upgrade-cro", "popup-cro", 
        "pricing-strategy", "product-marketing-context", "programmatic-seo", 
        "referral-program", "revops", "sales-enablement", "schema-markup", 
        "seo-audit", "signup-flow-cro", "site-architecture", "social-content"
    ]
    
    category = st.selectbox("Pilih Marketing Skill:", all_categories)
    
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# --- INISIALISASI CLIENT & MEMORY ---
if not api_key:
    st.warning("Silakan masukkan DeepSeek API Key di sidebar untuk memulai.")
    st.stop()

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Ambil instruksi sistem berdasarkan kategori yang dipilih
system_instruction = get_marketing_skill(category)

# --- TAMPILAN CHAT ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Apa yang ingin Anda buat?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        api_messages = [
            {"role": "system", "content": system_instruction + "\nAlways respond in Indonesian."}
        ] + st.session_state.messages

        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=api_messages,
                stream=True 
            )
            
            for chunk in response:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
