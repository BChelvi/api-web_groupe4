from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from config.db import get_db
from models.client import Client
from schemas.client_schema import ClientSchemaOut,ClientSchema

router_client = APIRouter(
    tags=["client"],
    prefix="/client"
    )   

#CREATE
@router_client.post("/", response_model=ClientSchemaOut,status_code=status.HTTP_201_CREATED)
async def add_client(client: ClientSchema, db : Session = Depends(get_db)):
    client_db = Client(**client.dict())
    db.add(client_db)
    db.commit()
    return ClientSchemaOut.from_orm(client_db)

@router_client.get("/")
async def list_clients(db : Session = Depends(get_db)):
    stmt = select(Client)
    liste=[]
    for client in db.scalars(stmt):
        liste.append(client)
    return liste

#READ
@router_client.get("/{client_id}",response_model=ClientSchemaOut)
async def get_client(client_id: int, db : Session = Depends(get_db)):
    stmt = select(Client).where(Client.id_client==client_id)
    client = db.scalar(stmt)
    return client

#UPDATE
@router_client.patch("/{client_id}",response_model=ClientSchemaOut)
async def change_client(client: ClientSchema, client_id:int,db : Session = Depends(get_db) ):
    stmt = select(Client).where(Client.id_client==client_id)
    result = db.scalar(stmt)
    if not result:
        raise HTTPException(status_code=404, detail="Client not found")
    for key, value in client.dict().items():
        setattr(result,key,value)
    db.commit()
    

    return result

#DELETE
@router_client.delete("/{client_id}")
async def delete_client(client:ClientSchema,client_id:int, db : Session = Depends(get_db)):
    client = db.get(Client,client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    db.delete(client)
    db.commit()
    return {"ok": True}
    
        
        
    





#DELETE