# django-rest-backend
Django rest api with GeoDjango

Es un muy buen ejercicio, no era necesario, pero ya que no había tenido la oportunidad de usar Posgis
aproveché para estudiarlo y tratar de implementar algo con esta manera de manejar geolocalizaciones.
Durante este desarrollo aprendí mucho sobre geolocalización y algunas de las herramientas
utilizadas para este tipo de datos y no niego que todavía me falta mucho por aprender acerca 
de este tema que está presente en nuestra vida diaria, pero que muchos ignoramos todos sus detalles.

# Instalación y ejecución del proyecto

## Con Docker

Para la ejecución con **Docker**, se debe:

- Instalar:
    * Docker
    * docker compose
- Clonar el repositorio
    
        git clone https://github.com/bigintelligence/django-rest-backend.git
- En el archivo docker-compose ubicado en la raíz del proyecto modificar las variables de entono 
correspondientes al acceso y configuración de BD
- Ejecutar los siguientes comandos
    
        docker-compose up --build

Si todo está ok, recibirá un mensaje en consola como este:

        Starting development server at http://0.0.0.0:8000/
        Quit the server with CONTROL-C.

Continuar con el apartado [Revision api endpoint](#revision-api-endpoint)

## Local

Se debe tener especial cuidado con la instalación de las librerías de geolocalización, ya que de estas depende 
**django.contrib.gis**.
Para la ejecución en entorno **local**, se debe:
- Instalar:
    * Las librerías de geolocalización disponibles en la siguiente url:
        
            https://www.gisinternals.com/release.php
    * un servidor de base de datos postgresSQL con PosGis o un contenedor iniciado con la imagen posgis/posgis
    * python 3.5 o superior con el gestor de paquetes pip

- Clonar el repositorio

        git clone https://github.com/bigintelligence/django-rest-backend.git

- Crear las variables de entorno correspondientes al servidor de base de datos SQL:
    * PG_DRIVER
    * PG_USER
    * PG_PASS
    * PG_HOST
    * PG_PORT
    * PG_BASE
- Crear las variables de entorno correspondientes a la configuración de django:
    * DJANGO_ALLOWED_HOSTS: "127.0.0.1 localhost 0.0.0.0 api"
    * DJANGO_SECRET_KEY: <<secret>>
    * DJANGO_CORS_ORIGIN_WHITELIST: "http://127.0.0.1 http://localhost http://0.0.0.0 http://api"
- Si lo prefiere crear el entorno virtual:

        python -m venv env
        env\Scripts\activate.bat ó source env/bin/activate

- Estando en la carpeta djangorestbackend ejecutar los siguientes comandos:

        pip install -r requirements.txt
        python manage.py runserver

- Si desea ejecutar los test de Django antes de correr el servidor de django:

        python manage.py tests

- Si desea ejecutar los test con pytest:

        pytest

# Revision api endpoint

Sé que solo era necesario un endpoint, sin embargo, para efectos de verificación de lectura de los registros
y que todo funcione correctamente agregué el endpoint de carga, para que se registre data sintética, de modo que 
se vea funcional el endpoint de consulta.

Para efectos de funcionamiento de esta api en sistemas distribuidos y de alta demanda, habrá que indagar más sobre
el requerimiento y la arquitectura en la que funcionará, y así poder hacer las modificaciones pertinentes a esta api.

- Para que se carguen datos de muestra iniciales a la base de datos, ejecutar la siguiente petición GET:

        http://localhost:8000/api/carga/

    El cual responderá lo siguiente:
```json
{ "upload_state": "Ok", "saved_result": "rows saved: 10/10" }
```
- Luego, ejecutar la siguiente petición GET:

      http://127.0.0.1:8000/api/inmuebles/

    El cual responderá el listado de los registros en BD:
```json
[
    {
        "id": 1,
        "build_status": 1,
        "is_active": false,
        "start_month": 19212,
        "construction_type": 2,
        "date_diff": "2",
        "description": "Chalet adosado ",
        "date_in": "2021-05-31T00:00:00Z",
        "property_type": 3,
        "end_week": 15186,
        "typology_type": 4,
        "coordinates": {
            "type": "Point",
            "coordinates": [
                40.6432,
                -3.23741
            ]
        },
        "boundary_id": 64607,
        "id_uda": "54-94183090",
        "title": "Cabanillas del Campo",
        "listing_type": 1,
        "date_out": "2021-06-14T00:00:00Z",
        "start_week": 15184,
        "end_quarter": 82,
        "last_activity": 340,
        "start_quarter": 82,
        "end_month": 19213
    },
    ...
]
```

# Mejoras
Muchas!
Pero todo depende del requerimiento y de la definición de infraestructura.
Claro que se me pudo haber pasado algo que no ví o se podría implementar algún patron de diseño 
diferente al adapter que implemente en utils, o generar más casos de test, o generar una cobertura con pytest, etc.

# Conclusión
Esto es solo un abrebocas de como implementar GeoDjango, un snipped interesante en caso de necesitarse y un aprendizaje
de algo que utilizamos a diario.

# Nota
Los datos y contraseñas en este repositorio no son reales y no son utilizados por mí en ningún sistema disponible al público.
Se aconseja que estos datos y contraseñas sean cambiados a su gusto y necesidad, ya que no son seguros.
