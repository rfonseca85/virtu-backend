from fastapi import APIRouter, UploadFile, File, Depends
from src.model.virtu_chef_models import Receipe
from src.model.user_auth_models import User
import base64
import src.service.virtu_chef_service as vcs
import src.service.user_auth_service as uas

router = APIRouter(tags=["virtu_chef"])

@router.post("/get_receipe", response_model=Receipe)
async def get_receipe(file: UploadFile = File(...), current_user: User = Depends(uas.get_current_active_user)):
    # Read the image file
    image_data = await file.read()
    image_base64 = base64.b64encode(image_data).decode("utf-8")
    receipe = vcs.get_receipe(image_base64) 
    return receipe