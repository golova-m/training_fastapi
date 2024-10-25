from fastapi import FastAPI 
from pydantic import BaseModel
import app.models.models as model


app = FastAPI()
#user1 = model.User(id = 1, name = 'Ann', email = 'ann@example.com')

# Пример пользовательских данных (для демонстрационных целей) 
fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
}


feedback_users = []


@app.post('/add_fake')
async def add_fake(username: str, user_info: str):
    fake_db.append({'username': username, 'user_info': user_info})
    return {"message": "юзер успешно добавлен в базу данных"}


@app.get('/')
async def root():
    return {'message': 'Hello, FastAPI!' }


@app.get("/users")
def root_users():
    return user1


@app.get('/users/{user_id}')
def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}

def age_verification(age: int):
    if age >= 18: return True
    return False


@app.post('/user')
def post_user(user: model.User):
    return {'name': user.name, 'age': user.age, 'is_adult': age_verification(user.age)}


@app.post('/feedback')
def post_feedback(feedback: model.Feedback):
    feedback_users.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}!"}


@app.get('/all_feedback')
def get_all_feedback():
    return feedback_users