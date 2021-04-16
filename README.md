## News API

News API: [link](https://news-api-assessment.herokuapp.com/api/posts/)

### Description
***
This is a collection to news api created as test assessment by Dina Iovcheva.

News api provides CRUD functions to posts, comments, replies to comments and a few functions
to users (create, update and get by id). A postman-documentation available by the 
[link](https://www.postman.com/dinaiovcheva/workspace/newsapi/overview).

### Technologies used
***
* Python 3.8
* Django
* Django Rest Framework
* PostgreSQL
* Docker

### How to run locally
***
##### Using Docker and docker-compose:
1. Install [Docker](https://www.docker.com/) and [docker compose](https://docs.docker.com/compose/).
2. Open a terminal and navigate to the project root folder.
3. Run the following `docker-compose` commands:

```
docker-compose build
docker-compose up -d
```
4. Apply migrations by using `docker-compose exec web python manage.py migrate`.
5. The project is running on http://localhost:8000.

##### Without Docker and Compose:
1. [Install Python3.8](https://www.python.org/downloads/).
2. [Install PostgreSQL](https://www.postgresql.org/) and start it.
3. Open a terminal and navigate to the project root folder.
4. Set up virtual environment: [tutorial](https://docs.python.org/3/tutorial/venv.html).
5. Install necessary packages: `pip install requirements.txt`.
6. Configure database in `config/settings.py`
7. Run next commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
8. The project is running on http://localhost:8000 
