# Sistema de Gestión de Tareas con Usuarios y Categorías

Este es un proyecto de **gestión de tareas** desarrollado con **Python** y **Flask**. El sistema permite a los usuarios crear, leer, actualizar y eliminar tareas (CRUD). Las tareas pueden ser categorizadas y asignadas a diferentes usuarios. Los usuarios pueden iniciar sesión, y los administradores pueden asignar tareas a otros usuarios.

### Características
- **Gestión de tareas**: Los usuarios pueden crear, ver, actualizar y eliminar tareas.
- **Gestión de usuarios**: Los usuarios pueden registrarse, iniciar sesión y gestionar sus propias tareas.
- **Categorías de tareas**: Las tareas pueden ser organizadas por categorías (por ejemplo, "Trabajo", "Personal", "Urgente").
- **Prioridad y estado de tareas**: Las tareas pueden tener diferentes niveles de prioridad y estados (como "Pendiente", "En progreso" y "Completada").
- **Asignación de tareas**: Los administradores pueden asignar tareas a otros usuarios.
- **Autenticación y autorización**: Los usuarios deben iniciar sesión para acceder a sus tareas, y los administradores tienen acceso completo a todas las tareas.

### Patrones de diseño utilizados
- **Factory Method**: Para crear diferentes tipos de usuarios (Administrador y Usuario Regular).
- **DAO (Data Access Object)**: Para separar la lógica de acceso a la base de datos de la lógica de negocio.
- **Singleton**: Para manejar la sesión del usuario y la conexión a la base de datos de manera centralizada.
- **Observer**: Para notificar a los usuarios sobre cambios en el estado de sus tareas (por ejemplo, cuando una tarea es completada).

### Requisitos
- **Python** 3.x
- **Flask** y **Flask-SQLAlchemy**
- **Flask-Login** para la gestión de sesiones de usuario
- **SQLite** (base de datos predeterminada)

### Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/sistema-gestion-tareas.git
   cd sistema-gestion-tareas
   ```

2. Crea un entorno virtual (opcional, pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Crea la base de datos (esto se puede hacer automáticamente la primera vez que corras la aplicación):

   ```bash
   python
   >>> from app import db
   >>> db.create_all()  # Crea las tablas en la base de datos
   ```

5. Ejecuta la aplicación Flask:

   ```bash
   python run.py
   ```

6. Accede a la aplicación en tu navegador en `http://127.0.0.1:5000`.

### Estructura del proyecto

```bash
flask-tasks/
│
├── app/
│   ├── __init__.py            # Inicializa la aplicación Flask
│   ├── models.py              # Define las clases del modelo (Usuario, Tarea, etc.)
│   ├── routes.py              # Define las rutas de la aplicación (CRUD)
│   ├── forms.py               # Formularios para entrada de datos
│   ├── templates/             # Plantillas HTML
│   ├── static/                # Archivos estáticos (CSS, JS, imágenes)
│
├── config.py                  # Configuración de Flask y base de datos
└── run.py                     # Archivo principal para ejecutar la app
```

### Rutas principales

- `/` - Página de inicio
- `/login` - Iniciar sesión (solo para usuarios registrados)
- `/registro` - Registro de un nuevo usuario
- `/crear_tarea` - Crear una nueva tarea
- `/editar_tarea/<int:id>` - Editar una tarea existente
- `/borrar_tarea/<int:id>` - Borrar una tarea existente
- `/perfil` - Ver perfil y tareas asignadas del usuario
- `/admin` - Panel de administrador para gestionar tareas y usuarios

### Dependencias

En el archivo `requirements.txt` se incluyen todas las dependencias necesarias para ejecutar el proyecto:

```txt
Flask==2.1.1
Flask-SQLAlchemy==2.5.1
Flask-Login==0.5.0
```

### Contribuir

Si deseas contribuir a este proyecto, puedes hacer un fork del repositorio y enviar un pull request con tus mejoras.

### Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

### Autor

Nombre  
Email  
Perfil GitHub
```
