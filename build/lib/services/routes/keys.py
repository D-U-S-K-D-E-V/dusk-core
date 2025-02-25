from fastapi import APIRouter

router = APIRouter(
    prefix="/key"
)

@router.post("/set")
async def set_keys(new_key: str):
    pass