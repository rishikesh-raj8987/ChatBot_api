

from fastapi import FastAPI
from schemas import ChatRequest


app = FastAPI()

@app.post(/"chat",response_model=Chatresponse)
def char(req: ChatRequest):