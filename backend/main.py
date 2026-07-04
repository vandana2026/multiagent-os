from fastapi import FastAPI
from app.api.routes import router
from app.core.settings import settings
from app.core.logger import app_logger

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)

app.include_router(router)


@app.on_event("startup")
async def startup():
    app_logger.info("🚀 MultiAgent OS Started Successfully")


@app.on_event("shutdown")
async def shutdown():
    app_logger.info("🛑 MultiAgent OS Stopped")