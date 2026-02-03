from models import Producto

# 1. CREATE: Insertar datos
def crear_productos(session, lista_productos):
    """Inserta una lista de productos en la base de datos."""
    session.add_all(lista_productos)
    session.commit()
    print(f"\n¡Se han añadido {len(lista_productos)} productos a la base de datos!")

# 2. READ: Obtener datos
def obtener_todos_los_productos(session):
    """Devuelve una lista con todos los Productos."""
    return session.query(Producto).all()


def obtener_producto_por_titulo(session, titulo):
    """Busca un producto por su columna titulo."""
    return session.query(Producto).filter_by(titulo=titulo).first()

# 3. UPDATE: Actualizar datos
def actualizar_stock_y_precio(session, producto_a_editar, descuento, cantidad_a_aumentar):
    """Actualiza los valores de precio y stock de un producto existente"""
    producto_a_editar.precio -= (descuento)
    producto_a_editar.stock += cantidad_a_aumentar
    
    session.commit()
    return producto_a_editar

# 4. DELETE: Eliminar datos
def eliminar_producto(session, producto_a_eliminar):
    """Elimina el producto recibido de la base de datos"""
    session.delete(producto_a_eliminar)

    # Guardar el nombre antes que desaparezca de la base de datos
    producto_eliminado = producto_a_eliminar.titulo

    # Confirmar eliminación
    session.commit()

    return producto_eliminado