from fastapi import APIRouter, UploadFile, File, Depends
import base64
from src.virtu_hunter.models.virtu_hunter_models import CoverLetter, CoverLetterRequest
from src.auth.model.user_auth_models import User
import src.auth.service.user_auth_service as uas
import src.virtu_hunter.service.virtu_hunter_service as vhs

router = APIRouter(tags=["Virtu.hunter"])

@router.post("/coverletter")#response_model=CoverLetter
async def generate_coverletter(request: CoverLetterRequest, current_user: User = Depends(uas.get_current_user)):
    # Read the image file
    coverletter = vhs.get_coverletter(request) 
    # CoverLetter = CoverLetter(coverletter=coverletter)
    return coverletter