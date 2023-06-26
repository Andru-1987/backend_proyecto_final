#!/bin/bash


# STEPS QUE RECOMIENDO
# NO ESTA FUNCIONANDO 100%

virtualenv venv
source ./venv/bin/activate 

pip install -r requirements.txt && sudo docker compose -f postgres_bd/docker-compose.yml up -d --build  

docker exec -it postgres psql -U postgres_admin -c "CREATE DATABASE sinapsis_web ENCODING 'LATIN1' TEMPLATE template0 LC_COLLATE 'C' LC_CTYPE 'C';"

python sinapsis_web/manage.py makemigrations && python sinapsis_web/manage.py migrate &&  python sinapsis_web/manage.py runserver