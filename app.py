from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from werkzeug.utils import secure_filename
import os
import time

app = Flask(__name__)
CORS(app)

class Catalogo:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            img VARCHAR(255),
            precio INT NOT NULL,
            categoria INT NOT NULL)''')
        self.conn.commit()

    def listar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        return self.cursor.fetchall()

    def consultar_producto(self, id):
        self.cursor.execute(f"SELECT * FROM productos WHERE id = {id}")
        return self.cursor.fetchone()

    def agregar_producto(self, nombre, precio, categoria):
        sql = "INSERT INTO productos (nombre, precio, categoria) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (nombre, precio, categoria))
        self.conn.commit()
        return self.cursor.lastrowid

    def modificar_producto(self, id, nombre, img, precio, categoria):
        sql = "UPDATE productos SET nombre = %s, img = %s, precio = %s, categoria = %s WHERE id = %s"
        self.cursor.execute(sql, (nombre, img, precio, categoria, id))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def eliminar_producto(self, id):
        self.cursor.execute(f"DELETE FROM productos WHERE id = {id}")
        self.conn.commit()
        return self.cursor.rowcount > 0

catalogo = Catalogo(host='localhost', user='root', password='', database='estilovivo')
ruta_destino = './static/imagenes/'

@app.route("/productos", methods=["GET"])
def listar_productos():
    return jsonify(catalogo.listar_productos())

@app.route("/productos/<int:id>", methods=["GET"])
def mostrar_producto(id):
    producto = catalogo.consultar_producto(id)
    return jsonify(producto) if producto else ("Producto no encontrado", 404)

@app.route("/productos", methods=["POST"])
def agregar_producto():
    nombre = request.form['nombre']
    precio = request.form['precio']
    categoria = request.form['categoria']
    
    
    nuevo_id = catalogo.agregar_producto(nombre, precio, categoria)
    if nuevo_id:
        
        return jsonify({"mensaje": "Producto agregado correctamente.", "id": nuevo_id,}), 201
    else:
        return jsonify({"mensaje": "Error al agregar el producto."}), 500

@app.route("/productos/<int:id>", methods=["PUT"])
def modificar_producto(id):
    nombre = request.form.get("nombre")
    precio = request.form.get("precio")
    categoria = request.form.get("categoria")
    nombre_imagen = catalogo.consultar_producto(id)["img"]
    if 'img' in request.files:
        imagen = request.files['img']
        nombre_imagen = secure_filename(imagen.filename)
        nombre_imagen = f"{os.path.splitext(nombre_imagen)[0]}_{int(time.time())}{os.path.splitext(nombre_imagen)[1]}"
        imagen.save(os.path.join(ruta_destino, nombre_imagen))
    if catalogo.modificar_producto(id, nombre, nombre_imagen, precio, categoria):
        return jsonify({"mensaje": "Producto modificado"}), 200
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 403

@app.route("/productos/<int:id>", methods=["DELETE"])
def eliminar_producto(id):
    producto = catalogo.consultar_producto(id)
    if producto:
        ruta_imagen = os.path.join(ruta_destino, producto['img'])
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)
        if catalogo.eliminar_producto(id):
            return jsonify({"mensaje": "Producto eliminado"}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar el producto"}), 500
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
