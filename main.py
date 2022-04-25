from turtle import title
from urllib import request
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI()

@app.get('/blog')
def index():
    return {'data': 'blogs from the db'}

class Blog(BaseModel):
    title: str
    body: str
    #published: Optional(bool)

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is created with little as {blog.title}"}



"""if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)"""