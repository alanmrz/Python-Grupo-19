let contenedor = document.getElementById("contenedorProductos");
let productos = []

async function cargarProductos() {
    try {
        let response = await fetch('https://alanmrz94.pythonanywhere.com/productos');
        if (!response.ok) {
            throw new Error('Error al obtener los productos');
        }
        productos = await response.json();
        productos.forEach(producto => {
            contenedor.innerHTML += `
                <div class="card">
                    <div class="imagen">
                        <a href="./productos/producto${producto.id}.html">
                            <img src="/static/imagenes/0${producto.img}.jpg" alt="">
                            <img src="/static/imagenes/0${producto.img}.jpg" alt="">
                        </a>
                    </div>
                    <p class="titulo-producto">${producto.nombre}</p>
                    <p class="precio">$ ${producto.precio}</p>
                </div>`;
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

cargarProductos();

let search = document.getElementById("buscarProd");

search.addEventListener('input', () => {
    let filtro = search.value.toLowerCase();
    contenedor.innerHTML = "";
    if (filtro == "") {
        cargarProductos();
    } else {
        productos.forEach(producto => {
            if (producto.nombre.toLowerCase().includes(filtro)) {
                contenedor.innerHTML += `
                    <div class="card">
                        <div class="imagen">
                            <a href="./productos/producto${producto.id}.html">
                                <img src="./static/imagenes/0${producto.img}" alt="">
                            </a>
                        </div>
                        <p class="titulo-producto">${producto.nombre}</p>
                        <p class="precio">$ ${producto.precio}</p>
                    </div>`;
            }
        });
    }
});
