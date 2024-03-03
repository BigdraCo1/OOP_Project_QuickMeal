from fastapi import APIRouter, HTTPException, status
from databases import database

app = APIRouter()


@app.delete("/{restaurant}", tags=['Delete'], status_code=status.HTTP_204_NO_CONTENT)
async def remove_restaurant(restaurant: str):
    if database.system.remove_restaurant(restaurant) != 'Success':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no restaurant name : {restaurant}")