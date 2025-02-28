# ANTES DE TODO EDER CHIPI Y CHIZITO :V 

# IMC Control Master

IMC Control Master es una aplicación para registrar y controlar el índice de masa corporal (IMC) de los usuarios.

## Instalación

Sigue estos pasos para instalar y configurar el proyecto:

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (opcional, pero recomendado)

### Clonar el repositorio

```bash
git clone https://github.com/BufonMestizo/app_imc/tree/main
cd imc-control-master
```

### Crear y activar un entorno virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Configurar la base de datos

Asegúrate de tener una base de datos configurada y actualiza la configuración en el archivo `config.py` si es necesario.

### Ejecutar la aplicación

```bash
export FLASK_APP=backend
export FLASK_ENV=development
flask run
```

En Windows:

```bash
set FLASK_APP=backend
set FLASK_ENV=development
flask run
```

La aplicación estará disponible en `http://127.0.0.1:5000`.

## Endpoints

- `POST /register`: Registrar un nuevo usuario.
- `POST /login`: Iniciar sesión.
- `GET /summary`: Obtener un resumen de todos los registros de IMC.
- `POST /insert`: Insertar un nuevo registro de IMC.

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
