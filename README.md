# Parse_FastAPI_postgreSQL_Docker использовал:
*  SQL db PostgreSQL
*  FastAPI 
*  SQLAlchemy
*  Docker-compose
___
## Тестовое задание №1 от bewise.ai 
1. С помощью Docker (предпочтительно - docker-compose) развернуть образ с любой опенсорсной СУБД (предпочтительно - PostgreSQL). 
Предоставить все необходимые скрипты и конфигурационные (docker/compose) файлы для развертывания СУБД, а также инструкции для подключения к ней. 
Необходимо обеспечить сохранность данных при рестарте контейнера (то есть - использовать volume-ы для хранения файлов СУБД на хост-машине.
2. Реализовать на Python3 веб сервис (с помощью FastAPI или Flask, например), выполняющий следующие функции:

    2.1. В сервисе должно быть реализован POST REST метод, принимающий на вход запросы с содержимым вида {"questions_num": integer}.
    
    2.2 После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.
    
    2.3 Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация (название колонок и типы данный можете выбрать сами, также можете добавлять свои колонки): 1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса. В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
    
    2.4 Ответом на запрос из п.2.a должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.
    
3. В репозитории с заданием должны быть предоставлены инструкции по сборке докер-образа с сервисом из п. 2., его настройке и запуску. А также пример запроса к POST API сервиса.
4. Желательно, если при выполнении задания вы будете использовать docker-compose, SQLAalchemy,  пользоваться аннотацией типов.

___
## Stack:
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

___

### Home


<img src="![1](https://github.com/budennovsk/Parse_FastAPI_postgreSQL_Docker/assets/97764479/629daea3-3ae3-44e5-ae63-7614a684cd1d" width=70% height=70%>
<br>

### Depatamets
<img src="https://github.com/budennovsk/DRF_PostgreSQL_React/assets/97764479/d85f3712-4eac-4134-8730-0abc47067cfd" width=70% height=70%>

### Udpate
<img src="https://github.com/budennovsk/DRF_PostgreSQL_React/assets/97764479/c1f14438-7321-49b3-a495-47993e2220c3" width=70% height=70%>

### Delete

<img src="https://github.com/budennovsk/DRF_PostgreSQL_React/assets/97764479/9a5e3c8e-0781-4711-8ce8-2e14c5c85155" width=70% height=70%>

### Result

<img src="https://github.com/budennovsk/DRF_PostgreSQL_React/assets/97764479/b177e476-2409-48b2-8c45-22d2e4fc2aed" width=70% height=70%>

### Employees

<img src="https://github.com/budennovsk/DRF_PostgreSQL_React/assets/97764479/2986cb76-2dce-41a3-ab6f-81d01e1382b0" width=70% height=70%>

### Create

<img src="https://github.com/budennovsk/DRF_PostgreSQL_React/assets/97764479/1c8bc92d-7418-438c-9d5b-9c492c555e99" width=70% height=70%>

### PostgreSQL

<img src="https://github.com/budennovsk/DRF_PostgreSQL_React/assets/97764479/665eb959-5952-43d7-a6e1-d3f658fcb938" width=70% height=70%>



