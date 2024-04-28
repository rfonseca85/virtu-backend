from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["health_check"])


@router.get("/health_check", response_class=HTMLResponse)
async def get_status():
    return HTMLResponse(
        content="<h3>Your backend is running correctly</h3>"
    )
