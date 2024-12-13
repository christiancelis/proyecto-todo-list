from sqlalchemy import Sequence, Column, Integer, String

from db.configdb import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column( Integer, Sequence("task_id_sequence"), primary_key=True)
    name = Column(String(100))
    description = Column(String(255))
    state = Column(String(20), default="Pendiente")
    