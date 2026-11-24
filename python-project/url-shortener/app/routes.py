
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.repository import increment_click_count
from app.schemas import URLCreate, URLResponse, URLStatsResponse
from app.services import (
    AliasTakenError,
    CodeGenerationError,
    ReservedAliasError,
    UrlExpiredError,
    UrlNotFoundError,
    create_short_url,
    get_active_url,
)


router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "healthy"}


@router.post(
    "/api/shorten",
    response_model=URLResponse,
    status_code=status.HTTP_201_CREATED,
)
def shorten_url(
    request: URLCreate,
    db: Session = Depends(get_db),
):
    try:
        url = create_short_url(db, request)

        return URLResponse(
            code=url.code,
            short_url=f"{settings.base_url.rstrip('/')}/{url.code}",
            original_url=url.original_url,
            created_at=url.created_at,
            expires_at=url.expires_at,
            click_count=url.click_count,
        )

    except AliasTakenError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc

    except ReservedAliasError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

    except CodeGenerationError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        ) from exc


@router.get(
    "/api/stats/{code}",
    response_model=URLStatsResponse,
)
def get_url_stats(
    code: str,
    db: Session = Depends(get_db),
):
    try:
        url = get_active_url(db, code)

        return URLStatsResponse(
            code=url.code,
            original_url=url.original_url,
            created_at=url.created_at,
            expires_at=url.expires_at,
            click_count=url.click_count,
        )

    except UrlNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    except UrlExpiredError as exc:
        raise HTTPException(
            status_code=status.HTTP_410_GONE,
            detail=str(exc),
        ) from exc


# Keep this catch-all route LAST.
@router.get("/{code}")
def redirect_url(
    code: str,
    db: Session = Depends(get_db),
):
    try:
        url = get_active_url(db, code)

        increment_click_count(db, code)

        return RedirectResponse(
            url=url.original_url,
            status_code=status.HTTP_302_FOUND,
        )

    except UrlNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    except UrlExpiredError as exc:
        raise HTTPException(
            status_code=status.HTTP_410_GONE,
            detail=str(exc),
        ) from exc
