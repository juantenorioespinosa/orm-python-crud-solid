![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-SOLID-B80672?style=for-the-badge)
![Patterns](https://img.shields.io/badge/Design_Patterns-Repository-orange?style=for-the-badge)
![CRUD](https://img.shields.io/badge/Operations-CRUD-green?style=for-the-badge)


# Sistema CRUD con SQLAlchemy y MySQL

Este proyecto es una implementación de un sistema **CRUD** (Create, Read, Update, Delete) utilizando Python, el ORM **SQLAlchemy** y una base de datos **MySQL**. El código sigue principios de diseño limpio, separando la configuración, los modelos de datos y la lógica de negocio en módulos independientes.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera para facilitar su mantenimiento y escalabilidad:

* **`setup.py`**: Configuración del motor de base de datos (Engine) y creación de la sesión de SQLAlchemy.
* **`models.py`**: Definición de los modelos de datos (clase Producto) utilizando el sistema declarativo de SQLAlchemy.
* **`crud.py`**: Funciones modulares que encapsulan la lógica de acceso a datos (Create, Read, Update, Delete).
* **`main.py`**: Punto de entrada del programa que orquesta el flujo de operaciones.
* **`.gitignore`**: Instrucciones para Git sobre qué archivos y carpetas debe ignorar (como el .env real).
* **`requirements`**.txt: Lista de dependencias y librerías necesarias para ejecutar el proyecto.
* **`.env.example`**: Plantilla con las variables de entorno necesarias para que otros configuren su acceso a la DB.
* **`.env`**: Archivo (no incluido en el repositorio) para gestionar credenciales sensibles.

## Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/juantenorioespinosa/orm-python-crud-solid.git](https://github.com/juantenorioespinosa/orm-python-crud-solid.git)
   cd orm-python-crud-solid

2. **Instalar dependencias:** Se recomienda usar un entorno virtual.
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt

3. **Configurar variables de entorno:** Crea un archivo llamado .env en la raíz del proyecto con el siguiente contenido:
   DB_PASSWORD=tu_contraseña_de_mysql

4. **Base de datos:** Asegúrate de tener un esquema en MySQL llamado practica_orm (o el nombre que hayas definido en setup.py).

## Funcionalidades Implementadas

**1. Create:** Inserción masiva de productos mediante session.add_all().

**2. Read:** Búsqueda global y filtrado por atributos específicos (como el título).

**3. Update:** Actualización de stock y aplicación de descuentos calculados dinámicamente.

**4. Delete:** Eliminación segura de registros con retorno de confirmación.

**5. Robustez:** Manejo de errores con bloques try/except y uso de session.rollback() para garantizar la integridad de los datos.

## Principios SOLID Aplicados

Este proyecto implementa los principios de diseño SOLID para garantizar un código mantenible y escalable:

**1. SRP (Responsabilidad Única):** Cada módulo tiene una misión única y clara.

models.py: Define la estructura de datos.

setup.py: Gestiona la infraestructura de conexión.

crud.py: Ejecuta operaciones de base de datos.

main.py: Orquesta el flujo lógico sin conocer detalles de implementación.

**2. OCP (Abierto/Cerrado)**
Las funciones en crud.py están diseñadas para ser extensibles sin modificar su código interno. Por ejemplo, actualizar_stock_y_precio permite variar los valores de descuento y stock desde los argumentos, adaptándose a nuevas reglas de negocio sin alterar su estructura.

**3. DIP (Inversión de Dependencias)**
Se utiliza la inyección de dependencias al pasar la session como argumento a las funciones de crud.py. Esto desacopla los módulos, evita importaciones circulares y permite que las funciones dependan de una abstracción (la sesión recibida) en lugar de una instancia concreta.

## Próximas mejoras
- [ ] Documentar las funciones con Docstrings.

✒️ Autor
Juan Tenorio - https://github.com/juantenorioespinosa
