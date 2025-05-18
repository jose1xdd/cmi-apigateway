from sqlalchemy import Enum, Column, String, Integer, Date, ForeignKey
from app.config.database import Base
from app.persistence.model.enum import EnumDocumento, EnumEscolaridad, EnumParentesco, EnumSexo
from sqlalchemy.orm import relationship


class Persona(Base):
    __tablename__ = 'persona'

    id = Column(String(36), primary_key=True)
    tipoDocumento = Column(Enum(EnumDocumento))
    nombre = Column(String(50))
    apellido = Column(String(50))
    fechaNacimiento = Column(Date)
    parentesco = Column(Enum(EnumParentesco))
    sexo = Column(Enum(EnumSexo))
    profesion = Column(String(100), nullable=True)
    escolaridad = Column(Enum(EnumEscolaridad))
    integrantes = Column(Integer)
    direccion = Column(String(200))
    telefono = Column(String(20))
    idFamilia = Column(Integer)
    idParcialidad = Column(Integer)

    usuario = relationship("Usuario", back_populates="persona", uselist=False)
