from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, Fish Kemei Aleka!"}

@app.get("/posts")
def get_post():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_post():
    return {"message": "Succesfully created posts"}
