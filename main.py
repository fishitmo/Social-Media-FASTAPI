from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

@app.get("/")
def root():
    return {"message": "Hello, Fish Kemei Aleka!"}

@app.get("/posts")
def get_post():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}
