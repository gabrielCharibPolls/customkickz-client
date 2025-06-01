from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.order import OrderCreate, OrderOut
from app.crud.order import create_order

router = APIRouter()

@router.post("/submit", response_model=OrderOut)
def submit_order(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, order)
