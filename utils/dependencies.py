from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import os
from dotenv import load_dotenv
from starlette import status
from datetime import timedelta, datetime
from internals.controller import Controller, CustomerAccount, RestaurantAccount, RiderAccount


load_dotenv()

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


def authenticate_user(username: str, password: str, controller: Controller):
    user = controller.search_instance_by_name(username)
    if user is None:
        return False
    if not bcrypt_context.verify(password, user.password):
        return False
    return user


def create_access_token(username: str, user_id: int, expires_delta: timedelta, controller: Controller):
    user_role = ''
    if not (controller.admin is None):
        user_role = 'admin'
    if isinstance(controller.search_instance_by_name(username), CustomerAccount):
        user_role = 'customer'
    if isinstance(controller.search_instance_by_name(username), RestaurantAccount):
        user_role = 'restaurant'
    if isinstance(controller.search_instance_by_name(username), RiderAccount):
        user_role = 'rider'
    encode = {'sub': username, 'id': user_id, 'role': user_role}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_customer(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: str = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None or (user_role != 'customer' and user_role != 'admin'):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')
        return {'username': username, 'id': user_id, 'role': user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')


async def get_current_restaurant(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: str = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None or (user_role != 'restaurant' and user_role != 'admin'):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')
        return {'username': username, 'id': user_id, 'role': user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')


async def get_current_admin(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: str = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None or user_role != 'admin':
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')
        return {'username': username, 'id': user_id, 'role': user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')


async def get_current_rider(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: str = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None or (user_role != 'rider' and user_role != 'admin'):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')
        return {'username': username, 'id': user_id, 'role': user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')


async def get_current_account(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: str = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None or (user_role != 'rider' and user_role != 'restaurant' and user_role != 'customer' and user_role != 'admin'):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')
        return {'username': username, 'id': user_id, 'role': user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')

user_dependency = Annotated[dict, Depends(get_current_customer)]
restaurant_dependency = Annotated[dict, Depends(get_current_restaurant)]
admin_dependency = Annotated[dict, Depends(get_current_admin)]
rider_dependency = Annotated[dict, Depends(get_current_rider)]
account_dependency = Annotated[dict, Depends(get_current_account)]