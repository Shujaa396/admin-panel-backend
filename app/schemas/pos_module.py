from pydantic import BaseModel

class POSModuleCreate(BaseModel):
    name: str
    is_active: bool = True

