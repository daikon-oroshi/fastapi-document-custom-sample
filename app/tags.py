from fastapi.openapi.models import Tag


SAMPLE_TAG = Tag(
    name="sample",
    description="sample tag description here",
    external_docs={
        "description": "sample tag external docs description here",
        "url": "https://example.com/sample",
    },
)

TAGS = [
    SAMPLE_TAG,
]
