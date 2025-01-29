from fastapi import APIRouter
from app.schemas import CreateTask, UpdateTask

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks():
    return {"message": "Get All Tasks"}


@router.get("/{task_id}")
async def task_by_id(task_id: int):
    return {"message": f"Get Task by id: {task_id}"}


@router.post("/create")
async def create_task(task: CreateTask):
    return {"message": "Create Task"}


@router.put("/update")
async def update_task(task: UpdateTask):
    return {"message": "Update Task"}


@router.delete("/delete")
async def delete_task():
    return {"message": "Delete Task"}


