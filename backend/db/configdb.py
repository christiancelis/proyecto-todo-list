from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError

db_name = "phytondb"
url="mysql+pymysql://user:password@localhost:3306"
urlc = f'{url}/{db_name}'

server_engine = create_engine(f'{url}')
try:
    with server_engine.connect() as connection:
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
    print(f"Base de datos '{db_name}' creada exitosamente.")
except OperationalError as e:
    print(f"Error al crear la base de datos: {e}")
    
print(urlc)

engine = create_engine(f'{urlc}', echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
        


