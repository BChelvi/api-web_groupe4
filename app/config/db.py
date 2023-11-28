from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# connexion à la base de donnée
connector = "mysql+pymysql"
user = "root"
password = "root"
host = "localhost"
database = "librairie"

engine = create_engine(f"{connector}://{user}:{password}@{host}/{database}")

Session = sessionmaker(bind=engine)
# Fonction pour donner la connexion à la BDD aux routes.
def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()
