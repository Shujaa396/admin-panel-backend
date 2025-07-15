from sqlmodel import SQLModel, Field
from typing import Optional

class POSModule(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    is_active: bool = True
