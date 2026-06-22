from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.api.food import router as food_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Nutrition Tracker",
        version="0.1.0",
    )
    app.include_router(food_router)
    app.include_router(auth_router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/")
    def root():
        return {"message": "Up and running!"}

    return app
