from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def admin_index():
    return {"message": "Admin getting schwifty"}
