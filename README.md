# Visionary AI 🔮

Welcome to **Visionary AI**, an advanced image analysis platform powered by the cutting-edge Gemini AI model. With **Visionary AI**, you can upload your images and interact with them like never before, extracting deep insights, text analysis, and more, all in real-time. 

## Features 🌟
- **Advanced Image Analysis:** Leverage the power of Gemini AI for fast and accurate image insights.
- **Text Extraction (OCR):** Automatically extract and analyze text from your images.
- **Real-Time Analysis:** Get instant feedback and analysis on any uploaded image.
- **Multi-format Support:** Upload images in JPG, JPEG, or PNG formats.
- **Downloadable Results:** Download the analysis as a `.txt` file for further reference.
- **Customizable Prompts:** Ask specific questions about the image and get tailored insights.

## 🚀 How It Works

1. **Upload an Image:** Drag and drop or click to upload an image (JPG, JPEG, or PNG).
2. **Ask a Question:** Type in your query about the image (e.g., "Extract all text" or "Analyze the image content").
3. **Get Detailed Insights:** Press the "Analyze with Gemini AI" button, and let Visionary AI generate insights in seconds!
4. **Download Results:** Save the analysis for future reference.

## ⚙️ Installation & Setup

### Prerequisites

Before you begin, make sure you have Python 3.7+ installed on your system.

### Steps to Run the App

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/visionary-ai.git


2. **Navigate to the project directory**
   ```bash
   cd visionary-ai

3. **Create a Virtual Environment (optional but recommended)**
   ```bash
   python -m venv venv

4. **Activate the Virtual Environment**
  - Windows:
    ```bash
    venv\Scripts\activate

  - Mac/Linux:
    ```bash
    source venv/bin/activate.

5. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

6. **Set up the API Key**
 - Create a .env file in the root directory of the project.
 - Add your Google API key:
   ```makefile
   GOOGLE_API_KEY=your_api_key_here

7. **Run the Application**
   ```bash
   streamlit run app.py

Open the web app in your browser at http://localhost:8501 and start uploading images!

## 🎨 Customization

You can customize the app to your liking by editing the app.py file or tweaking the styles in the CSS section. To add more features or integrate additional models, simply extend the functionality of the code!

## 📚 Dependencies

- **Streamlit**: For creating interactive web apps.
- **Python-dotenv**: For loading environment variables.
- **Pillow**: For image processing.
- **Google Generative AI**: The API used for image analysis.

### 💡 Contributing
Feel free to fork this repository and submit pull requests for improvements, bug fixes, or new features!

## 🚨 Important Notes

- **Google API Key**: Make sure to configure your Google API key in the .env file to start using the AI capabilities.
- **Performance** : The image analysis may take a few moments depending on the size of the image and your internet speed.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.


