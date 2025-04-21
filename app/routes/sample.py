from fastapi import APIRouter, Query
from typing import Annotated
from schema.sample_query import SampleQuery
from fastapi.responses import PlainTextResponse


router = APIRouter(prefix="/sample", tags=["sample"])


@router.get(
    "/",
    summary="sammary here",
    description="description here",
    operation_id="get_sample",
    response_class=PlainTextResponse,
)
async def get_sample(query: Annotated[SampleQuery, Query()]):
    print(query)
    return "OK"


@router.post("/")
async def create_item(item: dict):
    return {"item": item}
