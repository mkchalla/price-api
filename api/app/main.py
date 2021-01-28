import os
from datetime import datetime, timedelta
from typing import List
from mimetypes import guess_type
import shutil

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi import Response, File, UploadFile
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

from . import actions, models, schemas
from .db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

MEDIA_ROOT_DIR = os.path.abspath('./media')

app = FastAPI()

origins = [
    "http://localhost:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

ACCESS_TOKEN_EXPIRE_MINUTES = 30


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")


# @app.post("/items/", response_model=schemas.Item)
# def create_item_for_user(
#     item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return actions.create_user_item(db=db, item=item)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = actions.get_items(db, skip=skip, limit=limit)
#     return items



async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, actions.SECRET_KEY, algorithms=[actions.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = username
    except JWTError:
        raise credentials_exception
    user = actions.get_user(db, username=token_data)
    if user is None:
        raise credentials_exception
    return user

@app.post("/api/v1/login", response_model=schemas.TokenUser)
async def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = actions.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = actions.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "username": user.username, "token_type": "bearer"}


@app.get("/users/me/")
async def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user


@app.post("/api/v1/signup", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return actions.create_user(db=db, user=user)

# @app.get("/users/me/items/")
# async def read_own_items(current_user: schemas.User = Depends(get_current_user)):
#     return [{"item_id": "Foo", "owner": current_user.username}]

@app.get("/api/v1/products", response_model=List[schemas.ProductInDB])
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return actions.get_products(db=db)

@app.get("/api/v1/products/{product_id}", response_model=schemas.ProductInDB)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return actions.get_product(db, product_id)

@app.post("/api/v1/products", response_model=schemas.ProductBase)
def create_product(name: str, description: str, file: UploadFile = File(...), current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):

    with open("./media/images/" + file.filename, "wb") as image:
        shutil.copyfileobj(file.file, image)

    image_url = str(file.filename)

    product = schemas.ProductBase(name=name, description=description)

    return actions.create_product(db, product, image_url=image_url)


@app.get("/media/images/{image_file}", response_model=schemas.ProductBase)
def get_image(image_file: str):
    image_file_path = os.path.join(MEDIA_ROOT_DIR, 'images', image_file)
    
    print(image_file_path)
    #filename = './site/' + filename

    if not os.path.isfile(image_file_path):
        return Response(status_code=404)

    # with open(image_file_path) as f:
    #     content = f.read()

    # content_type, _ = guess_type(image_file_path)
    #return Response(content, media_type=content_type)

    return FileResponse(image_file_path)