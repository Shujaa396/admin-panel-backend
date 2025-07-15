# app/models/user.py

from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    is_active: bool
    created_at: datetime
    role: str  # 👈 "admin" or "user"
