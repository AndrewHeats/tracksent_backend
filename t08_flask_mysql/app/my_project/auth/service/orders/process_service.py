

from my_project.auth.dao import process_dao
from my_project.auth.service.general_service import GeneralService


class ProcessService(GeneralService):
    """
    Realisation of Field service.
    """
    _dao = process_dao
