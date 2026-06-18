from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="Nutrition Tracker",
        version="0.1.0",
    )

    @app.get("/")
    def root():
        return {"message": "Hello World"}

    return app
