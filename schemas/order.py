from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class OrderCreate(BaseModel):
    customer_name: str
    email: EmailStr
    shoe_model: str
    size: int
    customization_note: Optional[str] = None
    image_url: Optional[str] = None

class OrderOut(OrderCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
