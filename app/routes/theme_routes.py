from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from config.db import get_db
from models.theme import Theme
# from schemas.client_schema import ClientSchemaOut,ClientSchema
from schemas.theme_schema import ThemeSchema,ThemeSchemaOut

router_theme = APIRouter(
    tags=["theme"],
    prefix="/theme"
    )   

#CREATE
@router_theme.post("/",response_model=ThemeSchemaOut, status_code=status.HTTP_201_CREATED)
async def add_theme(theme: ThemeSchema, db : Session = Depends(get_db)):
    theme_db = Theme(**theme.dict())
    db.add(theme_db)
    db.commit()
    return ThemeSchemaOut.from_orm(theme_db)

@router_theme.get("/")
async def list_themes(db : Session = Depends(get_db)):
    stmt = select(Theme)
    liste=[]
    for theme in db.scalars(stmt):
        liste.append(theme)
    return liste