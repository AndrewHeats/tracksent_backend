

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import type_service


class TypeController(GeneralController):
    """
    Realisation of Type controller.
    """
    _service = type_service
