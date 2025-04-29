from fastapi.openapi.models import Tag


SAMPLE_TAG = Tag(
    name="Sample Tag",
    description="sample tag description here (サンプルタグの description)",
    external_docs={
        "description": "sample tag external docs description here",
        "url": "https://example.com/sample",
    },
)

SAMPLE_TAG2 = Tag(
    name="Sample Tag 2",
    description="sample tag 2 description here (サンプルタグ2の description)",
    external_docs={
        "description": "sample tag 2 external doc description here",
        "url": "https://example.com/sample2",
    },
)

TAGS = [SAMPLE_TAG, SAMPLE_TAG2]
