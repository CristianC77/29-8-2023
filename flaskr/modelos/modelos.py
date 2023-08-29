from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()

album_cancion = db.Table('album_cancion',
    db.Column('album_id', db.Integer, db.ForeignKey("album.id"), primary_key=True),
    db.Column('cancion_id', db.Integer, db.ForeignKey("cancion.id"), primary_key=True))

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))
    albumes = db.relationship('Album', secondary='album_cancion', back_populates="canciones")

class Medio(enum.Enum):
    disco = 1
    casete = 2
    cd = 3

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(180))
    anio = db.Column(db.Integer)
    description = db.Column(db.String(180))
    medio = db.Column(db.Enum(Medio))
    usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    canciones = db.relationship('Cancion', secondary='album_cancion', back_populates="albumes")
    __table_args__ = (db.UniqueConstraint("id_usuario", "titulo", name="titulo_unico_album"),)
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120))
    contrasena = db.Column(db.String(120))
    albumes = db.relationship('Album', cascade='all, delete, delete-orphan')
