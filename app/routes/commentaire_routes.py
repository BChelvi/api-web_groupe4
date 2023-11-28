from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from config.db import get_db
from models.commentaire import Commentaire
from schemas.commentaire_schema import CommentaireSchema, CommentaireSchemaOut,CommentaireSchemaClient
from models.client import Client

router_commentaire = APIRouter(
    tags=["commentaire"],
    prefix="/commentaire"
    )   

#CREATE
@router_commentaire.post("/", response_model=CommentaireSchemaOut,status_code=status.HTTP_201_CREATED)
async def add_commentaire(commentaire: CommentaireSchema, db : Session = Depends(get_db)):
    commentaire_db = Commentaire(**commentaire.dict())
    db.add(commentaire_db)
    db.commit()
    return CommentaireSchemaOut.from_orm(commentaire_db)

@router_commentaire.get("/")
async def list_commentaire(db : Session = Depends(get_db)):
    stmt = select(Commentaire)
    liste=[]
    for commentaire in db.scalars(stmt):
        liste.append(commentaire)
    return liste

#READ
@router_commentaire.get("/{commentaire_id}",response_model=CommentaireSchemaClient)
async def get_commentaire_by_id(commentaire_id: int, db : Session = Depends(get_db)):
    stmt = select(Commentaire).where(Commentaire.id_commentaire==commentaire_id).join(Client)
    commentaire = db.scalar(stmt)
    return commentaire

@router_commentaire.get("/liste_by_clients/{client_id}")
async def list_commentaire_by_client(client_id: int, db : Session = Depends(get_db)):
    stmt = (
            select(Commentaire)
            .where(Commentaire.id_client == client_id)
        )
    result = db.scalars(stmt).fetchall()
    return result


@router_commentaire.get("/liste_by_ouvrage/{ouvrage_id}")
async def list_commentaire_by_ouvrage(ouvrage_id: int, db : Session = Depends(get_db)):
    stmt = select(Commentaire).where(Commentaire.id_ouvrage==ouvrage_id)
    liste=[]
    for commentaire in db.scalars(stmt):
        liste.append(commentaire)
    return liste
