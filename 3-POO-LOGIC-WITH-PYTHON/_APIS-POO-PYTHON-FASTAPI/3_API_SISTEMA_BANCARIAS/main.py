from fastapi import FastAPI
from router.account_routers import router as account_router

app = FastAPI(title="SISTEMA DE CONTAS BANCÁRIAS")

app.include_router(account_router, prefix="/api/v1", tags=["Account"])