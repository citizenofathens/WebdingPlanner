

from sqlalchemy.orm import Session
from wedding.backend.db import schemas


def get_user(db: Session , username: str ):
    return db.query(schemas.User).filter(schemas.User.username == username).first()
