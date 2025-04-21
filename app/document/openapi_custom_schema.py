from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from schema.sample_query import SampleQuery


def set_custom_openapi(app: FastAPI) -> None:

    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title=app.title,
            version=app.version,
            summary=app.summary,
            description=app.description,
            routes=app.routes,
        )
        openapi_schema["info"]["x-logo"] = {
            "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
        }

        queires = [SampleQuery]
        for query in queires:
            schema = query.model_json_schema(
                ref_template="#/components/schemas/{model}"
            )
            del schema["$defs"]
            openapi_schema["components"]["schemas"][query.__name__] = schema

        return openapi_schema

    app.openapi = custom_openapi
