import streamlit as st
from dotenv import load_dotenv
import os
import base64
import io
import pandas as pd
from PIL import Image, ImageEnhance
import google.generativeai as genai

# Load API key from environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit Page Configuration
st.set_page_config(
    page_title="Visionary AI: Advanced Image Analysis Powered by Gemini AI",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for UI Enhancement
st.markdown("""
    <style>
    .main { padding: 2rem; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3rem; background-color: #4CAF50; color: white; font-weight: bold; }
    .uploadedImage { border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
    .stTextArea>div>div>textarea { border-radius: 10px; }
    .stDownloadButton>button { width: 100%; }
    </style>
""", unsafe_allow_html=True)

# Sidebar with Information
with st.sidebar:
    st.title("🔮 Visionary AI")
    st.subheader("Advanced Image Analysis Powered by Gemini AI")
    st.markdown("""
        **Features:**  
        - Advanced AI-Powered OCR  
        - Multi-Image Upload Support  
        - Image Preprocessing for Better OCR  
        - PDF & CSV Export of Results  
        - Live Webcam Capture  
        - Dark Mode Support  
    """)
    st.markdown("---")
    st.caption("Powered by **Google Gemini AI** 🚀")

# Function to optimize and enhance image for better OCR results
def enhance_image(image):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(2.0)  # Increase contrast for better text recognition

# Function to handle AI processing
def get_gemini_response(input_prompt, image_data):
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    response = model.generate_content([input_prompt, image_data[0]])
    return response.text

# Image Processing Helper
def process_uploaded_images(uploaded_files):
    processed_images = []
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        image = enhance_image(image)  # Apply preprocessing
        bytes_data = io.BytesIO()
        image.save(bytes_data, format="PNG")
        image_data = [{
            "mime_type": "image/png",
            "data": bytes_data.getvalue()
        }]
        processed_images.append((image, image_data))
    return processed_images

# Main Section
st.title("🌟 Visionary AI: Advanced Image Analysis Powered by Gemini AI")
st.markdown("Upload images and let Neural Lens extract insights!")

# Live Webcam Capture
use_webcam = st.checkbox("📷 Capture Image from Webcam")
uploaded_files = st.file_uploader("Upload Images (JPEG/PNG)", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Capture Image via Webcam
if use_webcam:
    webcam_image = st.camera_input("Take a picture")
    if webcam_image:
        uploaded_files.append(webcam_image)

# User Query Input
user_query = st.text_area(
    "What insights do you need from the image?",
    placeholder="E.g., Extract all text and analyze the content...",
    height=100
)

# Display Uploaded Images
if uploaded_files:
    st.subheader("Uploaded Images")
    col1, col2 = st.columns(2)
    with col1:
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

# Perform AI Analysis
if st.button("🔍 Analyze with Neural Lens"):
    if not user_query.strip():
        st.error("⚠️ Please enter a query before analyzing.")
    elif not uploaded_files:
        st.error("⚠️ Please upload at least one image.")
    else:
        with st.spinner("🤖 Neural Lens is analyzing..."):
            try:
                processed_images = process_uploaded_images(uploaded_files)
                full_response = []
                
                for image, image_data in processed_images:
                    response = get_gemini_response(user_query, image_data)
                    full_response.append(response)
                
                # Display Results
                st.success("✨ Analysis Complete!")
                st.subheader("📊 AI Analysis Results")
                for i, response in enumerate(full_response):
                    st.markdown(f"### Image {i+1}")
                    st.markdown(response)

                # Save as Text File
                txt_response = "\n\n".join(full_response)
                st.download_button("📥 Download Analysis (TXT)", txt_response, "neural_lens_analysis.txt")

                # Save as CSV
                df = pd.DataFrame({"Image": [f"Image {i+1}" for i in range(len(full_response))], "Analysis": full_response})
                csv_response = df.to_csv(index=False).encode('utf-8')
                st.download_button("📥 Download Analysis (CSV)", csv_response, "neural_lens_analysis.csv", "text/csv")

            except Exception as e:
                st.error(f"🚫 Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center'><p>Created with ❤️ using Streamlit & Google Gemini AI</p></div>",
    unsafe_allow_html=True
)
