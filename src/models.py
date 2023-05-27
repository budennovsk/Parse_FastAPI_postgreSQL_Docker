from sqlalchemy import Column, Integer, Text, DateTime

from src.database import Base, engine


# создаем модель хранения ответов от сервиса
class Quiz(Base):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True)
    id_question = Column(Integer, unique=True)
    question = Column(Text)
    answer = Column(Text)
    created_at = Column(DateTime)

    def __repr__(self):
        return f'<Quiz {self.id!r},{self.question!r},{self.answer!r}>'


# создаем таблицы
Base.metadata.create_all(bind=engine)
