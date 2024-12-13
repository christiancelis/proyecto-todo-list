from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models.Task import Task
from db.configdb import get_db_session
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from db.configdb import Base,engine


class Tarea(BaseModel):
    nombre: str
    descripcion: str
    estado: str = "Pendiente"


class TareaRespuesta(BaseModel):
    id: int
    nombre: str
    descripcion: str
    estado: str


class uTarea(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    estado: Optional[str] = None
    
try:
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas exitosamente.")
except Exception as e:
    print(f"Error al crear las tablas: {e}")


app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Métodos permitidos (GET, POST, etc.)
    allow_headers=["*"],  # Encabezados permitidos
)


@app.get("/")
def index():
    return "Hola, mundo"


@app.get("/api/tareas")
def listar_tareas(session: Session = Depends(get_db_session)):
    tasks = session.query(Task).all()
    if not tasks:
        return {"message": "No hay tareas disponibles"}

    # Usamos list comprehension para simplificar el código
    tareas = [{"id": i.id, "nombre": i.name, "descripcion": i.description, "estado": i.state} for i in tasks]
    return {"tareas": tareas}


@app.post("/api/tareas", response_model=TareaRespuesta)
def agregar_tarea(tarea: Tarea, session: Session = Depends(get_db_session)):
    new_task = Task(name=tarea.nombre, description=tarea.descripcion, state=tarea.estado)
    session.add(new_task)
    session.commit()
    session.refresh(new_task)  # Recargamos el objeto para obtener el id generado
    return {"id": new_task.id, "nombre": new_task.name, "descripcion": new_task.description, "estado": new_task.state}


@app.patch("/api/tareas/{id}", response_model=TareaRespuesta)
def editar_tarea(id: int, tarea: uTarea, session: Session = Depends(get_db_session)):
    tarea_a_editar = session.query(Task).filter(Task.id == id).first()

    if not tarea_a_editar:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    # Actualizamos solo los campos proporcionados
    if tarea.nombre:
        tarea_a_editar.name = tarea.nombre
    if tarea.descripcion:
        tarea_a_editar.description = tarea.descripcion
    if tarea.estado:
        tarea_a_editar.state = tarea.estado

    session.commit()
    session.refresh(tarea_a_editar)  # Recargamos el objeto para obtener el id actualizado

    return {"id": tarea_a_editar.id, "nombre": tarea_a_editar.name, "descripcion": tarea_a_editar.description, "estado": tarea_a_editar.state}


@app.delete("/api/tareas/{id}")
def eliminar_tarea(id: int, session: Session = Depends(get_db_session)):
    tarea_a_eliminar = session.query(Task).filter(Task.id == id).first()
    if not tarea_a_eliminar:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    try:
        session.delete(tarea_a_eliminar)
        session.commit()
    except Exception as e:
        session.rollback()  # Si ocurre un error, se revierte la transacción
        raise HTTPException(status_code=500, detail=f"Error al eliminar la tarea: {str(e)}")

    return {
        "message": "Tarea eliminada con éxito", 
        "id": tarea_a_eliminar.id, 
        "nombre": tarea_a_eliminar.name,
        "descripcion": tarea_a_eliminar.description,
        "estado": tarea_a_eliminar.state
    }
