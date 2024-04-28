from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str


class User(BaseModel):
    clerkId: str
    email: str
    username: str
    photo: str
    firstName: str
    lastName: str
    planId: int
    creditBalance: int








