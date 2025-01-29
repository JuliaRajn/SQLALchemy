from pydantic import BaseModel
from typing import Optional

class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

class UpdateUser(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    age: Optional[int] = None

class CreateTask(BaseModel):
    title: str
    content: str
    priority: int


class UpdateTask(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    priority: Optional[int] = None
