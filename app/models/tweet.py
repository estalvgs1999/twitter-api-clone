# Python
from datetime import datetime
from typing import Optional

# Pydantic
from uuid import UUID
from pydantic.fields import Field
from pydantic.main import BaseModel

# Models
from app.models.user import User


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)
