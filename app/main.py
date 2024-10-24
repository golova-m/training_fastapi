from fastapi import FastAPI 
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    username: str
    message: str  


@app.get('/')
async def root():
    return {'message': 'Hello, FastAPI!' }


@app.get("/custom")
def root_html():
    return {"message": "This is a custom message!"}


@app.post('/')
async def root(user: User):
    return user