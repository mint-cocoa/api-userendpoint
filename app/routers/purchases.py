# routers/purchases.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, models, dependencies
from app.dependencies import get_db
from app.utils.qr_gen import generate_qr_code  # QR 코드 생성 함수 임포트

router = APIRouter(
    prefix="/purchases",
    tags=["purchases"],
)   

@router.post("/", response_model=schemas.Purchase)
def create_purchase(
    purchase: schemas.PurchaseCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(dependencies.get_current_active_user)
):
    # 티켓 존재 여부 확인
    ticket = crud.ticket.get_ticket_by_id(db, ticket_id=purchase.ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="티켓을 찾을 수 없습니다.")

    # 구매 생성
    db_purchase = crud.purchase.create_purchase(db=db, purchase=purchase, user_id=current_user.id)

    # QR 코드에 포함할 데이터 생성
    qr_data = {
        "purchase_id": db_purchase.id,
        "user_id": current_user.id,
        "ticket_id": ticket.id,
        "quantity": purchase.quantity,
        "purchase_date": db_purchase.purchase_date.isoformat()
    }

    # QR 코드 생성
    import json
    qr_data_str = json.dumps(qr_data)
    qr_code_base64 = generate_qr_code(qr_data_str)

    # 응답 객체 생성
    response_purchase = schemas.Purchase(
        id=db_purchase.id,
        user_id=current_user.id,
        ticket_id=ticket.id,
        quantity=purchase.quantity,
        purchase_date=db_purchase.purchase_date,
        qr_code=qr_code_base64
    )

    return response_purchase
