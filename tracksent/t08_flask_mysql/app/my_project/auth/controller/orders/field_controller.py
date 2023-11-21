

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import field_service


class FieldController(GeneralController):
    """
    Realisation of Field controller.
    """
    _service = field_service
