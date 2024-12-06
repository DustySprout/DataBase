from flask import Blueprint, request
from .controller import *

# Створюємо Blueprints для кожного контролера
accesspoints_bp = Blueprint('accesspoints_bp', __name__, url_prefix='/api/accesspoint')
select_bp = Blueprint('select_bp', __name__, url_prefix='/api/select')


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
def get_all_select():
    return SelectController.get_all_employee_equipment()

@select_bp.route('/second', methods=['GET'])
def get_select(select_id):
    return SelectController.get_all_office_equipment(select_id)