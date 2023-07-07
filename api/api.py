from fastapi import APIRouter


rotue = APIRouter()

@rotue.get(path="/demo", summary="demo API")
def demon():
    return {"demo": "demo api"}

