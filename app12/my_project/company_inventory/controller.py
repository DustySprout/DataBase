from .dao import *

from flask import jsonify, request

class AccessPointsController:
    @staticmethod
    def get_all_access_points():
        access_points = AccessPointsDAO.get_all_access_points()
        return jsonify(access_points), 200
    
    @staticmethod
    def get_access_point(access_point_id):
        access_point = AccessPointsDAO.get_access_point_by_id(access_point_id)
        if access_point:
            return jsonify(access_point), 200
        return jsonify({'message': 'Access Point not found'}), 404
    
    @staticmethod
    def add_access_point(data):
        if not data or not all(key in data for key in ('serial_number', 'model')):
            return jsonify({'message': 'Invalid data'}), 400
        AccessPointsDAO.add_access_point(data['serial_number'], data['model'])
        return jsonify({'message': 'Access Point added successfully!'}), 201
       
    
    @staticmethod
    def update_access_point(access_point_id, data):
        if not data or not all(key in data for key in ('serial_number', 'model')):
            return jsonify({'message': 'Invalid data'}), 400
        AccessPointsDAO.update_access_point(access_point_id, data['serial_number'], data['model'])
        return jsonify({'message': 'Access Point updated successfully!'}), 200
    
    @staticmethod
    def delete_access_point(access_point_id):
        try:
            AccessPointsDAO.delete_access_point(access_point_id)
            return jsonify({'message': 'Access Point deleted successfully!'}), 200
        except Exception as e:
            return jsonify({'message': f'Error deleting Access Point: {e}'}), 500

# Тут не всі контролери, вибираю виключно необхідні для прикладу за лабораторною роботою аби переконатись що все працює

class SelectController:
    @staticmethod
    def first():
        select = SelectDAO.first()
        return jsonify(select), 200
    
    @staticmethod
    def second():
        select = SelectDAO.second()
        return jsonify(select), 200
    

    
    