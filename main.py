from fastapi import FastAPI
from loguru import logger
from routes import auth_routes, product_routes
from routes.product_routes import router as product_router

from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure Store API")

app.include_router(product_router)
logger.add("logs/api.log", rotation= "1 MB")

app.include_router(auth_routes.router)
app.include_router(product_routes.router)

@app.get("/")
def home():
    logger.info("API en funcionamiento")
    return {"status": "SecureStore API running"}
