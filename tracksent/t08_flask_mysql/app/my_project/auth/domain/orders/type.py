

from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Type(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type: str = db.Column(db.String(40))

    def __repr__(self) -> str:
        return f"Type({self.id}, '{self.type}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "type": self.type,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Type:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Type(
            name=dto_dict.get("name"),
            type=dto_dict.get("type"),
        )
        return obj
