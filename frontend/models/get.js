export default async function getTasks() {
    const url=  `http://127.0.0.1:8000/api/tareas`;
    try {
        const response = await fetch(url);
        return await response.json();
    } catch (error) {
        console.error('Error al obtener las tareas:', error);
        return [];
    }
}