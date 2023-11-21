

from my_project.auth.dao import field_dao
from my_project.auth.service.general_service import GeneralService


class FieldService(GeneralService):
    """
    Realisation of Field service.
    """
    _dao = field_dao
