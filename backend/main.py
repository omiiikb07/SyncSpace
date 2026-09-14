from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI(
    title="SyncSpace API",
    description="Backend API for message and audio call detection",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "SyncSpace API is running",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "SyncSpace Backend",
        "time": datetime.now().isoformat()
    }


@app.post("/analyze/message")
def analyze_message(message_data: dict):
    message = message_data.get("message", "")

    suspicious_words = [
        "scam",
        "fraud",
        "otp",
        "password",
        "urgent",
        "blocked",
        "verify"
    ]

    detected_words = [
        word for word in suspicious_words
        if word in message.lower()
    ]

    if detected_words:
        risk_level = "High"
        risk_score = 85
    else:
        risk_level = "Low"
        risk_score = 15

    return {
        "type": "message",
        "message": message,
        "risk_level": risk_level,
        "risk_score": risk_score,
        "detected_words": detected_words,
        "analysis": "Suspicious words detected."
        if detected_words
        else "No suspicious words detected."
    }


@app.post("/analyze/audio")
def analyze_audio(audio_data: dict):
    duration = audio_data.get("duration", 0)

    return {
        "type": "audio",
        "duration": duration,
        "risk_level": "Pending",
        "risk_score": 0,
        "analysis": "Audio analysis service will be connected next."
    }