from fastapi import Body, Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import  timedelta
from src.model.user_auth_models import User, Token
from dotenv import load_dotenv
import os
import src.service.user_auth_service as uas

# Load the .env file
load_dotenv()

router = APIRouter(tags=["user_auth"])

@router.post("/users/", response_model=User)
async def create_user(user: User = Body(...)):
    created_user = uas.create_user(user)
    if created_user is None:
        raise HTTPException(status_code=400, detail="User already exists")
    return created_user


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = uas.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = uas.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(uas.get_current_active_user)):
    return current_user


