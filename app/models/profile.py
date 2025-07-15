from sqlmodel import SQLModel, Field
from typing import Optional

class Profile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    bio: str
