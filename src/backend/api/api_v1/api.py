from fastapi import APIRouter

from api.api_v1.endpoints import layouts
from api.api_v1.endpoints import solvers

api_router = APIRouter()
api_router.include_router(layouts.router, prefix="/layouts", tags=["layout"])
api_router.include_router(solvers.router, prefix="/solvers", tags=["solver"])
