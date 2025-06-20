import streamlit as st
from datetime import datetime
import base64
from PIL import Image
import io
import os

# Page configuration
st.set_page_config(
    page_title="Convolutional Neural Networks - Coursera",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 🎯 CUSTOMIZE YOUR DETAILS HERE ONLY
# ==========================================
# Replace with your details:

YOUR_NAME = "Ranjana Jha"
YOUR_COMPLETION_DATE_SPEC = "June 14, 2025"
YOUR_HOURS = "35 hours (approximately)"
DEFAULT_CERTIFICATE_PATH = "ranjanaCNNCertificate.jpeg.png"
DEEPLEARNING_LOGO_PATH = "deeplearning.png"

# Certificate upload section
st.sidebar.title("🎓 Certificate Options")
st.sidebar.markdown("Choose how to display your certificate:")

c# Upload logic
st.sidebar.title("🎓 Certificate Options")
certificate_option = st.sidebar.radio(
    "Certificate Display Option",
    ["Use Default Certificate", "Upload New Certificate"]
)

uploaded_certificate = st.sidebar.file_uploader("Upload certificate", type=['png', 'jpg', 'jpeg'])

@st.cache_data

def load_image(path):
    if os.path.exists(path):
        return Image.open(path)
    return None

# Load certificate
if certificate_option == "Upload New Certificate" and uploaded_certificate is not None:
    certificate_img = Image.open(uploaded_certificate)
else:
    certificate_img = load_image(DEFAULT_CERTIFICATE_PATH)

# Load logo
logo_img = load_image(DEEPLEARNING_LOGO_PATH)
if logo_img:
    buf = io.BytesIO()
    logo_img.save(buf, format="PNG")
    logo_b64 = base64.b64encode(buf.getvalue()).decode()
    logo_html = f'<img src="data:image/png;base64,{logo_b64}" style="height:56px;">'
else:
    logo_html = "🧠"

# Apply styles
st.markdown("""
<style>
    #MainMenu, header, footer {visibility: hidden;}
    .container { max-width: 1200px; margin: auto; padding: 40px 16px; }
    .header-bar { background: #0056D3; color: white; padding: 16px; font-size: 24px; font-weight: bold; }
    .nav-tabs { display: flex; gap: 24px; padding: 8px 0; font-size: 16px; border-bottom: 1px solid #ccc; }
    .nav-tabs div { padding-bottom: 4px; cursor: pointer; }
    .nav-tabs .active { border-bottom: 3px solid #0056D3; font-weight: bold; }
    .grid { display: grid; grid-template-columns: 2fr 1fr; gap: 32px; margin-top: 40px; }
    .certificate-container img { width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
    .info-box { background: linear-gradient(135deg, #e8f4fd 0%, #d1e7f8 100%); padding: 24px; border-radius: 8px; }
    .skills { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 16px; }
    .skill { padding: 6px 12px; background: white; border-radius: 16px; border: 1px solid #ccc; font-size: 13px; }
    .course-card { margin-top: 32px; border: 1px solid #ccc; padding: 24px; border-radius: 8px; }

    @media (max-width: 768px) {
        .grid { grid-template-columns: 1fr; }
        .certificate-container { order: -1; margin-bottom: 24px; }
    }
</style>
""", unsafe_allow_html=True)

# Render UI
st.markdown("""
<div class="header-bar">coursera</div>
<div class="nav-tabs">
    <div class="active">For Individuals</div>
    <div>For Businesses</div>
    <div>For Universities</div>
    <div>For Governments</div>
</div>
<div class="container">
    <div style="font-size:14px; color:#888;">Course Certificate</div>
    <h1 style="font-weight:400; margin-top:0;">Convolutional Neural Networks</h1>

    <div class="grid">
        <div>
            <div class="info-box">
                <div style="font-weight:bold; font-size:18px;">Completed by {YOUR_NAME}</div>
                <div style="margin:8px 0;">{YOUR_COMPLETION_DATE}</div>
                <div style="color:#555;">{YOUR_HOURS}</div>
                <div style="margin-top:12px; font-size:15px; color:#555;">
                    {YOUR_NAME}'s account is verified. Coursera certifies their successful completion of <b>Convolutional Neural Networks</b>
                </div>
            </div>

            <div class="course-card">
                <div style="display:flex; align-items:center; gap:16px;">
                    <div>{logo_html}</div>
                    <div>
                        <div style="font-size:20px; font-weight:600; color:#0056D3;">Convolutional Neural Networks</div>
                        <div style="color:#666;">DeepLearning.AI</div>
                    </div>
                </div>
                <div style="margin:16px 0; color:#555;">★★★★☆ 4.9 (42,492 ratings) | 540K Students Enrolled</div>
                <button style="background:#0056D3; color:white; padding:10px 20px; border:none; border-radius:4px; cursor:pointer;">Enroll for Free</button>
                <div class="skills">
                    <div class="skill">PyTorch</div>
                    <div class="skill">Algorithms</div>
                    <div class="skill">Artificial Neural Networks</div>
                    <div class="skill">Deep Learning</div>
                    <div class="skill">Tensorflow</div>
                    <div class="skill">Data Processing</div>
                    <div class="skill">Computer Vision</div>
                    <div class="skill">Image Analysis</div>
                    <div class="skill">Applied Machine Learning</div>
                    <div class="skill">Artificial Intelligence</div>
                </div>
            </div>
        </div>

        <div class="certificate-container">
""", unsafe_allow_html=True)

if certificate_img:
    st.image(certificate_img, use_column_width=True)

st.markdown("""
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
