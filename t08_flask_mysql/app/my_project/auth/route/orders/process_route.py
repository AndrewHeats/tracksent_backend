

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import process_controller
from my_project.auth.domain import Process

process_bp = Blueprint('processes', __name__, url_prefix='/processes')


@process_bp.get('')
def get_all_processes() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(process_controller.find_all()), HTTPStatus.OK)


@process_bp.post('')
def create_process() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    process = Process.create_from_dto(content)
    process_controller.create(process)
    return make_response(jsonify(process.put_into_dto()), HTTPStatus.CREATED)


@process_bp.get('/<int:process_id>')
def get_process(process_id: int) -> Response:
    """
    Gets process by ID.
    :return: Response object
    """
    return make_response(jsonify(process_controller.find_by_id(process_id)), HTTPStatus.OK)


@process_bp.put('/<int:process_id>')
def update_process(process_id: int) -> Response:
    """
    Updates Process by ID.
    :return: Response object
    """
    content = request.get_json()
    process = Process.create_from_dto(content)
    process_controller.update(process_id, process)
    return make_response("Process updated", HTTPStatus.OK)


@process_bp.patch('/<int:process_id>')
def patch_process(process_id: int) -> Response:
    """
    Patches Process by ID.
    :return: Response object
    """
    content = request.get_json()
    process_controller.patch(process_id, content)
    return make_response("Process updated", HTTPStatus.OK)


@process_bp.delete('/<int:process_id>')
def delete_process(process_id: int) -> Response:
    """
    Deletes Process by ID.
    :return: Response object
    """
    process_controller.delete(process_id)
    return make_response("Process deleted", HTTPStatus.OK)
