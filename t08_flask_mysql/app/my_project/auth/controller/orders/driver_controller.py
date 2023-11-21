

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import driver_service


class DriverController(GeneralController):
    """
    Realisation of Driver controller.
    """
    _service = driver_service
