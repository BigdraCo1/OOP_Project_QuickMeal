from fastapi import APIRouter, HTTPException, status
from constants.controller import system

app = APIRouter(prefix="/search", tags=["search"], responses={404: {"description": "Not found"}})


@app.get("/restaurant", status_code=status.HTTP_200_OK)
async def show():
    show_list = []
    for restaurant_acc in system.restaurant_account_list:
        for restaurant in restaurant_acc.restaurant_list:
            restaurant_raw_attribute = vars(restaurant)
            restaurant_attributes = {
                key: value
                for key, value in restaurant_raw_attribute.items()
                if key != '_Restaurant__owner'
            }

            show_list.append(restaurant_attributes)
    return show_list


@app.get("/{key}", status_code=status.HTTP_200_OK)
async def show_search(key: str):
    if isinstance(system.search_menu_and_restaurant(key), str):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Restaurant or Menu with {key} not found")
    return system.search_menu_and_restaurant(key)
