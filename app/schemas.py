from pydantic import BaseModel, Field

class FeedbackRatingModel(BaseModel):
    rating: int = Field(0, ge=1, le=5)
