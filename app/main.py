"""Main configs."""

import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request

from app.core.config import settings
from app.home import routes


# API Metadata
tags_metadata = [
    {
        "name": "Home",
        "description": "Operations related to home",
    },
]

# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    summary="A JSON API created for the Coding Latam community.",
    description=("\nAccess the API documentation at `/docs` or `/redoc`."),
    version=str(os.environ.get("API_VERSION")),
    # terms_of_service="http://example.com/terms/",
    contact={
        "name": "Coding Latam GitHub",
        "url": "https://github.com/Coding-Latam",
    },
    license_info={
        "name": "MIT License",
        "url": "https://github.com/tyronejosee/project_coding_latam_api/blob/main/LICENSE",
    },
    debug=False,
    openapi_tags=tags_metadata,
    # servers=[
    #     {
    #         "url": "https://coding-latam-api.up.railway.app/",
    #         "description": "Production",
    #     },
    #     {
    #         "url": "http://127.0.0.1:8000/",
    #         "description": "Local",
    #     },
    # ],
    # docs_url="/swagger",
    # redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


# Redirect root to documentation
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


# Redirect to the documentation if the page is not found
@app.exception_handler(404)
async def not_found_error(request: Request, exc: Exception):
    return RedirectResponse(url="/docs")


# Serve static files
app.mount("/images", StaticFiles(directory=settings.STATIC_DIR), name="images")

# Include routers
app.include_router(routes.router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
