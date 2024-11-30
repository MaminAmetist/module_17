from fastapi import FastAPI
from app.routers import user
from app.routers import task

app = FastAPI()


@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router_user)
app.include_router(task.router_task)

