from fastapi import APIRouter, HTTPException, status
from constants.controller import system
from utils.dependencies import admin_dependency

app = APIRouter(prefix='/admin')
@app.delete("/rider_approval_list/{rider}/deny")
async def deny_rider_in_approval_list(rider_username: str , admin : admin_dependency):
    if admin is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.remove_rider_in_approve_list(rider_username)


@app.delete("/rider_approval_list/{rider}/accept")
async def accept_rider_in_approval_list(rider_username: str, admin : admin_dependency):
    if admin is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.approve_rider(rider_username)


@app.delete("/restaurant_approval_list/{restaurant}/deny")
async def deny_restaurant_in_approval_list(restaurant_name: str, admin : admin_dependency):
    if admin is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.remove_restaurant_in_approve_list(restaurant_name)


@app.delete("/restaurant_approval_list/{restaurant}/accept")
async def accept_restaurant_in_approval_list(restaurant_name: str, admin : admin_dependency):
    if admin is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.approve_restaurant(restaurant_name)

@app.get("/rider_approval_list")
async def show_rider_in_approval_list(admin : admin_dependency):
    if admin is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_rider_approval_list()

@app.get("/restaurant_approval_list")
async def show_restaurant_in_approval_list(admin : admin_dependency):
    if admin is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_restaurant_approval_list()
