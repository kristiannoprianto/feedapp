from operator import and_
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/feedback",
    tags=['Feedbacks']
)

@router.post("/")
def save_rating(payload: schemas.FeedbackRatingModel, db: Session = Depends(get_db)):
    add_rating = models.FeedbackRate(**payload.model_dump())

    db.add(add_rating)
    db.commit()
    db.refresh(add_rating)

    if add_rating.rating < 5:
        resp_content = "Thank you for your feedback. We will try to improve our product"
    elif add_rating.rating == 5:
        resp_content = "Thank you for loving our products!"
    return {"response": resp_content}
