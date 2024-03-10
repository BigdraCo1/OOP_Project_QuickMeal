from constants.controller import system
from fastapi import APIRouter, HTTPException, status
from utils.dependencies import rider_dependency

app = APIRouter(prefix='/rider')

@app.get("/{rider_id}/show/recieved_order_list", tags = ["Rider"])
async def show_request_order_list(rider_id: str, rider : rider_dependency) -> dict:
    if rider is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {
        "data": system.show_request_order(rider_id)
    }
    
@app.get("/{rider_id}/show/requested_order_list", tags = ["Rider"])
async def show_receive_order_list(rider_id: str, rider : rider_dependency) -> dict:
    if rider is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {
        "data": system.show_receive_order(rider_id)
    }
    
@app.get("/{rider_id}/show/finished_order_list", tags = ["Rider"])
async def show_finished_order_list(rider_id: str, rider : rider_dependency) -> dict:
    if rider is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {
        "data": system.show_finished_order(rider_id)
    }
    
@app.put("/rider/{rider_id}/accept/{order_id}", tags = ["Rider"])
async def accept_rider_order(rider_id: str, order_id: str, rider : rider_dependency) -> dict:
    if rider is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {
        "data": system.accept_order_by_rider(rider_id, order_id)
    }
    
@app.put("/rider/{rider_id}/deny/{order_id}", tags = ["Rider"])
async def deny_rider_order(rider_id: str, order_id: str, rider : rider_dependency) -> dict:
    if rider is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {
        "data": system.deny_order_by_rider(rider_id, order_id)
    }
    
@app.put("/rider/{rider_id}/receive/{order_id}", tags = ["Rider"])
async def receive_rider_order(rider_id: str, order_id: str, rider : rider_dependency) -> dict:
    if rider is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {
        "data": system.receive_order_from_rider(rider_id, order_id)
    }
    
@app.put("/{rider_id}/delivere/{order_id}", tags = ["Rider"])
async def deliver_rider_order(rider_id: str, order_id: str, rider : rider_dependency) -> dict:
    if rider is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {
        "data": system.deliver_order(rider_id, order_id)
    }