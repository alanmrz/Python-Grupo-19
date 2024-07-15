import mysql.connector

midba = mysql.connector.connect(host= "localhost", user= "root", password="", port=3306, database = "estilovivo")

cursor = midba.cursor()

sql = "INSERT INTO productos (nombre, img, precio, categoria) VALUES (%s, %s, %s, %s)"
valores = [
    ('Armario blanco con ropero y estantes ANTONIN', 1, 554000, 1),
    ('Armario industrail mango INDUSTRIA', 2, 872000, 1),
    ('Armario colgador nórdico blanco y madera clara KELMA', 3, 663000, 1),
    ('Armario nórdico acabado roble claro MAHE', 4, 790000, 1),
    ('Armario nórdico con ropero y estantes blanco y madera ELIE', 5, 495000, 1)
]
cursor.executemany(sql, valores)

midba.commit()

print(cursor.rowcount)

cursor.close()
midba.close()

# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hola_mundo():
#     return "flask"

# # app.add_url_rule('/', 'hello', hola_mundo)

# @app.route('/24148')
# def hola_24148():
#     return "flask 24148"

# if __name__ == '__main__':
#     app.run()