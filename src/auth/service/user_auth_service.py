from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from src.auth.model.user_auth_models import TokenData, User
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client['virtu-hunter-db']
users_collection = db['users']

# Create a password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(username: str, password: str):
    user_from_db = users_collection.find_one({"username": username})
    if user_from_db is None:
        print("User not found")
        return False
    else:
        user = User(**user_from_db)
        if pwd_context.verify(password, user.password) is False:
            print("Password incorrect")
            return False
        print("User authenticated")
        return user


def create_user(user: User) -> User:
    # Check if a user with the same username already exists
    existing_user = users_collection.find_one({"username": user.username})
    if existing_user is not None:
        return None

    # Hash the password
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password

    # Insert the user into the database
    users_collection.insert_one(dict(user))

    return user

def create_access_token(data: dict, expires_delta: timedelta ):
    to_encode = data.copy()
    # if expires_delta:
    #     expire = datetime.utcnow() + expires_delta
    # else:
    #     expire = datetime.utcnow() + timedelta(minutes=15)

    # to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception

        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception

    user = users_collection.find_one({"clerkId": token_data.username})
    if user is None:
        raise credential_exception

    return User(**user)


