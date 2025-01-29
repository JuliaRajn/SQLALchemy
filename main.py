from fastapi import FastAPI
from app.routers import task_router, user_router
from sqlalchemy import create_engine
from app.backend.db import Base
from app.models import User, Task

# Создаем движок базы данных и выводим SQL
engine = create_engine("sqlite:///taskmanager.db", echo=True)

# Импортируем модели и создаем таблицы
Base.metadata.create_all(bind=engine)


# Создаем FastAPI приложение
app = FastAPI()


# Подключаем роутеры
app.include_router(task_router)
app.include_router(user_router)


# Маршрут для приветственного сообщения
@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


