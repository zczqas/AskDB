from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import settings

# from app.db.database import Base, engine
from app.urls import InitializeRouter

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_version="3.1.0",
)

media_directory = Path(settings.MEDIA_PATH)
app.mount("/media", StaticFiles(directory=media_directory), name="media")

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


InitializeRouter(app)


@app.get("/")
async def root():
    return {"status": f"{settings.PROJECT_NAME} is okay and running."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
