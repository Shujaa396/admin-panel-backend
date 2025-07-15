# app/schemas/user.py

from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    is_active: bool
    role: str  # 👈 Add this too
