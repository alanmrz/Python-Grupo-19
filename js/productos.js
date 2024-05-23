let contenedor = document.getElementById("contenedorProductos")
const muebles = [
                    {
                    "nombre":"Armario blanco con ropero y estantes ANTONIN",
                    "img": 1,
                    "precio":554.000
                    },
                    {
                    "nombre":"Armario industrail mango INDUSTRIA",
                    "img": 2,
                    "precio":872.000
                    },
                    {
                    "nombre":"Armario colgador nórdico blanco y madera clara KELMA",
                    "img": 3,
                    "precio":663.000
                    },
                    {
                    "nombre":"Armario nórdico acabado roble claro MAHE",
                    "img": 4,
                     "precio":790.000
                    },
                    {
                    "nombre":"Armario nórdico con ropero y estantes blanco y madera ELIE",
                    "img": 5,
                    "precio":495.000
                    }
                ]

// contenedor.innerHTML= ""

muebles.forEach(mueble => {
                            contenedor.innerHTML+= 
                            `<div class="card">
                            <div class="imagen">
                                <a href="./productos/producto${mueble.img}.html">
                                    <img src="./img/Producto ${mueble.img}/0${muebles[0].img}.jpg" alt="">
                                    <img src="./img/Producto ${mueble.img}/0${muebles[0].img+1}.jpg" alt="">
                                </a>
                            </div>
                            <p class="titulo-producto">${mueble.nombre}</p>
                            <p class="precio">$ ${mueble.precio}.000</p>
                        </div>`
                        }
                        )