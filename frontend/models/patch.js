export default function patchTask(id,objeto) {
    const url=  `http://127.0.0.1:8000/api/tareas/${id}`;
    fetch(url, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json ;charset=UTF-8",
      },
      body: JSON.stringify(objeto),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.error(error);
      });
  }