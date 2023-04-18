from datetime import timedelta, datetime


from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from wedding.backend.apis.domain.user import user_crud, user_schema
from wedding.backend.apis.domain.user.user_crud import pwd_context

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
SECRET_KEY = "a12e4d7e64ea22cb01f62b0e27b5e5df1756c91656ea050cdf9daef8303cb4be"
ALGORITHM = "HS256"

router = APIRouter()

@router.post("/login",responses_model=user_schema.Token)
def login_for_access_token(form_data : OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(get_db)):
    # check user and password
    user = user_crud.get_user(db, form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail="Incorrect username or password",
          headers={"WWW-Authenticate": "Bearer"},
        )

    # make access token
    data = {
        "sub" : user.username,
        "exp" : datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token" : access_token,
        "token_type" : "bearer",
        "username" : user.username
    }







