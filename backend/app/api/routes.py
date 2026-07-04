from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Welcome to MultiAgent OS 🚀",
        "version": "1.0.0",
        "status": "Running"
    }