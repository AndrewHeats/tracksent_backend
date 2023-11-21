

from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto
vehicle_field = db.Table(
    'vehicle_field',
    db.Column('vehicle_id', db.Integer, db.ForeignKey('vehicle.id')),
    db.Column('field_id', db.Integer, db.ForeignKey('field.id')),
    extend_existing=True,
)

class Vehicle(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "vehicle"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model: str = db.Column(db.String(10))
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=True)
    type = db.relationship("Type", foreign_keys=[type_id], lazy=True, uselist=False, backref="vehicles")  # only on the child class

    fields = db.relationship('Field', secondary=vehicle_field, back_populates='vehicles')

    def __repr__(self) -> str:
        return f"Vehicle({self.id}, '{self.type}', '{self.model}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "type": self.type.type if self.type is not None else "",
            "model": self.model
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Vehicle:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Vehicle(
            type_id=dto_dict.get("type_id"),
            model=dto_dict.get("model")
        )
        return obj
