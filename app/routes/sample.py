from fastapi import APIRouter, Depends
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
async def get_sample(
    query: SampleQuery = Depends(SampleQuery),
):
    print(query)
    return "OK"


@router.post("/")
async def create_item(item: dict):
    return {"item": item}
