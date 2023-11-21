

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import driver_controller
from my_project.auth.domain import Driver


driver_bp = Blueprint('drivers', __name__, url_prefix='/drivers')


@driver_bp.get('')
def get_all_drivers() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(driver_controller.find_all()), HTTPStatus.OK)


@driver_bp.post('')
def create_driver() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    driver = Driver.create_from_dto(content)
    driver_controller.create(driver)
    return make_response(jsonify(driver.put_into_dto()), HTTPStatus.CREATED)


@driver_bp.get('/<int:driver_id>')
def get_driver(driver_id: int) -> Response:
    """
    Gets type by ID.
    :return: Response object
    """
    return make_response(jsonify(driver_controller.find_by_id(driver_id)), HTTPStatus.OK)


@driver_bp.put('/<int:driver_id>')
def update_driver(driver_id: int) -> Response:
    """
    Updates Process by ID.
    :return: Response object
    """
    content = request.get_json()
    driver = Driver.create_from_dto(content)
    driver_controller.update(driver_id, driver)
    return make_response("Driver updated", HTTPStatus.OK)


@driver_bp.patch('/<int:driver_id>')
def patch_driver(driver_id: int) -> Response:
    """
    Patches Process by ID.
    :return: Response object
    """
    content = request.get_json()
    driver_controller.patch(driver_id, content)
    return make_response("Driver updated", HTTPStatus.OK)


@driver_bp.delete('/<int:driver_id>')
def delete_driver(driver_id: int) -> Response:
    """
    Deletes Process by ID.
    :return: Response object
    """
    driver_controller.delete(driver_id)
    return make_response("Driver deleted", HTTPStatus.OK)
