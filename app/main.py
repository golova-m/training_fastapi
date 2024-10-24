from fastapi import FastAPI 
from fastapi.responses import FileResponse
from pydantic import BaseModel


app = FastAPI()


@app.get('/')
async def root():
    return FileResponse('templates/index.html')


@app.get("/file", response_class = FileResponse)
def root_html():
    return 'templates/index.html'


@app.post('/calculate')
def calculate(num1: int, num2: int):
    print({"result": num1 + num2})
    return {"result": num1 + num2}