from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.config.database import Base

class Usuario(Base):
    __tablename__ = 'Usuario'
    
    email = Column(String(100), primary_key=True)
    password = Column(String(200))
    
    # Importante: "Persona" debe ser exactamente igual que __tablename__ en la clase Persona
    personaId = Column(String(36), ForeignKey('Persona.id'))
    
    # Importante: "persona" debe ser en minúsculas para coincidir con el nombre del atributo
    # en la clase Persona y "back_populates" debe ser "usuario" en minúsculas
    persona = relationship("Persona", back_populates="usuario")