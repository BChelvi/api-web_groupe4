from fastapi import FastAPI
from routes.client_routes import router_client
from routes.ouvrage_routes import router_ouvrage
from routes.theme_routes import router_theme
from routes.commentaire_routes import router_commentaire
from models.base import Base
from config.db import engine

app = FastAPI()
app.include_router(router_client)
app.include_router(router_ouvrage)
app.include_router(router_theme)
app.include_router(router_commentaire)
Base.metadata.create_all(engine)