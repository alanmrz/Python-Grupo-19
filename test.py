# import mysql.connector

# midba = mysql.connector.connect(host= "localhost", user= "root", password="", port=3307)

# cursor = midba.cursor()

# cursor.execute("SHOW DATABASES")
# for i in cursor:
#     print(i)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hola_mundo():
    return "flask"

# app.add_url_rule('/', 'hello', hola_mundo)

@app.route('/24148')
def hola_24148():
    return "flask 24148"

if __name__ == '__main__':
    app.run()