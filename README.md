# 🧠 Face Verification API (FastAPI + DeepFace)

This is a lightweight Python-based microservice for face verification using DeepFace. It compares a user's selfie with their NID (National ID) photo and returns a verification result and similarity confidence score.

---

## 🚀 Features

- Face comparison using DeepFace
- Accepts base64-encoded images
- Returns `verified` boolean and `confidence` score
- Built with FastAPI for speed and flexibility

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI**
- **DeepFace**
- **OpenCV**
- **Uvicorn**

---

## 📦 Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/face-verification-api.git
   cd face-verification-api
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Running the Service

1. Run the FastAPI server using uvicorn:

   ```bash
   uvicorn face_verify_service:app --host 0.0.0.0 --port 5001
   ```

2. Your API will be live at:

   ```bash
   http://localhost:5001/docs
   ```
