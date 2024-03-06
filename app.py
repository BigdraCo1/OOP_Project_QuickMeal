from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import menu, search, restaurant
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Authorization"]
)

app.include_router(menu.app)
app.include_router(search.app)
app.include_router(restaurant.app)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, log_level="info")