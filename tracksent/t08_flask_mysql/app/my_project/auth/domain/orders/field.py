from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

process_field = db.Table(
    'process_field',
    db.Column('process_id', db.Integer, db.ForeignKey('process.id')),
    db.Column('field_id', db.Integer, db.ForeignKey('field.id')),
    extend_existing=True,
)

vehicle_field = db.Table(
    'vehicle_field',
    db.Column('vehicle_id', db.Integer, db.ForeignKey('vehicle.id')),
    db.Column('field_id', db.Integer, db.ForeignKey('field.id')),
    extend_existing=True,
)

class Field(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "field"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area: float = db.Column(db.Float(7, 0))
    culture: str = db.Column(db.String(40))

    processes = db.relationship('Process', secondary=process_field, back_populates='fields')
    vehicles = db.relationship('Vehicle', secondary=vehicle_field, back_populates='fields')

    def __repr__(self) -> str:
        return f"Field({self.id}, '{self.area}', '{self.culture}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "area": self.area,
            "culture": self.culture,
            "processes": [process.put_into_dto() for process in self.processes],
            "vehicles": [vehicle.put_into_dto() for vehicle in self.vehicles]
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Field:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Field(
            area=dto_dict.get("area"),
            culture=dto_dict.get("culture"),
        )
        return obj
