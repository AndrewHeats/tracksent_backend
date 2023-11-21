
from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Field


class FieldDAO(GeneralDAO):
    """
    Realisation of Field data access layer.
    """
    _domain_type = Field


