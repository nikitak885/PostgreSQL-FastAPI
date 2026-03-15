from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base



class questions(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)

class choice(Base):
    __tablename__ = "choice"

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("question.id"))


