from pydantic import BaseModel

class ProfileCreate(BaseModel):
    user_id: int
    bio: str
