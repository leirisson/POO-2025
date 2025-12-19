from fastapi import FastAPI
from routers.account_routers import router as account_router

app = FastAPI(title="SISTEMA BANCÁRIO")
app.include_router(account_router, prefix="/accounts", tags=["Accounts"])