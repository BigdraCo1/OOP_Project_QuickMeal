from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer


app = APIRouter(prefix='/auth')


oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')