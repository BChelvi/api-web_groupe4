from pydantic import BaseModel

class ThemeSchema(BaseModel):
    nom_theme: str

    class Config:
        orm_mode = True
        from_attributes = True

class ThemeSchemaIn(ThemeSchema):
    pass

class ThemeSchemaOut(ThemeSchema):
    id_theme: int