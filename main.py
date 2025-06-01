from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, Fish Kemei Aleka!"}

@app.get("/")
def get_post():
    return {"data": "This is your posts"}
