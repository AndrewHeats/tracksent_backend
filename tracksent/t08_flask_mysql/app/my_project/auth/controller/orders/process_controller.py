

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import process_service


class ProcessController(GeneralController):
    """
    Realisation of Field controller.
    """
    _service = process_service
