from typing import Optional
from sqlalchemy import String,ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from models.client import Client
from models.ouvrage import Ouvrage


class Commentaire(Base):
    __tablename__ = "commentaire"
    id_commentaire: Mapped[int] = mapped_column(primary_key=True)
    
    id_client : Mapped[int] = mapped_column(ForeignKey(Client.id_client))
    client: Mapped["Client"] = relationship(back_populates="commentaires")
    
    id_ouvrage : Mapped[int] = mapped_column(ForeignKey(Ouvrage.id_ouvrage))
    ouvrage: Mapped["Ouvrage"] = relationship(back_populates="commentaires")
    
    date_publication_commentaire : Mapped[Date] = mapped_column(Date)
    auteur_commentaire : Mapped[str] = mapped_column(String(255))
    titre_commentaire : Mapped[str] = mapped_column(String(255))