

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import type_controller
from my_project.auth.domain import Type

type_bp = Blueprint('types', __name__, url_prefix='/types')


@type_bp.get('')
def get_all_types() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(type_controller.find_all()), HTTPStatus.OK)


@type_bp.post('')
def create_type() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    type = Type.create_from_dto(content)
    type_controller.create(type)
    return make_response(jsonify(type.put_into_dto()), HTTPStatus.CREATED)


@type_bp.get('/<int:type_id>')
def get_type(type_id: int) -> Response:
    """
    Gets type by ID.
    :return: Response object
    """
    return make_response(jsonify(type_controller.find_by_id(type_id)), HTTPStatus.OK)


@type_bp.put('/<int:type_id>')
def update_type(type_id: int) -> Response:
    """
    Updates Process by ID.
    :return: Response object
    """
    content = request.get_json()
    type = Type.create_from_dto(content)
    type_controller.update(type_id, type)
    return make_response("Type updated", HTTPStatus.OK)


@type_bp.patch('/<int:type_id>')
def patch_type(type_id: int) -> Response:
    """
    Patches Process by ID.
    :return: Response object
    """
    content = request.get_json()
    type_controller.patch(type_id, content)
    return make_response("Type updated", HTTPStatus.OK)


@type_bp.delete('/<int:type_id>')
def delete_type(type_id: int) -> Response:
    """
    Deletes Process by ID.
    :return: Response object
    """
    type_controller.delete(type_id)
    return make_response("Type deleted", HTTPStatus.OK)
