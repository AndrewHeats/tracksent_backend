
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Vehicle


class VehicleDAO(GeneralDAO):
    """
    Realisation of Vehicle data access layer.
    """
    _domain_type = Vehicle


