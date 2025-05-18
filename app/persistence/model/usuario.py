from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.config.database import Base

class Usuario(Base):
    __tablename__ = 'usuario'
    
    email = Column(String(100), primary_key=True)
    password = Column(String(200))
    is_active = Column(Boolean, default=True)
    
    personaId = Column(String(36), ForeignKey('persona.id'))
    persona = relationship("Persona", back_populates="usuario")