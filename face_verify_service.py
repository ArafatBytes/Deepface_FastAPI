from fastapi import FastAPI
from pydantic import BaseModel
from deepface import DeepFace
import base64
import cv2
import numpy as np

app = FastAPI()

class VerifyRequest(BaseModel):
    nid: str
    selfie: str

def base64_to_image(base64_str):
    # Remove data URL prefix if present
    if ',' in base64_str:
        base64_str = base64_str.split(',')[1]
    img_data = base64.b64decode(base64_str)
    np_arr = np.frombuffer(img_data, np.uint8)
    return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

@app.post("/verify")
async def verify_faces(req: VerifyRequest):
    try:
        img1 = base64_to_image(req.nid)
        img2 = base64_to_image(req.selfie)
        # DeepFace returns a dict with 'verified' and 'distance'
        result = DeepFace.verify(img1, img2, enforce_detection=True)
        # DeepFace: lower distance = more similar, verified = True if below threshold
        confidence = 1.0 - float(result.get('distance', 1.0))  # Invert for confidence-like score
        verified = result.get('verified', False)
        return {
            "verified": bool(verified),
            "confidence": round(confidence, 3)
        }
    except Exception as e:
        return {"verified": False, "confidence": 0.0, "error": str(e)}

# To run: uvicorn face_verify_service:app --host 0.0.0.0 --port 5001
