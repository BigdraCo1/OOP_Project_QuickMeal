from pydantic import BaseModel


class CreatUserRequest(BaseModel):
    username: str
    password: str
    telephone_number: str
    email: str
    fullname: str
    role: str


class Token(BaseModel):
    access_token: str
    token_type: str