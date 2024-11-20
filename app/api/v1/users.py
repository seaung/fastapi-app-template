from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.configs.databases import get_db
from app.schemas.users import UserResponse, UserCreate
from app.services.user_services import create_user, get_user_by_name


user_router = APIRouter()


@user_router.post('/user/create', response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    ok = get_user_by_name(db, user.username)
    if ok:
        raise HTTPException(status_code=400, detail='username already taken')
    return create_user(db, user)


@user_router.get('/user/get', response_model=UserResponse)
def get_user(username: str, db: Session = Depends(get_db)):
    user = get_user_by_name(db, username)
    if not user:
        raise HTTPException(status_code=400, detail='user not found')
    return user
