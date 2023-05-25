
import requests
from fastapi import FastAPI, status, Depends

from src.database import SessionLocal
from src.models import Quiz
from src.schemas import CreateQuiz
from sqlalchemy.orm import Session

# приложение
app = FastAPI()


# определяем зависимость
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=CreateQuiz, status_code=status.HTTP_200_OK)
def get_display(db: Session = Depends(get_db)):
    """ Отображение списка БД кроме последней записи, и первой """
    row = [
        'Пустой объект'
        if db.query(Quiz.id).count() <= 1 else
        {
            'id': i.id,
            'id_question': i.id_question,
            'question': i.question,
            'answer': i.answer,

        }

        for i in db.query(Quiz).all()[:-1]
    ]
    for it in row:
        return CreateQuiz(**it)


@app.post("/", status_code=status.HTTP_201_CREATED)
def get_create(count: int, db: Session = Depends(get_db)) -> None:
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
