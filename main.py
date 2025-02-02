import os
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Render!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Renderが指定するポートを取得
    uvicorn.run(app, host="0.0.0.0", port=port)
