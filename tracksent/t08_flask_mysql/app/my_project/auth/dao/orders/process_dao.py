
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Process


class ProcessDAO(GeneralDAO):
    """
    Realisation of Field data access layer.
    """
    _domain_type = Process


