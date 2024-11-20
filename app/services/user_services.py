from sqlalchemy.orm import Session
from app.models.users import Users
from app.schemas.users import UserCreate
from app.configs.security import hash_password


def create_user(db: Session, user_data: UserCreate):
    hashed_password = hash_password(user_data.password)
    db_user = Users(username=user_data.username,
                    hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_name(db: Session, username: str):
    return db.query(Users).filter(Users.username == username).first()
