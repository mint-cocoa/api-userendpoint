# main.py
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, parks, tickets, purchases, facilities, users

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(parks.router)
app.include_router(tickets.router)
app.include_router(purchases.router)
app.include_router(facilities.router)
app.include_router(users.router)