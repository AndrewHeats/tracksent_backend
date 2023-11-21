
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import field_controller
from my_project.auth.domain import Field

field_bp = Blueprint('fields', __name__, url_prefix='/fields')


@field_bp.get('')
def get_all_fields() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(field_controller.find_all()), HTTPStatus.OK)


@field_bp.post('')
def create_field() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    field = Field.create_from_dto(content)
    field_controller.create(field)
    return make_response(jsonify(field.put_into_dto()), HTTPStatus.CREATED)


@field_bp.get('/<int:field_id>')
def get_field(field_id: int) -> Response:
    """
    Gets field by ID.
    :return: Response object
    """
    return make_response(jsonify(field_controller.find_by_id(field_id)), HTTPStatus.OK)


@field_bp.put('/<int:field_id>')
def update_field(field_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    field = Field.create_from_dto(content)
    field_controller.update(field_id, field)
    return make_response("Field updated", HTTPStatus.OK)


@field_bp.patch('/<int:field_id>')
def patch_field(field_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    field_controller.patch(field_id, content)
    return make_response("Field updated", HTTPStatus.OK)


@field_bp.delete('/<int:field_id>')
def delete_field(field_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    field_controller.delete(field_id)
    return make_response("Field deleted", HTTPStatus.OK)
