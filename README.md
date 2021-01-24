## Summary:
Python JWT authentication in Django Rest Framework with Postgres database.

It contains the following apps:
- authentication (implements authentication)
- shipments (endpoint to filter data)

## Requirements:
```
appnope==0.1.2
asgiref==3.3.1
backcall==0.2.0
decorator==4.4.2
Django==3.1.5
django-cors-headers==3.6.0
django-filter==2.4.0
djangorestframework==3.12.2
ipdb==0.13.4
ipython==7.19.0
ipython-genutils==0.2.0
jedi==0.18.0
parso==0.8.1
pexpect==4.8.0
pickleshare==0.7.5
prompt-toolkit==3.0.14
psycopg2-binary==2.8.6
ptyprocess==0.7.0
Pygments==2.7.4
PyJWT==2.0.1
pytz==2020.5
sqlparse==0.4.1
traitlets==5.0.5
wcwidth==0.2.5

```

## Project Structure (App Based):
```bash
TracksForShippers_server/
├── apps
│   ├── authentication
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── authentication.py
│   │   ├── permission.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── shipments
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializer.py
│   │   ├── urls.py
│   │   └── views.py
│   └── jwt_utility.py
├── django_rest_jwt
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── README.md
├── manage.py
├── models.py
└── requirements.txt
```
### How to start application (using Virtual Environment)
- Clone the project using command:
    ```
    git clone < URL repo >
    ```
- Go into the project directory:
    ```
    cd < directory >
    ```
- Create and Activate the Virtual Environment:
  ```
  virtualenv <name of the environment> e.g virtualenv venv_jwt
  source venv_jwt/bin/activate
  ```
- Install requirements:
  ```
  pip install -r requirements.txt
  ```
Note: You can see your installed dependencies by running command: ```pip freeze```
- Run the Application:
  ```
  python3 manage.py runserver
  ```
  
### Test using POSTMAN
- http://127.0.0.1:8000/api/auth/login/
```
{"username": "website_developer","password":"any"}

```
- http://127.0.0.1:8000/api/auth/register/
```
{"id": 2, "username": "website_developer", "email": "", "first_name": "", "last_name": "", "password":"any"}
```
- http://127.0.0.1:8000/api/shipments/list?type_of_goods=Cereals&type_of_calculations=modeled&start_city=Berlin&end_city=Bremen&start_time=2020-09-10T08:15:00Z&end_time=2020-09-10T13:45:00Z
```
  {
    "id": 14177,
    "shipper_company_id": 1,
    "carrier_company_id": -102,
    "truck_id": null,
    "co2_model_id": 2,
    "travelled_distance": 396.054314614305,
    "fuel_consumed": null,
    "estimated_fuel_consumed": 380.452270818669,
    "weight": 17.210862922861,
    "type_of_goods": "Cereals",
    "start_country": "Germany",
    "start_city": "Berlin",
    "start_postcode": "10557",
    "end_country": "Germany",
    "end_city": "Bremen",
    "end_postcode": "28195",
    "type_of_calculations": "modeled",
    "allocated_distance": null,
    "allocated_fuel": null,
    "total_co2_emitted": 817.972382260137,
    "creation_timestamp": "2020-09-10T06:43:37.281385Z",
    "last_updated_timestamp": "2020-09-10T06:43:37.281385Z",
    "start_time": "2020-09-10T08:15:00Z",
    "end_time": "2020-09-10T13:45:00Z",
    "fuel_type": "diesel"
  }
```

### Userful Links
- https://pypi.org/project/jwt/
- https://pyjwt.readthedocs.io/en/latest/


