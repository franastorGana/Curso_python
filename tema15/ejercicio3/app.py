'''
A partir del siguiente diccionario guardado en memoria, con valor inicial:

 

Pero que lo coja de una sql lite

Construir un API RestFul con Flask que interactúe con él, a través de los siguientes tres endpoints:

GET  /peliculas: Devuelve el listado de películas
 
GET  /peliculas/{id_película}: Devuelve la película, que encaja con el id enviado
 
POST  /peliculas: Permite insertar una película al diccionario.


'''
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

def conectar_bd():
    return sqlite3.connect("peliculas.db")


@app.route("/peliculas", methods=["GET"])
def obtener_peliculas():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM peliculas")
    peliculas = [{"id": str(fila[0]), "nombre": fila[1]} for fila in cursor.fetchall()]
    
    conexion.close()
    return jsonify({"peliculas": peliculas}), 200

# GET /peliculas/<id_pelicula> - Obtener una película por su ID
@app.route("/peliculas/<int:id_pelicula>", methods=["GET"])
def obtener_pelicula(id_pelicula):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM peliculas WHERE id = ?", (id_pelicula,))
    pelicula = cursor.fetchone()
    
    conexion.close()
    
    if pelicula:
        return jsonify({"película": {"id": str(pelicula[0]), "nombre": pelicula[1]}}), 200
    return jsonify({"error": "Película no encontrada"}), 404

# POST /peliculas - Agregar una nueva película
@app.route("/peliculas", methods=["POST"])
def agregar_pelicula():
    data = request.json
    
    if not data or "nombre" not in data:
        return jsonify({"error": "Datos incompletos"}), 400
    
    conexion = conectar_bd()
    cursor = conexion.cursor()
    
    cursor.execute("INSERT INTO peliculas (nombre) VALUES (?)", (data["nombre"],))
    conexion.commit()
    
    nuevo_id = cursor.lastrowid  # Obtener el ID autoincremental de la película agregada
    conexion.close()
    
    return jsonify({"mensaje": "Película agregada", "id": str(nuevo_id)}), 201

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)