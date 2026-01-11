from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
import os

from openai import OpenAI

# 🔥 VERY IMPORTANT — load .env FIRST
load_dotenv()

# Debug (optional)
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

# Create OpenAI client AFTER loading env
client = OpenAI()

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=req.message
    )

    return {
        "reply": response.output[0].content[0].text
    }
