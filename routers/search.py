from fastapi import FastAPI, HTTPException, status

app = FastAPI()


@app.get("/restaurant", tags=['search'], status_code=status.HTTP_200_OK)
async def show():
    show_list = []
    for restaurant_acc in system_controller.restaurant_list:
        for restaurant in restaurant_acc.restaurant_list:
            restaurant_raw_attribute = vars(restaurant)
            restaurant_attributes = {key: value for key, value in restaurant_raw_attribute.items() if
                                     key != '_Restaurant__owner'}
            show_list.append(restaurant_attributes)
    return show_list


@app.get("/{key}", tags=['search'], status_code=status.HTTP_200_OK)
async def show_search(key: str):
    if isinstance(system_controller.search_menu_and_restaurant(key), str):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Restaurant or Menu with {key} not found")
    return system_controller.search_menu_and_restaurant(key)
