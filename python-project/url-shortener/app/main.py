
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import models
from app.database import Base, engine
from app.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables when the application starts
    Base.metadata.create_all(bind=engine)

    yield

    # Application shutdown


app = FastAPI(
    title="URL Shortener API",
    description="A professional URL shortening service built with FastAPI and MySQL.",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(router)
