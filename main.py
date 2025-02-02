from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Render!"}

@app.get("/post")
def test_post():
    return {"status": "Threads API integration coming soon!"}
