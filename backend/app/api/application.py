from fastapi import FastAPI

from app.api.food import router as food_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Nutrition Tracker",
        version="0.1.0",
    )
    app.include_router(food_router)

    @app.get("/")
    def root():
        return {"message": "Hello World"}

    return app
