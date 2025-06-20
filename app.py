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
YOUR_COMPLETION_DATE = "June 14, 2025"
YOUR_HOURS = "35 hours (approximately)"
DEFAULT_CERTIFICATE_PATH = "ranjanaCNNCertificate.jpeg.png"
DEEPLEARNING_LOGO_PATH = "deeplearnin.png"

# Certificate upload section
st.sidebar.title("🎓 Certificate Options")
st.sidebar.markdown("Choose how to display your certificate:")

certificate_option = st.sidebar.radio(
    "Certificate Display Option",
    ["Use Default Certificate", "Upload New Certificate"],
    help="Choose to use your default certificate or upload a new one"
)

uploaded_certificate = None
if certificate_option == "Upload New Certificate":
    uploaded_certificate = st.sidebar.file_uploader(
        "Choose your certificate PNG file", 
        type=['png', 'jpg', 'jpeg'],
        help="Upload your certificate image (PNG/JPG format)"
    )

# Function to load default certificate
@st.cache_data
def load_default_certificate():
    """Load the default certificate image"""
    try:
        if os.path.exists(DEFAULT_CERTIFICATE_PATH):
            return Image.open(DEFAULT_CERTIFICATE_PATH)
        else:
            return None
    except Exception as e:
        return None

# Function to load DeepLearning logo
@st.cache_data
def load_deeplearning_logo():
    """Load the DeepLearning.AI logo"""
    try:
        if os.path.exists(DEEPLEARNING_LOGO_PATH):
            return Image.open(DEEPLEARNING_LOGO_PATH)
        else:
            return None
    except Exception as e:
        return None

