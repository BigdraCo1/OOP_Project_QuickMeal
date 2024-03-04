from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import menu, search, restaurant, order_detail, cancel
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
app.include_router(order_detail.app)
app.include_router(cancel.app)


