

from my_project.auth.dao import type_dao
from my_project.auth.service.general_service import GeneralService


class TypeService(GeneralService):
    """
    Realisation of Type service.
    """
    _dao = type_dao
