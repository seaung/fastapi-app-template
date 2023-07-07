from fastapi import APIRouter


from api import api


api_route = APIRouter()


api_route.include_router(api.rotue, prefix="/v1", tags=["演示demoAPI"])

