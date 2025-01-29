from fastapi import APIRouter
from app.schemas import CreateUser, UpdateUser

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def all_users():
    return {"message": "Get All Users"}


@router.get("/{user_id}")
async def user_by_id(user_id: int):
    return {"message": f"Get User by id: {user_id}"}


@router.post("/create")
async def create_user(user: CreateUser):
    return {"message": "Create User"}


@router.put("/update")
async def update_user(user: UpdateUser):
    return {"message": "Update User"}


@router.delete("/delete")
async def delete_user():
    return {"message": "Delete User"}

