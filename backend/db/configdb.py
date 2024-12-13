from sqlalchemy import create_engine, Sequence, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("mysql+pymysql://usuario:contraseña@localhost:3306/phytondb", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()