from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float
from setup import engine

Base = declarative_base()

class Producto(Base):
    """
    Representa la tabla 'productos' en la base de datos.
    Cada instancia de esta clase corresponde a una fila de la tabla.
    """
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    plataforma = Column(String(50))
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    # Representación del objeto
    def __repr__(self):
        """
        Define una representación legible del objeto en formato string.
        Útil para depuración (debugging) y logs por consola.
        """
        return f"Producto: titulo={self.titulo}, precio={self.precio}, stock={self.stock}"

# Crear la tabla 'productos' en la base de datos
Base.metadata.create_all(engine)
