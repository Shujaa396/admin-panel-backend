from fastapi import FastAPI
from app.routes import ping, user, profile, subscription, pos_module
from app.database.connection import create_db_and_tables

app = FastAPI()

# 🔁 Create tables at startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Include routes
app.include_router(ping.router)
app.include_router(user.router)
app.include_router(profile.router)
app.include_router(subscription.router)
app.include_router(pos_module.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the backend!"}
