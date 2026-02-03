from setup import Session
from models import Producto
from crud import crear_productos
from crud import obtener_todos_los_productos, obtener_producto_por_titulo
from crud import actualizar_stock_y_precio
from crud import eliminar_producto

# Abrir la sesión (la conexión activa para trabajar)
session = Session()

# 1. CREATE: Insertar datos
productos_nuevos= [
    Producto(titulo = "Super Mario Bros.", plataforma = "Nintendo Switch", precio = 59.9, stock = 10),
    Producto(titulo = "Tetris", plataforma = "Game Boy", precio = 24.9, stock = 15)
]

try:
    crear_productos(session,productos_nuevos)
except Exception as e:
    session.rollback()   # Si hay error, deshace los cambios
    print(f"\nError al añadir el producto: {e}")

# 2. READ: Obtener datos
print("\n--- Lista de Inventario ---")
Inventario = obtener_todos_los_productos(session)
for producto in Inventario:
    print(producto)

# Búsqueda específica
titulo_buscado =  "Super Mario Bros."
producto_encontrado = obtener_producto_por_titulo(session, titulo_buscado)

if producto_encontrado:
        print(f"Producto encontrado: {producto_encontrado.titulo} | Stock: {producto_encontrado.stock}")
else:
    print(f"El producto {titulo_buscado} no existe.")

# 3. UPDATE: Actualizar datos
titulo_objetivo = "Tetris"
try:
    # Identificar el registro
    producto_a_editar = obtener_producto_por_titulo(session,titulo_objetivo)

    if producto_a_editar:
        print(f"\n--- Actualizando: {producto_a_editar.titulo} ---")

        # Logica de negocio
        descuento = producto_a_editar.precio * 0.25   # 25% de descuento
        cantidad_a_aumentar = 10

        # Delegar la persistencia de los datos a la función en CRUD
        producto_actualizado = actualizar_stock_y_precio(session, producto_a_editar,descuento, cantidad_a_aumentar)

        print(f"¡{producto_actualizado.titulo} actualizado!")
        print(f"Nuevo Precio: {producto_actualizado.precio:.2f} | Nuevo stock: {producto_actualizado.stock}")
    else:
        print("\nNo se encontró el producto para actualizar")

except Exception as e:
    session.rollback()
    print(f"\nError al actualizar el producto: {e}")

# 4. DELETE: Eliminar
titulo_a_eliminar = "Super Mario Bros."
try:
    # Buscar el producto a eliminar
    producto_a_eliminar = obtener_producto_por_titulo(session, titulo_a_eliminar)

    if producto_a_eliminar:
        producto_eliminado = eliminar_producto(session, producto_a_eliminar)
        print(f"\n¡El producto '{producto_eliminado}' ha sido eliminado!")
    else:
        print("\nNo se encontro el producto para eliminar")

except Exception as e:
    session.rollback()
    print(f"\nError al eliminar el producto: {e}")

# Mostrar lista actualizada
print(f"\nInventario actualizado:")
lista_productos = session.query(Producto).all()

for producto in enumerate(lista_productos, start=1):
    print(f"{producto[0]}. {producto[1]}")

# Siempre cerrar la sesión al terminar
session.close()
