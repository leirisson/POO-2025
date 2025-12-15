from fastapi import FastAPI
from routers.contas_route import router as contas_router

app = FastAPI(title="Exercício 2: Contas Bancárias Especiais")

app.include_router(contas_router)
