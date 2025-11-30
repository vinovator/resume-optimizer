# 👔 Resume Optimizer Pro

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://resume-optimizer-pro.streamlit.app/)

Resume Optimizer Pro is an AI-powered application designed to help job seekers tailor their resumes to specific job descriptions. Powered by **CrewAI** and **Google Gemini**, it simulates a hiring committee to analyze your resume against a job description (JD) and provides actionable feedback and optimization.

**Live Demo:** [https://resume-optimizer-pro.streamlit.app/](https://resume-optimizer-pro.streamlit.app/)

## 🚀 Features

The application employs a multi-agent system acting as a "Hiring Committee":

1.  **HR & Tech Screener**:
    *   Validates hard requirements: Technical Skills, Education, Experience, and Location.
    *   Identifies missing keywords and gaps.
2.  **Culture Fit Analyst**:
    *   Assesses soft skills and leadership traits.
    *   Evaluates the tone and cultural alignment of the resume.
3.  **Professional Resume Writer**:
    *   Rewrites the Professional Summary to align with the JD.
    *   Optimizes bullet points to include missing keywords and improve impact.

**Key Outputs:**
*   **Match Score**: A weighted score (0-100%) indicating how well the resume fits the JD.
*   **Detailed Breakdown**: Specific scores for Tech Skills, Experience, Education, and Location.
*   **Gap Analysis**: Explicit lists of missing hard/soft skills and experience gaps.
*   **Optimization**: A tailored summary and improved bullet points ready to copy-paste.

## 🛠️ Tech Stack

*   **[CrewAI](https://crewai.com)**: Orchestrates the multi-agent AI system.
*   **[Streamlit](https://streamlit.io)**: Provides the interactive web interface.
*   **[Google Gemini](https://deepmind.google/technologies/gemini/)**: The LLM powering the agents.
*   **Pydantic**: Ensures structured and reliable data output.

## 📋 Prerequisites

*   Python 3.10 or higher
*   A Google Gemini API Key

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd resume-optimizer
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Configuration

1.  Create a `.env` file in the root directory.
2.  Add your Google Gemini API key:
    ```env
    GOOGLE_API_KEY=your_gemini_api_key_here
    ```

## ▶️ Usage

1.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

2.  **Use the Interface:**
    *   Paste your **Resume** text in the left column.
    *   Paste the **Job Description** in the right column.
    *   Click **"Analyze Resume against JD"**.

3.  **View Results:**
    *   Watch the agents work in real-time (Thinking/Action logs).
    *   Review your Match Score and detailed feedback.
    *   Use the "Optimized Summary" and "Improved Bullet Points" to update your resume.

## 📂 Project Structure

```
resume-optimizer/
├── app.py                # Main Streamlit application entry point
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (API keys)
└── src/
    ├── agents.py         # Definitions of CrewAI agents (Screener, Analyst, Writer)
    ├── tasks.py          # Definition of the analysis task
    ├── crew.py           # CrewAI orchestration logic
    ├── models.py         # Pydantic models for structured output
    └── config.py         # LLM configuration
```
