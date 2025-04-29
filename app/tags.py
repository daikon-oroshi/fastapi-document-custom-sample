from fastapi.openapi.models import Tag


SAMPLE_TAG = Tag(
    name="SampleTag",
    description="sample tag description here (サンプルタグの description)",
    external_docs={
        "description": "sample tag external docs description here",
        "url": "https://example.com/sample",
    },
)


SAMPLE_TAG2_DESCRIPTION = """
## sample tag **description** here (サンプルタグの description)
- aaaa
"""


SAMPLE_TAG2 = Tag(
    name="SampleTag2",
    description=SAMPLE_TAG2_DESCRIPTION,
)

TAGS = [SAMPLE_TAG, SAMPLE_TAG2]
