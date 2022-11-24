# О ПРОЕКТЕ

Проект HTTP-api-database. 
В данном проекте реализована возможность подключения к базе данных и извлечения из нее информации на предмет продуктов и их категорий. 

# ОПИСАНИЕ КОМАНД ДЛЯ ЗАПУСКА ПРИЛОЖЕНИЯ

1. Клонировать проект:
```
git@github.com:irinaexzellent/HTTP-api-database.git
```

2. Перейти в папку HTTP-api-database и создать файл **.env-postgresql**

3. В файле **.env-postgresql** указать:
```
POSTGRES_USER=пароль пользователя базы данных
POSTGRES_PASSWORD=имя пользователя базы данных
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=имя базы данных
```
4. В папку API добавить файл **database.ini**:
```
[postgresql]
host=db
database=имя базы данных(должно совпадать с POSTGRES_DB в .env-postgresql)
user=имя пользователя базы данных(должно совпадать с POSTGRES_USER в .env-postgresql)
password=пароль пользователя базы данных(должно совпадать с POSTGRES_PASSWORD в .env-postgresql)
port=5432
```
5. Перейти в папку с файлом docker-compose.yml (HTTP-api-database) и выполнить:
```
docker-compose up -d
```
6. Перейти в pgAdmin http://127.0.0.1:5050/browser/ и создать базу данных
```
При регистрации в connection сервера указать host name - db (имя контенейра базы данных) 
```
Код создания базы данных и внесения информации в таблицы представлен - HTTP-api-database/API/SQL.sql

7. Перезапустить контейнер flask_web:
```
docker restart <id контейнера flask_web>
```
8. Проверить результаты работы по следующим адресам:

http://127.0.0.1:5000/api/v1/category-products - список всех продуктов с их категориями

http://127.0.0.1:5000/api/v1/pairs - список всех пар «Имя продукта – Имя категории»

http://127.0.0.1:5000/api/v1/category - список категорий с продуктами



Для остановки и удаления контейнеров, удаления volumes и образов:
```
docker kill $(docker ps -q) # stop all containers
docker rm $(docker ps -a -q) # remove all containers 
docker rmi $(docker images -q) # remove all images
docker network prune # remove all networks
docker volume prune # remove all volumes
```

## Автор

* **Ирина Иконникова** - (https://github.com/irinaexzellent)
