from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.db.food import FoodEntry
from app.schemas.food import FoodCreate, FoodResponse, TextRequest
from app.services.llm import parse

router = APIRouter()


@router.post(
    "/food",
    response_model=FoodResponse,
)
def create_food(
    food: FoodCreate,
    db: Session = Depends(get_db),
):
    item = FoodEntry(
        food_name=food.food_name,
        calories=food.calories,
    )

    db.add(item)

    db.commit()

    db.refresh(item)

    return item


@router.post(
    "/text",
    response_model=FoodResponse,
)
def create_food_from_text(
    req: TextRequest,
    db: Session = Depends(get_db),
):
    result = parse(req.text)
    try:
        food_name = result.get("food_name")
        calories = result.get("calories")
    except Exception:
        food_name = None
        calories = None

    if food_name is None:
        return {"status": "error", "message": "Could not parse food_name"}
    if calories is None:
        return {"status": "error", "message": "Could not parse calories"}

    item = FoodEntry(
        food_name=food_name,
        calories=calories,
    )

    db.add(item)

    db.commit()

    db.refresh(item)

    return item


@router.get(
    "/food",
    response_model=list[FoodResponse],
)
def get_food(
    db: Session = Depends(get_db),
):
    return db.query(FoodEntry).all()
