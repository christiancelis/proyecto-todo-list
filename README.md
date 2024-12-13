# proyecto-todo-list

## Analisis de codigo con SONARQUBE:
    
link:
[https://github.com/christiancelis/proyecto-todo-list/blob/master/backend/prueba%20-%20Overview%20-%20SonarQube%20Community%20Build.pdf] (Click aqui para ir al pd del analisis en sonarqube) 

   

# Tecnologias Usadas
    
    Frontend: Javascript, Html, Css.
    
    Backend: Phyton(Lenguaje), sqlAlchemy(ORM), FastApi(Framework WEB, Manejo Api).

# Descripcion del proyecto

## Aplicación de Gestión de Tareas
Esta es una aplicación desarrollada en Python que permite a los usuarios gestionar sus tareas diarias de forma sencilla y eficiente. Con esta herramienta, los usuarios pueden agregar, listar, completar y eliminar tareas, además de guardar y cargar su progreso utilizando archivos o una base de datos para garantizar la persistencia de los datos.

# Funcionalidades
### Agregar Tareas
1. Los usuarios pueden agregar nuevas tareas, proporcionando un título y una descripción.

2. Listar Tareas
Muestra todas las tareas creadas, indicando su estado (pendiente o completada).

3. Marcar Tareas como Completadas
Permite marcar una tarea como completada para un mejor seguimiento del progreso.

4. Eliminar Tareas
Opción para eliminar tareas completadas, manteniendo la lista organizada.

5. Interfaz
La aplicación puede ejecutarse mediante una interfaz gráfica o directamente desde la línea de comandos.

##  Requisitos Técnicos
Utiliza estructuras de datos como listas y diccionarios.
Maneja excepciones para evitar cierres inesperados.
Emplea módulos estándar de Python como json para importar y exportar tareas.
Integra una base de datos SQL (con preferencia por SQLAlchemy) para garantizar la persistencia de los datos.


## Inicializacion del proyecto
crear un entorno virtual phyton, Situarse dentro del directorio backend, e ir a configuracion de visual studio code, panel de comandos y escribir "crear entorno virtual" luego seleccionar venv.

## Dependencias del backend
    Las siguientes son las dependencias necesarias para el correcto funcionamiento del aplicativo.


          
  ```bash  
    pip install sqlalchemy
    pip install pymysql
    pip install fastapi
    pip install pydantic
    pip install uvicorn
  ```
## Instalacion de dependencias con requirement.txt
```bash  
    pip install -r requirements.txt
```

## Configuracion de la base de datos:

Crea un base de datos en workbench con el nombre:  phytondb
    
1. Configurar ruta de acceso a bd en el backend:

    cambia la siguiente ruta ubicada en backend/db/configdb con tu configuracion local de base de datos.

```phyton
engine = create_engine("mysql+pymysql://usuario:contraseña@localhost:3306/phytondb", echo=True)
```
  




## Comando de ejecucion backend

```bash
    uvicorn main:app --reload
```

## Ejecucion del frontend

Instalacion requerida: Extension de vs code "Live Server"
situarse en el directorio frontend y seleccionar en la parte inferior derecha de vs code el icono  "Go Live" .



