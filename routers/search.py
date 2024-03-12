from fastapi import APIRouter, HTTPException, status
from constants.controller import system

app = APIRouter(prefix="/search", tags=["search"], responses={404: {"description": "Not found"}})


@app.get("/menu_and_restaurant/{key}", status_code=status.HTTP_200_OK)
async def show_search(key: str):
    if isinstance(system.search_menu_and_restaurant(key), str):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Restaurant or Menu with {key} not found")
    return system.search_menu_and_restaurant(key)
