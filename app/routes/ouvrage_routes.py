from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from config.db import get_db
from models.ouvrage import Ouvrage
from schemas.ouvrage_schema import OuvrageSchemaOut,OuvrageSchema

router_ouvrage = APIRouter(
    tags=["ouvrage"],
    prefix="/ouvrage"
    )   

#CREATE
@router_ouvrage.post("/", response_model=OuvrageSchemaOut,status_code=status.HTTP_201_CREATED)
async def add_ouvrage(ouvrage: OuvrageSchema, db : Session = Depends(get_db)):
    ouvrage_db = Ouvrage(**ouvrage.dict())
    db.add(ouvrage_db)
    db.commit()
    return OuvrageSchemaOut.from_orm(ouvrage_db)

@router_ouvrage.get("/")
async def list_ouvrages(db : Session = Depends(get_db)):
    stmt = select(Ouvrage)
    liste=[]
    for ouvrage in db.scalars(stmt):
        liste.append(ouvrage)
    return liste