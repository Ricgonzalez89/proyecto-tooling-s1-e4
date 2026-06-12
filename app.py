"""
API de Tareas - Proyecto Tooling Python
Framework: Flask
Puerto: 5000
Almacenamiento: En memoria (lista)
"""
from flask import Flask, request, jsonify
app = Flask(__name__)
# BASE DE DATOS EN MEMORIA (NO MODIFICAR)
tareas = []
contador_id = 1

#Hacemos el route para el get, donde se va a mostrar la lista de tareas
@app.route('/tareas', methods=['GET'])
def listar_tareas():
    """Retornar la lista completa de tareas en JSON."""
    #Retornamos el JSON con la lista de tareas y el código 200(OK)
    return jsonify(tareas), 200

#Hacemos el route para el post, donde se va a crear una nueva tarea
@app.route('/tareas', methods=['POST'])
def crear_tarea():
    """
    Recibir JSON con ,"titulo": "..."-
    Validar, crear tarea, retornar código 201 o 400.
    """
    #llamamos a la variable global contador_id para poder modificarla dentro de la función
    global contador_id
    #pedimos los datos del request en formato JSON
    datos = request.get_json()
    #Validamos que los datos no sean nulos y que contengan la clave 'titulo'
    if not datos:
        #Si los datos no son válidos, retornamos un error con código 400 (Bad Request)
        return jsonify({'error': 'Faltan datos'}), 400
    #Validamos que los datos contengan la clave 'titulo'
    if 'titulo' not in datos:
        #Si titulo no esta en los datos, retornamos un error con código 400 (Bad Request)
        return jsonify({'error': 'El unico campo requerido es: "titulo"'}), 400
    #Si los datos son válidos, creamos la nueva tarea con un ID único y el título proporcionado
    nueva_tarea = {
        'id': contador_id,
        'titulo': datos['titulo']
    }
    #Agregamos la nueva tarea a la lista de tareas
    tareas.append(nueva_tarea)
    #Incrementamos la variable contador_id para el próximo ID único
    contador_id += 1
    #Retornamos la nueva tarea con código 201 (Created)
    return jsonify(nueva_tarea), 201
    
@app.route('/tareas/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    """Eliminar tarea por ID. Código 200 si existe, 404 si no."""
    # TODO: Implementar
    pass
if __name__ == '__main__':
    app.run(port=5000, debug=True)
