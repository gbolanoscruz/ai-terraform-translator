# 🏗️ AI-Powered Terraform Cloud Translator

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B.svg)
![Gemini AI](https://img.shields.io/badge/Google%20GenAI-Gemini%203.1-4285F4.svg)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC.svg)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF.svg)

## 📖 Overview
This project is an AI-driven Infrastructure as Code (IaC) translation tool designed for modern DevOps and SRE teams. It leverages **Google's Gemini 3.1 Flash Lite** model via the new `google-genai` SDK to automatically analyze, detect, and translate Terraform configurations between major cloud providers (AWS, Azure, and GCP).

Built with a focus on observability, automation, and software engineering best practices, the repository includes a responsive UI, automated static code analysis, unit testing, and a containerized CI/CD pipeline.

## ✨ Key Features
* **Intelligent Provider Detection:** Automatically parses `.tf` files to identify the source cloud environment using RegEx.
* **Agentic AI Translation:** Translates infrastructure resources and applies target-cloud best practices using Google's Gemini AI.
* **Modern UI:** Built with Streamlit for a seamless, fast, and interactive user experience.
* **Production-Ready CI/CD:** Fully automated GitHub Actions workflow for linting (`flake8`), unit testing (`pytest`), and Docker builds.
* **Secure by Design:** API keys are managed exclusively via environment variables (`.env`).

---

## 🚀 Local Development Setup

### 1. Prerequisites
* Python 3.12+
* Git
* A Google Gemini API Key (Get one at [Google AI Studio](https://aistudio.google.com/))

### 2. Clone the Repository
```bash
git clone [https://github.com/gbolanoscruz/ai-terraform-translator.git](https://github.com/gbolanoscruz/ai-terraform-translator.git)
cd ai-terraform-translator

### 3. Configure the Virtual Environment (Windows)
```PowerShell
python -m venv venv
.\venv\Scripts\activate

### 4. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt

### 5. Configure Environment Variables
Create a .env file in the root directory and add your Google AI API key. (This file is ignored by Git).

```Plaintext
GEMINI_API_KEY=your_api_key_here

### 6. Run the Application
```bash
streamlit run app.py

The application will be available in your browser at http://localhost:8501.

🧪 Testing & Quality Assurance

This project uses pytest for unit testing and flake8 for static code analysis.

Run Unit Tests:
```bash
python -m pytest "test/Unit Tests/test_app.py" -v

Run Linter:
```bash
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

🐳 Docker Deployment
To build and run the application as an isolated container:
```bash
# Build the image
docker build -t ai-terraform-translator:latest .

# Run the container (Make sure to pass your API key)
docker run -p 8501:8501 -e GEMINI_API_KEY="your_api_key_here" ai-terraform-translator:latest

⚙️ CI/CD Architecture

This repository implements a strict continuous integration pipeline using GitHub Actions. On every push or pull_request to the main branch, the pipeline:

    1. Provisions an Ubuntu runner.

    2. Checks out the code and sets up Python 3.12.

    3. Lints the codebase for syntax errors and PEP8 compliance.

    4. Executes unit tests with a mocked API key to ensure core logic integrity.

    5. Builds the Docker container to guarantee deployment readiness.

Built with 💻 by Gustavo Bolaños