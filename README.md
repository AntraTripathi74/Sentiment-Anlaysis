# Sentiment-Analysis

This repository contains a Sentiment Analysis application built with Python. It leverages Google's Gemini 1.5 Pro to analyze uploaded sales call transcripts (DOCX files) and determine the client's sentiment, summarize the call, and identify areas for improvement for the sales representative. The user interface is provided by Streamlit, offering an intuitive way to upload files and view the analysis results.

## ✨ Features

* Gemini 1.5 Pro Powered: Leverages advanced AI for sentiment detection and summarization while preserving context.
* Sentiment Categorization: Clearly identifies client sentiment as "Interested" or "Not Interested."
* Concise Summaries: Get bullet-point summaries of key conversation points.
* Performance Improvement Suggestions: Receives actionable feedback for sales representatives.
* User-Friendly Streamlit UI: Simple and intuitive web interface for uploading files and viewing results.

## 🚀 Prerequisites

* Google Cloud Project: You need a Google Cloud project with the Vertex AI API enabled.
* Authentication: Ensure you have the Google Cloud SDK installed and are authenticated to your Google Cloud project.
* Gemini 1.5 Pro Access: Your Google Cloud project must have access to the `gemini-1.5-pro` model.
