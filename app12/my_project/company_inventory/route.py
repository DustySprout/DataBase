from flask import Blueprint, request, current_app, jsonify
from .controller import *

# Створюємо Blueprints для кожного контролера
accesspoints_bp = Blueprint('accesspoints_bp', __name__, url_prefix='/api/accesspoint')
select_bp = Blueprint('select_bp', __name__, url_prefix='/api/select')
trigger_bp = Blueprint('trigger_bp', __name__, url_prefix='/api/trigger')
procedure_bp = Blueprint('procedure_bp', __name__, url_prefix='/api/procedure')


# ---------- Access Point Routes ----------

@accesspoints_bp.route('/', methods=['GET'])
def get_all_access_points():
    return AccessPointsController.get_all_access_points()

@accesspoints_bp.route('/<int:access_point_id>', methods=['GET'])
def get_access_point(access_point_id):
    return AccessPointsController.get_access_point(access_point_id)

@accesspoints_bp.route('/', methods=['POST'])
def add_access_point():
    data = request.get_json()
    print(data)
    return AccessPointsController.add_access_point(data)

@accesspoints_bp.route('/<int:access_point_id>', methods=['PUT'])
def update_access_point(access_point_id):
    data = request.get_json()
    return AccessPointsController.update_access_point(access_point_id, data)

@accesspoints_bp.route('/<int:access_point_id>', methods=['DELETE'])
def delete_access_point(access_point_id):
    return AccessPointsController.delete_access_point(access_point_id)

# ---------- Select Routes ----------
@select_bp.route('/first', methods=['GET'])
def first():
    return SelectController.first()

@select_bp.route('/second', methods=['GET'])
def second():
    return SelectController.second()


#  ---------- Fuctional Routes ----------
@select_bp.route('/get_all_access_points_func', methods=['GET'])
def get_all_access_points_func():
    query = "CALL get_all_access_points();"

    cursor = current_app.mysql.connection.cursor()
    cursor.execute(query)
    rv = cursor.fetchall()
    cursor.close()

    return jsonify(rv)

@trigger_bp.route('/triggeraccesspoint', methods=['GET'])
def triggeraccesspoint():
    query = """SELECT * FROM `company_inventory`.`access_points_log`;"""

    cursor = current_app.mysql.connection.cursor()
    cursor.execute(query)
    rv = cursor.fetchall()
    cursor.close()

    return jsonify(rv)

@procedure_bp.route('/procedureaccesspoint', methods=['post'])
def procedureaccesspoint():
    data = request.get_json()
    print(data)    
    query = """CALL insert_access_point(%s, %s);"""

    cursor = current_app.mysql.connection.cursor()
    cursor.execute(query, (data['serial_number'], data['model']))
    current_app.mysql.connection.commit()
    cursor.close()
    
    query = """SELECT * FROM `company_inventory`.`access_points_log`;"""
    cursor = current_app.mysql.connection.cursor()
    cursor.execute(query)
    rv = cursor.fetchall()
    cursor.close()

    return jsonify(rv)  

