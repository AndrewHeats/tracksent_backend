
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Type


class TypeDAO(GeneralDAO):
    """
    Realisation of Type data access layer.
    """
    _domain_type = Type


