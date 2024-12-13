import getTasks from "./models/get.js";
import postTask from "./models/post.js";
import deleteTask from "./models/delete.js";
import patchTask from "./models/patch.js";

const butonform = document.querySelector(".enviarTarea");

const form = document.getElementById("fm1");
form.addEventListener("click", (e) => {
  e.preventDefault();
  e.stopPropagation();
});

butonform.addEventListener("click", async (e) => {
  const form = document.getElementById("fm1");

  const data = new FormData(form).entries();
  let datos = Object.fromEntries(data);
  console.log(datos);

  let dato = {
    nombre: datos.name,
    descripcion: datos.description,
  };
  const retorno = await postTask(dato);
  location.reload();
  console.log(retorno);
  e.preventDefault();
  e.stopPropagation();
});


function pintarTareas(b) {
  const contenedorTareas = document.getElementById("taskcontainer");
  let html = "";
  for (let i = 0; i < b.length; i++) {
    html += `
            <div class="container" id="${b[i].id}">
                <div class="checkcontainer a"> 
                    <input type="checkbox" class="combo" ${
                      b[i].estado === "Completado" ? "checked" : ""
                    }>
                </div>
                <div class="cont a">
                    <h3>${b[i].nombre}</h3>
                    <p>${b[i].descripcion}</p>
                </div>
                <div class="estadoTarea a">
                    <p>(${b[i].estado})</p>
                </div>
                <div class="buttoncontainer a">
                    <button id="botonEliminar">Eliminar</button>
                </div>
            </div>
        `;
  }
  contenedorTareas.innerHTML = html;
}

function eliminarTareas(buttonEliminar) {
  if (buttonEliminar) {
    buttonEliminar.forEach((buttonE) => {
      buttonE.addEventListener("click", async (e) => {
        const elementoId = e.target.parentElement.parentElement.id;
        console.log(elementoId);
        const resp = await deleteTask(elementoId);
        console.log(resp);
        location.reload();
      });
    });
  }
}

async function estadoTarea(check) {
  if (check) {
    check.forEach((checkb) => {
      checkb.addEventListener("change", async (e) => {
        const estadoe = e.target.checked;
        const elementParent = e.target.parentElement.parentElement;
        const elementId = elementParent.id;
        const data = {
          estado: estadoe ? "Completado" : "Pendiente",
        };
        try {
          const resp = await patchTask(elementId, data);
          e.target.checked = estadoe;
          const targetChild = elementParent.children[2];
          if (targetChild) {
            targetChild.textContent = `(${data.estado})`;
            data.estado == "Completado"
              ? (targetChild.style.color = "green")
              : (targetChild.style.color = "black");
          }
        } catch (error) {
          console.error("Error al actualizar la tarea:", error);
          e.target.checked = !estadoe;
          alert(
            "Hubo un error al actualizar la tarea. Por favor, inténtalo de nuevo."
          );
        }
        e.preventDefault();
        e.stopPropagation();
      });
    });
  }
}

async function main() {
  const a = await getTasks();
  const b = a;

  pintarTareas(b.tareas);
  const btnsEliminar = document.querySelectorAll("#botonEliminar");
  eliminarTareas(btnsEliminar);
  console.log();
  const checkbx = document.querySelectorAll(".combo");
  estadoTarea(checkbx);
}

main();
