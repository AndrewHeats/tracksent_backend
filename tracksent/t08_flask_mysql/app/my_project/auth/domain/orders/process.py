

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


class Process(db.Model):
    __tablename__ = "process"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    process = db.Column(db.String(40))

    fields = db.relationship('Field', secondary=process_field, back_populates='processes')

    def __repr__(self):
        return f"Process({self.id}, '{self.process}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "process": self.process,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Process:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Process(
            name=dto_dict.get("name"),
            process=dto_dict.get("process"),
        )
        return obj
