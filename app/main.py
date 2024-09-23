from fastapi import FastAPI
from .routers import auth, users, parks, facilities, tickets, purchases
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(parks.router)
app.include_router(facilities.router)
app.include_router(tickets.router)
app.include_router(purchases.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Park Management System"}
