# main.py
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, parks, tickets, purchases

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(parks.router, prefix="/parks", tags=["parks"])
app.include_router(tickets.router, prefix="/tickets", tags=["tickets"])
app.include_router(purchases.router, prefix="/purchases", tags=["purchases"])
