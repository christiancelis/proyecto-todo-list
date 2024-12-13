export default function deleteTask(id) {
    const url = `http://127.0.0.1:8000/api/tareas/${id}`;
    fetch(url, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json", 
      },
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Error al eliminar la tarea");
        }
        return response.json();
      })
      .then((json) => {
        console.log("Tarea eliminada:", json);
        
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }