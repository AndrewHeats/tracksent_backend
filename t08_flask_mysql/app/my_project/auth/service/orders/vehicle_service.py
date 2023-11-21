

from my_project.auth.dao import vehicle_dao
from my_project.auth.service.general_service import GeneralService


class VehicleService(GeneralService):
    """
    Realisation of Vehicle service.
    """
    _dao = vehicle_dao
