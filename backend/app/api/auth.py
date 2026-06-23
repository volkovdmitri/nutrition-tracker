from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.auth.jwt import create_access_token, decode_access_token
from app.auth.security import hash_password, verify_password
from app.db.dependencies import get_db
from app.db.user import User
from app.schemas.user import UserCreate, UserLogin

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
router = APIRouter(tags=["Auth"])


@router.post("/auth/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    password_hash = hash_password(user.password)
    db_user = User(username=user.username, email=user.email, password_hash=password_hash)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"id": db_user.id, "email": db_user.email}


@router.post("/auth/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="User not found")

    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(db_user.id)})

    return {"access_token": token, "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_access_token(token)

    if not payload:
        raise HTTPException(status_code=401)

    user_id = payload.get("sub")

    user = db.query(User).get(user_id)

    if not user:
        raise HTTPException(status_code=401)

    return user
