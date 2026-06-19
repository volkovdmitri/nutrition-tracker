from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.food import router as food_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Nutrition Tracker",
        version="0.1.0",
    )
    app.include_router(food_router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "http://localhost:5174",
            "http://frontend:5173",
            "http://frontend:5174",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/")
    def root():
        return {"message": "Hello World"}

    return app
