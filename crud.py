from models import Producto

# 1. CREATE: Insertar datos
def crear_productos(session, lista_productos):
    """
    Inserta una lista de productos en la base de datos de forma masiva.
    
    Args:
        session: Instancia de la sesión de SQLAlchemy.
        lista_productos: Una Lista (list) que contiene instancias de la clase Productos.

    Returns:
        None
    """
    session.add_all(lista_productos)
    session.commit()
    print(f"\n¡Se han añadido {len(lista_productos)} productos a la base de datos!")

# 2. READ: Obtener datos
def obtener_todos_los_productos(session):
    """
    Devuelve una lista con todos los Productos.
    
    Args:
        session: Instancia de la sesión de SQLAlchemy.

    Returns:
        Una lista (list) que contiene instancias de la clase Producto.
    """
    return session.query(Producto).all()


def obtener_producto_por_titulo(session, titulo):
    """Busca un producto por su columna titulo."""
    return session.query(Producto).filter_by(titulo=titulo).first()

# 3. UPDATE: Actualizar datos
def actualizar_stock_y_precio(session, producto_a_editar, descuento, cantidad_a_aumentar):
    """
    Actualiza los valores de precio y stock de un producto existente.
    
    Args:
        session: Instancia de la sesión de SQLAlchemy.
        producto: Objeto de la clase Producto a modificar.
        descuento: Valor numérico a restar del precio actual.
        cantidad_a_aumentar: Valor numérico a sumar al stock actual.
    
    Returns:
        El objeto producto actualizado y confirmado en la DB.
    """
    producto_a_editar.precio -= (descuento)
    producto_a_editar.stock += cantidad_a_aumentar
    
    session.commit()
    return producto_a_editar

# 4. DELETE: Eliminar datos
def eliminar_producto(session, producto_a_eliminar):
    """
    Elimina un producto existente de la base de datos.

    Args:
        session: Instancia de la sesión de SQLAlchemy.
        producto_a_eliminar: Objeto de la clase Producto a eliminar.

    Returns:
        str: El título del producto eliminado para confirmar la operación.
    """
    # Guardar el nombre antes que desaparezca de la base de datos
    producto_eliminado = producto_a_eliminar.titulo

    session.delete(producto_a_eliminar)

    # Confirmar eliminación
    session.commit()

    return producto_eliminado