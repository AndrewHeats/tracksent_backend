from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Driver(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "driver"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(40))
    surname: str = db.Column(db.String(40))
    phone_number: str = db.Column(db.String(13))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=True)
    vehicles = db.relationship("Vehicle", foreign_keys=[vehicle_id], lazy=True, backref="driver")

    def __repr__(self) -> str:
        return f"Driver({self.id}, '{self.name}', '{self.surname}', '{self.phone_number}', '{self.vehicles}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO with relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "phone_number": self.phone_number,
            "vehicles": self.vehicles.put_into_dto()
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Driver:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Driver(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            phone_number=dto_dict.get("phone_number"),
        )
        return obj
