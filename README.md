# Sistema CRUD con SQLAlchemy y MySQL

Este proyecto es una implementación de un sistema **CRUD** (Create, Read, Update, Delete) utilizando Python, el ORM **SQLAlchemy** y una base de datos **MySQL**. El código sigue principios de diseño limpio, separando la configuración, los modelos de datos y la lógica de negocio en módulos independientes.

## 🛠️ Estructura del Proyecto

El proyecto está organizado de la siguiente manera para facilitar su mantenimiento y escalabilidad:

* **`setup.py`**: Configuración del motor de base de datos (Engine) y creación de la sesión de SQLAlchemy.
* **`models.py`**: Definición de los modelos de datos (clase Producto) utilizando el sistema declarativo de SQLAlchemy.
* **`crud.py`**: Funciones modulares que encapsulan la lógica de acceso a datos (Create, Read, Update, Delete).
* **`main.py`**: Punto de entrada del programa que orquesta el flujo de operaciones.
* **`.gitignore`**: Instrucciones para Git sobre qué archivos y carpetas debe ignorar (como el .env real).
* **`requirements`**.txt: Lista de dependencias y librerías necesarias para ejecutar el proyecto.
* **`.env.example`**: Plantilla con las variables de entorno necesarias para que otros configuren su acceso a la DB.
* **`.env`**: Archivo (no incluido en el repositorio) para gestionar credenciales sensibles.

## 🚀 Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/juantenorioespinosa/Proyecto_ORM_CRUD.git](https://github.com/juantenorioespinosa/Proyecto_ORM_CRUD.git)
   cd Proyecto_ORM_CRUD

2. **Instalar dependencias:** Se recomienda usar un entorno virtual.
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt

3. **Configurar variables de entorno:** Crea un archivo llamado .env en la raíz del proyecto con el siguiente contenido:
   DB_PASSWORD=tu_contraseña_de_mysql

4. **Base de datos:** Asegúrate de tener un esquema en MySQL llamado practica_orm (o el nombre que hayas definido en setup.py).

📋 **Funcionalidades Implementadas**
- Create: Inserción masiva de productos mediante session.add_all().
- Read: Búsqueda global y filtrado por atributos específicos (como el título).
- Update: Actualización de stock y aplicación de descuentos calculados dinámicamente.
- Delete: Eliminación segura de registros con retorno de confirmación.
- Robustez: Manejo de errores con bloques try/except y uso de session.rollback() para garantizar la integridad de los datos.

✒️ Autor
Juan Tenorio - https://github.com/juantenorioespinosa