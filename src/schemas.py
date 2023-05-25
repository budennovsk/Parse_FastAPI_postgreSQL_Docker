
from pydantic import BaseModel


class CreateQuiz(BaseModel):
    id_question = int
    question = str
    answer = str


    class Config:
        orm_mode = True
