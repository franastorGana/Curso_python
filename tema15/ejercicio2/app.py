'''
A partir del siguiente diccionario guardado en memoria, con valor inicial:

 

peliculas_dict = {'0':'Regreso al Futuro I', '1':'Robocop', '2':'Avatar', '3':'Big Fish}

Construir un API RestFul con Flask que interactúe con él, a través de los siguientes tres endpoints:

GET  /peliculas: Devuelve el listado de películas
 
GET  /peliculas/{id_película}: Devuelve la película, que encaja con el id enviado
 
POST  /peliculas: Permite insertar una película al diccionario.


'''
from flask import  Flask, jsonify, request

app = Flask(__name__)

peliculas_dict = {'0':'Regreso al Futuro I', '1':'Robocop', '2':'Avatar', '3':'Big Fish'}

# GET /peliculas - Obtener todas las películas
@app.route("/peliculas", methods=["GET"])
def obtener_peliculas():
    return jsonify({"peliculas": peliculas_dict}), 200


# GET /peliculas/<id_pelicula> - Obtener una película por su ID
@app.route("/peliculas/<int:id_pelicula>", methods=["GET"])
def obtener_pelicula(id_pelicula):
    print(id_pelicula)
    print(peliculas_dict)
    pelicula = peliculas_dict.get(str(id_pelicula))
    if pelicula:
        return jsonify({
            "película": {
                "id": str(id_pelicula),
                "nombre": pelicula
            }
        }), 200
    return jsonify({"error": "Película no encontrada"}), 404

# POST /peliculas - Agregar una nueva película
@app.route("/peliculas", methods=["POST"])
def agregar_pelicula():
    data = request.json  # Obtener datos enviados en formato JSON
    
    if not data or "titulo" not in data or "año" not in data or "genero" not in data:
        return jsonify({"error": "Datos incompletos"}), 400

    nuevo_id = max(peliculas_dict.keys()) + 1  # Obtener el siguiente ID disponible
    peliculas_dict[nuevo_id] = {
        "titulo": data["titulo"],
        "año": data["año"],
        "genero": data["genero"]
    }

    return jsonify({"mensaje": "Película agregada", "id": nuevo_id,"nombre":data["titulo"]}), 201

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)