# Styling
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .main > div {padding-top: 0rem;}
    .stAlert, .stSuccess, .stInfo, .stWarning, .stError {display: none;}
    .main-content {max-width: 1200px; margin: auto; padding: 40px 24px; background: white;}
    .main-header {background: #0056D3; padding: 12px 0; margin: -1rem -1rem 0rem -1rem;}
    .header-content {max-width: 1200px; margin: auto; display: flex; justify-content: space-between; padding: 0 24px; color: white; font-size: 16px;}
    .coursera-logo {font-size: 28px; font-weight: bold;}
    .nav-menu {background: white; padding: 8px 0; border-bottom: 1px solid #e1e1e1; margin: 0rem -1rem;}
    .nav-items {max-width: 1200px; margin: auto; display: flex; gap: 40px; padding: 0 24px; color: #666; font-size: 16px;}
    .nav-item.active {border-bottom: 3px solid #0056D3; color: #0056D3; font-weight: 500;}
    .completion-section {display: grid; grid-template-columns: 2fr 1fr; gap: 40px; align-items: flex-start;}
    .completion-banner {background: linear-gradient(135deg, #e8f4fd 0%, #d1e7f8 100%); padding: 32px; border-radius: 8px; display: flex; gap: 24px;}
    .checkmark {background: #00C851; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; color: white; font-size: 18px; font-weight: bold;}
    .completion-text {font-size: 24px; font-weight: 600;}
    .certificate-container {background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);}
    .specialization-card {background: white; border: 1px solid #e1e1e1; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);}
    .skills-grid {display: flex; flex-wrap: wrap; gap: 12px; padding: 16px;}
    .skill-tag {background: white; border: 1px solid #d1d1d1; padding: 8px 16px; border-radius: 16px; font-size: 14px; color: #666;}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(f"""
<div class="main-header">
  <div class="header-content">
    <div class="coursera-logo">coursera</div>
    <div>{YOUR_NAME[0]}</div>
  </div>
</div>
<div class="nav-menu">
  <div class="nav-items">
    <div class="nav-item active">For Individuals</div>
    <div class="nav-item">For Businesses</div>
    <div class="nav-item">For Universities</div>
    <div class="nav-item">For Governments</div>
  </div>
</div>
""", unsafe_allow_html=True)

# Header
st.markdown(f"""
<div class="main-header">
    <div class="header-content">
        <div class="coursera-logo">coursera</div>
        <div class="header-nav">
            <input type="text" class="header-search" placeholder="What do you want to learn?">
            <span>Online Degrees</span>
            <span>Careers</span>
            <span>English</span>
            <span>{YOUR_NAME[0]}</span>
        </div>
    </div>
</div>

<div class="nav-menu">
    <div class="nav-items">
        <div class="nav-item active">For Individuals</div>
        <div class="nav-item">For Businesses</div>
        <div class="nav-item">For Universities</div>
        <div class="nav-item">For Governments</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Main content container
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Breadcrumb
st.markdown('<div class="breadcrumb">Course Certificate</div>', unsafe_allow_html=True)

# Course title
st.markdown('<h1 class="course-title">Convolutional Neural Networks</h1>', unsafe_allow_html=True)

# Main completion section with responsive grid
st.markdown('<div class="completion-section">', unsafe_allow_html=True)

# Left column - Completion banner and course info
st.markdown('<div class="completion-left">', unsafe_allow_html=True)

# Completion banner with profile
st.markdown(f"""
<div class="completion-banner">
    <div class="profile-section">
        <div class="profile-avatar">
            👤
            <div class="checkmark-overlay">✓</div>
        </div>
        <div class="completion-details">
            <div class="completion-text">Completed by {YOUR_NAME}</div>
            <div class="completion-date">{YOUR_COMPLETION_DATE}</div>
            <div class="completion-hours">{YOUR_HOURS}</div>
            <div class="verification-text">
                {YOUR_NAME}'s account is verified. Coursera certifies their successful completion of <strong>Convolutional Neural Networks</strong>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Load DeepLearning logo
deeplearning_logo = load_deeplearning_logo()

# Course info card with logo handling
if deeplearning_logo:
    # Convert PIL image to base64 for HTML embedding
    buffered = io.BytesIO()
    deeplearning_logo.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    logo_html = f'<img src="data:image/png;base64,{img_str}" alt="DeepLearning.AI Logo">'
else:
    logo_html = '🧠'  # Fallback to brain emoji

st.markdown(f"""
<div class="course-card">
    <div class="course-header">
        <div class="course-logo">{logo_html}</div>
        <div class="course-details">
            <h2>Convolutional Neural Networks</h2>
            <p class="course-provider">DeepLearning.AI</p>
        </div>
    </div>
    
    <div class="rating-section">
        <span class="stars">★★★★★</span>
        <span class="rating-text">4.9 (42,492 ratings) | 540K Students Enrolled</span>
    </div>
    
    <button class="enroll-btn">Enroll for Free</button>
    
    <div class="skills-section">
        <div class="skills-title">SKILLS YOU WILL GAIN</div>
        <div class="skills-grid">
            <div class="skill-tag">PyTorch (Machine Learning Library)</div>
            <div class="skill-tag">Algorithms</div>
            <div class="skill-tag">Artificial Neural Networks</div>
            <div class="skill-tag">Deep Learning</div>
            <div class="skill-tag">Tensorflow</div>
            <div class="skill-tag">Data Processing</div>
            <div class="skill-tag">Computer Vision</div>
            <div class="skill-tag">Applied Machine Learning</div>
            <div class="skill-tag">Image Analysis</div>
            <div class="skill-tag">Artificial Intelligence</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close left column

# Right column - Certificate
st.markdown('<div class="completion-right">', unsafe_allow_html=True)

# Certificate display logic - NO STATUS MESSAGES
certificate_to_display = None

if certificate_option == "Use Default Certificate":
    certificate_to_display = load_default_certificate()
elif uploaded_certificate is not None:
    try:
        certificate_to_display = Image.open(uploaded_certificate)
    except Exception:
        certificate_to_display = None

# Display certificate silently
if certificate_to_display is not None:
    st.markdown('<div class="certificate-container">', unsafe_allow_html=True)
    st.image(certificate_to_display, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close right column
st.markdown('</div>', unsafe_allow_html=True)  # Close completion section
st.markdown('</div>', unsafe_allow_html=True)  # Close main content

# Footer
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <div>© 2025 Coursera Inc. All rights reserved.</div>
        <div class="footer-social">
            <span>🌐 Facebook</span>
            <span>💼 LinkedIn</span>
            <span>🐦 Twitter</span>
            <span>📺 YouTube</span>
            <span>📸 Instagram</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar info (kept minimal to not interfere with main design)
st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 Quick Info")
st.sidebar.info(f"""
**Student Name:** {YOUR_NAME}
**Course:** Convolutional Neural Networks
**Provider:** DeepLearning.AI
**Completion Date:** {YOUR_COMPLETION_DATE}
**Duration:** {YOUR_HOURS}
""")

# Hide all Streamlit messages and warnings
st.markdown("""
<script>
// Hide all status messages and warnings
const hideElements = () => {
    const elementsToHide = document.querySelectorAll('.stAlert, .stSuccess, .stInfo, .stWarning, .stError, [data-testid="stAlert"]');
    elementsToHide.forEach(el => el.style.display = 'none');
};

// Run on page load and periodically
hideElements();
setInterval(hideElements, 1000);
</script>
""", unsafe_allow_html=True)