from fastapi import FastAPI 
from pydantic import BaseModel
import models.models as model


app = FastAPI()
user1 = model.User(id = 1, name = 'Ann', age = 20)

@app.get('/')
async def root():
    return {'message': 'Hello, FastAPI!' }


@app.get("/users")
def root_users():
    return user1

def age_verification(age: int):
    if age >= 18: return True
    return False


@app.post('/user')
def post_user(user: model.User):
    return {'name': user.name, 'age': user.age, 'is_adult': age_verification(user.age)}
