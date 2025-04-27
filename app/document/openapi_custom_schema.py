from typing import Any
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from schema.sample_query import SampleQuery
from pydantic import BaseModel


def set_custom_openapi(app: FastAPI) -> None:

    def query_schema(query_cls: type[BaseModel]) -> tuple[str, dict[str, Any]]:
        schema = query_cls.model_json_schema(
            ref_template="#/components/schemas/{model}"
        )
        # 余計なので削除
        del schema["$defs"]
        # default null だと optional にならないので削除
        for value in schema["properties"].values():
            if "default" in value.keys() and value["default"] is None:
                del value["default"]

        return query_cls.__name__, schema

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

        # query parameter は schema に追加されないのでここで追加
        queires: list[type[BaseModel]] = [SampleQuery]
        for query in queires:
            q_name, q_schema = query_schema(query)

            openapi_schema["components"]["schemas"][q_name] = q_schema

        return openapi_schema

    app.openapi = custom_openapi
