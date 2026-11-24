
from datetime import datetime

from pydantic import BaseModel, ConfigDict, HttpUrl, Field


class URLCreate(BaseModel):
    original_url: HttpUrl

    custom_alias: str | None = Field(
        default=None,
        min_length=3,
        max_length=30,
        pattern=r"^[a-zA-Z0-9_-]+$",
    )

    expires_in_days: int | None = Field(
        default=None,
        ge=1,
        le=365,
    )


class URLResponse(BaseModel):
    code: str
    short_url: str
    original_url: str
    created_at: datetime
    expires_at: datetime | None
    click_count: int


class URLStatsResponse(BaseModel):
    code: str
    original_url: str
    created_at: datetime
    expires_at: datetime | None
    click_count: int
