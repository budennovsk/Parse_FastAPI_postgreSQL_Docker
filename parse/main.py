import requests
from fastapi import FastAPI

from parse.database import *
from parse.models import Quiz

app = FastAPI()


@app.get("/")
def get_display():
    return {'Answer': 'Пустой объект' if db.query(Quiz.id).count() <= 1 else db.query(Quiz).all()[:-1]}


@app.post("/")
def get_create(count):
    url = f'https://jservice.io/api/random?count={count}'
    response_data = requests.get(url).json()
    for items in response_data:
        while db.query(Quiz).filter(Quiz.id_question == items['id']).first() is not None:
            items = requests.get(
                url=f"https://jservice.io/api/random?count=1"
            ).json()
            print('True')

        answer_db = Quiz(
            id_question=items["id"],
            question=items["question"],
            answer=items["answer"],
            created_at=items['created_at']

        )
        db.add(answer_db)
        db.commit()
        db.refresh(answer_db)
