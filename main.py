from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating : Optional[int] = None

@app.get("/")
def root():
    return {"message": "Hello, Fish Kemei Aleka!"}

@app.get("/posts")
def get_post():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_post(post: Post):
    print(post.rating)
    print(post.dict())  # Convert to dictionary if needed
    return {"Data": post}
