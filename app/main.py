from fastapi import FastAPI 

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello, FastAPI!' }


@app.get("/custom")
def root_html():
    return {"message": "This is a custom message!"}