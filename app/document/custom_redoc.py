from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json


def set_custom_redoc(app: FastAPI) -> None:
    """
    FastAPIのRedocの設定を行う関数
    """

    def redoc_html():
        return get_redoc_html(
            openapi_url=app.openapi_url,
            title=app.title,
            theme={"sidebar": {"backgroundColor": "lightblue"}},
        )

    app.add_api_route(
        "/redoc",
        redoc_html,
        methods=["GET"],
        include_in_schema=False,
    )


# @see https://github.com/fastapi/fastapi/blob/26dc148cb91f9ec679b7cf1a74f5a6d6747e7e00/fastapi/openapi/docs.py#L161  # noqa: E501
#
# How to set redoc parameter https://redocly.com/docs/redoc/deployment/html
# Redoc parameters https://redocly.com/docs-legacy/api-reference-docs/configuration/functionality  # noqa: E501
def get_redoc_html(
    openapi_url: str = "/openapi.json",
    title: str = "FastAPI Sample API",
    redoc_js_url: str = (
        "https://cdn.jsdelivr.net/npm/redoc@2/bundles/redoc.standalone.js"
    ),
    redoc_favicon_url: str = "https://fastapi.tiangolo.com/img/favicon.png",
    with_google_fonts: bool = True,
    theme: dict = None,
) -> HTMLResponse:
    """
    Generate and return the HTML response that loads ReDoc for the alternative
    API docs (normally served at `/redoc`).

    You would only call this function yourself if you needed to override some parts,
    for example the URLs to use to load ReDoc's JavaScript and CSS.

    Read more about it in the
    [FastAPI docs for Custom Docs UI Static Assets (Self-Hosting)](https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/).
    """  # noqa: E501

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>{title}</title>
    <!-- needed for adaptive design -->
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    """
    if with_google_fonts:
        html += """
    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">
    """  # noqa: E501
    html += f"""
    <link rel="shortcut icon" href="{redoc_favicon_url}">
    <!--
    ReDoc doesn't change outer page styles
    -->
    <style>
      body {{
        margin: 0;
        padding: 0;
      }}
    </style>
    </head>
    <body>
    <noscript>
        ReDoc requires Javascript to function. Please enable it to browse the documentation.
    </noscript>
    <redoc
        spec-url="{openapi_url}"
        disable-search="true"
        hide-download-button="true"
    """  # noqa: E501
    if theme is not None:
        html += f"""
            theme='{json.dumps(theme)}'
        """
    html += f"""
    ></redoc>
    <script src="{redoc_js_url}"> </script>
    </body>
    </html>
    """
    return HTMLResponse(html)
