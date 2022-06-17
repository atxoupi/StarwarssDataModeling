import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(8), nullable=False)
    favoriteUser = relationship('favoritos', backref='user', lazy=True)

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    lastname = Column(String(250))
    id_planeta = Column(Integer, ForeignKey('planetas.id'), nullable=False)
    ojos = Column(String(20))
    pelo = Column(String(20))
    altura= Column(Integer)
    peso= Column(Integer)
    favoritePersonaje = relationship('personajes', backref='user', lazy=True)

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    clima = Column(String(250))
    poblacion = Column(Integer)
    rotacion = Column(String(20))
    planetPersonaje = relationship('personajes', backref='planetas', lazy=True)
    favoritePlanet = relationship('planetas', backref='user', lazy=True)

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    cilindrada = Column(Integer)
    capacidad = Column(Integer)
    favoriteVehiculo = relationship('favoritos', backref='vehiculos', lazy=True)
    

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'),nullable=False)
    id_personaje = Column(Integer, ForeignKey('personajes.id'),nullable=False)
    id_planeta = Column(Integer, ForeignKey('planetas.id'),nullable=False)
    id_vehiculo = Column(Integer, ForeignKey('vehiculos.id'),nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')