

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import vehicle_controller
from my_project.auth.domain import Vehicle

vehicle_bp = Blueprint('vehicles', __name__, url_prefix='/vehicles')


@vehicle_bp.get('')
def get_all_vehicles() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(vehicle_controller.find_all()), HTTPStatus.OK)


@vehicle_bp.post('')
def create_vehicle() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    vehicle = Vehicle.create_from_dto(content)
    vehicle_controller.create(vehicle)
    return make_response(jsonify(vehicle.put_into_dto()), HTTPStatus.CREATED)


@vehicle_bp.get('/<int:vehicle_id>')
def get_vehicle(vehicle_id: int) -> Response:
    """
    Gets type by ID.
    :return: Response object
    """
    return make_response(jsonify(vehicle_controller.find_by_id(vehicle_id)), HTTPStatus.OK)


@vehicle_bp.put('/<int:vehicle_id>')
def update_vehicle(vehicle_id: int) -> Response:
    """
    Updates Process by ID.
    :return: Response object
    """
    content = request.get_json()
    vehicle = Vehicle.create_from_dto(content)
    vehicle_controller.update(vehicle_id, vehicle)
    return make_response("Vehicle updated", HTTPStatus.OK)


@vehicle_bp.patch('/<int:vehicle_id>')
def patch_vehicle(vehicle_id: int) -> Response:
    """
    Patches Process by ID.
    :return: Response object
    """
    content = request.get_json()
    vehicle_controller.patch(vehicle_id, content)
    return make_response("Vehicle updated", HTTPStatus.OK)


@vehicle_bp.delete('/<int:vehicle_id>')
def delete_vehicle(vehicle_id: int) -> Response:
    """
    Deletes Process by ID.
    :return: Response object
    """
    vehicle_controller.delete(vehicle_id)
    return make_response("Vehicle deleted", HTTPStatus.OK)
