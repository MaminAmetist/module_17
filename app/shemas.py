from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int
    slug: None


class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int
    user_id: int
    slug: None
    completed: None


class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int
