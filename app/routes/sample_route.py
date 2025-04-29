from fastapi import APIRouter, Query
from typing import Annotated
from fastapi.responses import PlainTextResponse

from schema import SampleQuery, SampleRequest, SampleResponse

from tags import SAMPLE_TAG, SAMPLE_TAG2


router1 = APIRouter(prefix="/sample", tags=[SAMPLE_TAG.name])
router2 = APIRouter(prefix="/sample2", tags=[SAMPLE_TAG2.name])


@router1.get(
    "/",
    summary="get_sample sammary here",
    description="get_sample description here",
    operation_id="get_sample",
    response_class=PlainTextResponse,
)
async def get_sample(query: Annotated[SampleQuery, Query()]):
    pass


@router2.post(
    "/",
    summary="create_sample summary here",
    description="create_sample description here",
    operation_id="create_sample",
    response_model=SampleResponse,
)
async def create_item(request: SampleRequest):
    pass
