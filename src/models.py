from sqlalchemy import Column, Integer, Text, Date
from datetime import date
from src.database import Base, engine


# создаем модель хранения ответов от сервиса
class Quiz(Base):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True)
    id_question = Column(Integer, unique=True)
    question = Column(Text)
    answer = Column(Text)
    created_at = Column(Date)

    def __init__(self, id_question: int = None, question: str = None, answer: str = None,
                 created_at: date = date.today()):
        self.id_question = id_question
        self.question = question
        self.answer = answer
        self.created_at = created_at

    def __repr__(self):
        return f'<Quiz {self.id!r},{self.question!r},{self.answer!r}>'


# создаем таблицы
Base.metadata.create_all(bind=engine)
