from pydantic import BaseModel
from datetime import date

class CommentaireSchema(BaseModel):
    id_client : int
    id_ouvrage : int
    date_publication_commentaire : date
    auteur_commentaire : str
    titre_commentaire : str
    
    class Config:
        orm_mode = True
        from_attributes = True

class CommentaireSchemaIn(CommentaireSchema):
    pass

class CommentaireSchemaOut(CommentaireSchema):
    id_commentaire: int
    
class CommentaireSchemaClient(CommentaireSchema):
    id_commentaire: int
    adresse_livraison_client : str