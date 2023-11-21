

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import vehicle_service


class VehicleController(GeneralController):
    """
    Realisation of Vehicle controller.
    """
    _service = vehicle_service
