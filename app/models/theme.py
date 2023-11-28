from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Theme(Base):
    __tablename__ = "theme"
    id_theme: Mapped[int] = mapped_column(primary_key=True)
    nom_theme : Mapped[str] = mapped_column(String(255))