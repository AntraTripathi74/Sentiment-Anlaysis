import streamlit as st
import vertexai
from vertexai.generative_models import GenerativeModel
import docx
import os

# Setting up the model
PROJECT_ID = "your-project-id"  # Replace with your Google Cloud project ID
# Ensure you have the Google Cloud SDK installed and authenticated
LOCATION = "us-central1"
vertexai.init(project=PROJECT_ID, location=LOCATION)
model = GenerativeModel("gemini-1.5-pro")

# Base prompt for the model
base_prompt = """
Task:
Summarize the provided sales call transcript in concise bullet points.
Determine the client's overall sentiment and interest level.
Identify areas where the sales representative could have improved their performance.

Output Format:
Sentiment Category: Interested or Not Interested
Summary of the Call: Key points from the conversation
Areas of Improvement: Specific suggestions for the sales representative

The transcript will be provided in the following format:
Speaker: Speaker's conversation
Additional Notes:
Pay close attention to hidden context and subtle cues that may indicate the client's true feelings.
If the client shows disinterest, attempts to delay the conversation, or tries to end it prematurely, classify them as "Not Interested."

Example:
Conversation Transcript:

Sales Rep: Hello, Mr. Smith. How are you today?

Client: Fine, thanks. What can I do for you?

Sales Rep: I'd like to discuss our new product...

Expected Output:
Sentiment Category: Not Interested
Summary of the Call: The sales rep introduced a new product. The client seemed disinterested and asked to be contacted later.
Areas of Improvement: The sales rep could have better engaged the client by asking questions about their needs and tailoring the presentation accordingly.
"""

# Function to extract text from DOCX
def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs if para.text])

# Function to analyze sentiment
def analyze_sentiment(file):
    transcript_text = extract_text_from_docx(file)
    final_prompt = base_prompt + transcript_text
    response = model.generate_content(final_prompt)
    output = response.text.strip()
    return output

# Streamlit UI
st.set_page_config(page_title="Sentiment Analysis with Gemini", layout="wide")

# Layout with logo and heading
col1, col2 = st.columns([4, 1])  # Adjust column widths as necessary
with col1:
    st.markdown("<h1 style='color: #34495e;'>Sentiment Analysis with Gemini</h1>", unsafe_allow_html=True)
with col2:
    logo_path = r"C:\Users\Antra Tripathi\Desktop\projects\sentiment analysis\google-gemini-icon.png"  # Local path to your logo
    st.image(logo_path, use_column_width=False, width=70)

# Vertical layout for file uploader and results
st.markdown("### Upload a DOC/DOCX file")
uploaded_file = st.file_uploader("", type=["docx", "doc"])
if uploaded_file:
    result = analyze_sentiment(uploaded_file)
    # st.markdown("### Sentiment Analysis Result")
    st.markdown(result)

# Add some styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f0f5;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)
