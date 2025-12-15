from fastapi import FastAPI
from routers.veiculo_router import router as veiculo_router


app = FastAPI(title="API Locadora de veículos")


app.include_router(veiculo_router)