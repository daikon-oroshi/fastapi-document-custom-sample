from fastapi import FastAPI, Response
from functools import lru_cache
import yaml


def set_openapi_yaml(app: FastAPI) -> None:
    """
    Set the path to the OpenAPI YAML file.
    """

    @lru_cache()
    def read_openapi_yaml() -> Response:
        openapi_json = app.openapi()
        yaml_s = yaml.dump(openapi_json, Dumper=yaml.CDumper)
        return Response(yaml_s, media_type="text/yaml")

    app.add_api_route(
        "/openapi.yaml",
        read_openapi_yaml,
        methods=["GET"],
        include_in_schema=False,
    )
