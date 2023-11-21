
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Driver


class DriverDAO(GeneralDAO):
    """
    Realisation of Driver data access layer.
    """
    _domain_type = Driver


