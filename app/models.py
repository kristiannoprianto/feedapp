from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, TIMESTAMP, text
from sqlalchemy.orm import relationship
from .database import Base

class FeedbackRate(Base):
    __tablename__ = "feedbackrates"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    rating = Column(Integer, nullable=False, default=0)
