from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.task_model import TaskModel

task_blueprint = Blueprint('task_blueprint', __name__)

model = TaskModel()

#cocina

@task_blueprint.route('/task/add_kitchen', methods=['POST'])
@cross_origin()
def create_task():
    content = model.add_kitchen(request.json['Marca'], request.json['Nombre'], request.json['Precio'], request.json['Stock'], request.json['Descripcion'])
    return jsonify(content)

@task_blueprint.route('/task/delete_kitchen', methods=['POST'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_kitchen(int(request.json['ID_cocina'])))

@task_blueprint.route('/task/get_kitchen', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_kitchen(int(request.json['ID_cocina'])))

@task_blueprint.route('/task/get_kitchens', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_kitchens())


#Especificaciones
#######################################


@task_blueprint.route('/task/add_specification', methods=['POST'])
@cross_origin()
def create_task_2():
    content = model.add_specification(request.json['ID_cocina'], request.json['Numero_de_quemadores'], request.json['Material_de_la_parrilla'], request.json['Material_de_la_cubierta'], request.json['Capacidad_del_horno'], request.json['Encendido_electronico'], request.json['Tipo_de_energia'], request.json['Timer'], request.json['Incluye_tapa'], request.json['Marca'], request.json['Modelo'], request.json['Tipo'], request.json['Alto'], request.json['Ancho'], request.json['Profundidad'], request.json['Peso'], request.json['Hecho_en'])
    return jsonify(content)

@task_blueprint.route('/task/delete_specification', methods=['POST'])
@cross_origin()
def delete_task_2():
    return jsonify(model.delete_specification(int(request.json['ID_especificaciones'])))

@task_blueprint.route('/task/get_specification', methods=['POST'])
@cross_origin()
def task_2():
    return jsonify(model.get_specification(int(request.json['ID_especificaciones'])))

@task_blueprint.route('/task/get_specifications', methods=['POST'])
@cross_origin()
def tasks_2():
    return jsonify(model.get_specifications())



######################################


@task_blueprint.route('/task/add_user', methods=['POST'])
@cross_origin()
def create_task_3():
    content = model.add_user(request.json['Username'], request.json['Password'])
    return jsonify(content)

@task_blueprint.route('/task/delete_user', methods=['POST'])
@cross_origin()
def delete_task_3():
    return jsonify(model.delete_user(int(request.json['DNI'])))

@task_blueprint.route('/task/get_user', methods=['POST'])
@cross_origin()
def task_3():
    return jsonify(model.get_user(int(request.json['DNI'])))

@task_blueprint.route('/task/get_users', methods=['POST'])
@cross_origin()
def tasks_3():
    return jsonify(model.get_users())

#########################################

#UPDATE

@task_blueprint.route('/task/update_user_username', methods=['POST'])
@cross_origin()
def update_task():
    return jsonify(model.update_user_username(request.json['Username']))

@task_blueprint.route('/task/update_user_password', methods=['POST'])
@cross_origin()
def update_task2():
    return jsonify(model.update_user_password(request.json['Password']))


#########################################

@task_blueprint.route('/task/add_admin', methods=['POST'])
@cross_origin()
def create_task_4():
    content = model.add_admin(request.json['Username'], request.json['Password'])
    return jsonify(content)

@task_blueprint.route('/task/delete_admin', methods=['POST'])
@cross_origin()
def delete_task_4():
    return jsonify(model.delete_admin(int(request.json['ID_Admin'])))

@task_blueprint.route('/task/get_admin', methods=['POST'])
@cross_origin()
def task_4():
    return jsonify(model.get_user(int(request.json['ID_Admin'])))


#########################################

@task_blueprint.route('/task/add_info_user', methods=['POST'])
@cross_origin()
def create_task_5():
    content = model.add_info_user(request.json['Nombre'], request.json['Apellido_P'], request.json['Apellido_M'], request.json['Telefono'], request.json['Correo'], request.json['Departamento'], request.json['Provincia'], request.json['Distrito'], request.json['Direccion'], request.json['Codigo_postal'])
    return jsonify(content)

@task_blueprint.route('/task/delete_info_user', methods=['POST'])
@cross_origin()
def delete_task_5():
    return jsonify(model.delete_info_user(int(request.json['DNI'])))

@task_blueprint.route('/task/get_info_user', methods=['POST'])
@cross_origin()
def task_5():
    return jsonify(model.get_info_user(int(request.json['DNI'])))

@task_blueprint.route('/task/get_info_users', methods=['POST'])
@cross_origin()
def tasks_5():
    return jsonify(model.get_info_users())

#########################################