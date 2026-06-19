from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.db.food import FoodEntry
from app.schemas.food import FoodCreate, FoodResponse

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


@router.get(
    "/food",
    response_model=list[FoodResponse],
)
def get_food(
    db: Session = Depends(get_db),
):
    return db.query(FoodEntry).all()
