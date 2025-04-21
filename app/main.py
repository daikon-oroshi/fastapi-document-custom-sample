from fastapi import FastAPI
import uvicorn
from routes.sample import router as sample_router
from tags import TAGS
from document.openapi_yaml import set_openapi_yaml
from document.openapi_custom_schema import set_custom_openapi


app = FastAPI(
    title="FastAPI Sample",
    description="FastAPI Sample Description",
    version="0.0.1",
    openapi_tags=TAGS,
)

app.include_router(sample_router)
set_openapi_yaml(app)
set_custom_openapi(app)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True)
