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

### Home Swagger UI

<img src="https://github.com/budennovsk/Parse_FastAPI_postgreSQL_Docker/assets/97764479/601c558a-20e7-431b-a067-eaa4f89e18bb" width=70% height=70%>
<br>

### GET запрос 

<img src="https://github.com/budennovsk/Parse_FastAPI_postgreSQL_Docker/assets/97764479/bb217ea6-9a90-4918-8154-453940773295" width=70% height=70%>

### POST запрос с добавлением 3 записей в БД

<img src="https://github.com/budennovsk/Parse_FastAPI_postgreSQL_Docker/assets/97764479/e08a6c8e-ac7f-4a37-8f23-ef69feb4e6ee" width=70% height=70%>

### Result

<img src="https://github.com/budennovsk/Parse_FastAPI_postgreSQL_Docker/assets/97764479/29388752-1ad6-492c-84f8-46ff446b5122" width=70% height=70%>



