
from datetime import datetime, timedelta, timezone
import secrets
import string

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.config import settings
from app.models import URL
from app.repository import create_url, get_url_by_code


# Characters used to generate short URL codes
CHARACTERS = string.ascii_letters + string.digits

# Aliases that must not be used by customers
RESERVED_ALIASES = {
    "api",
    "docs",
    "redoc",
    "openapi",
    "health",
    "admin",
}


# Application-specific exceptions
class AliasTakenError(Exception):
    pass


class ReservedAliasError(Exception):
    pass


class UrlNotFoundError(Exception):
    pass


class UrlExpiredError(Exception):
    pass


class CodeGenerationError(Exception):
    pass


def generate_short_code() -> str:
    return "".join(
        secrets.choice(CHARACTERS)
        for _ in range(settings.code_length)
    )


def create_short_url(db: Session, request) -> URL:
    original_url = str(request.original_url)

    expires_at = None

    if request.expires_in_days is not None:
        expires_at = (
            datetime.now(timezone.utc)
            + timedelta(days=request.expires_in_days)
        ).replace(tzinfo=None)

    # Handle a user-provided custom alias
    if request.custom_alias:
        alias = request.custom_alias

        if alias.lower() in RESERVED_ALIASES:
            raise ReservedAliasError(
                f"The alias '{alias}' is reserved."
            )

        url = URL(
            code=alias,
            original_url=original_url,
            expires_at=expires_at,
        )

        try:
            return create_url(db, url)
        except IntegrityError as exc:
            raise AliasTakenError(
                f"The alias '{alias}' is already taken."
            ) from exc

    # Generate a random code and retry if a collision occurs
    for _ in range(5):
        code = generate_short_code()

        url = URL(
            code=code,
            original_url=original_url,
            expires_at=expires_at,
        )

        try:
            return create_url(db, url)
        except IntegrityError:
            continue

    raise CodeGenerationError(
        "Could not generate a unique short URL. Please try again."
    )


def get_active_url(db: Session, code: str) -> URL:
    url = get_url_by_code(db, code)

    if url is None:
        raise UrlNotFoundError(
            f"No URL found for code '{code}'."
        )

    if url.expires_at is not None:
        current_time = datetime.now(timezone.utc).replace(tzinfo=None)

        if url.expires_at <= current_time:
            raise UrlExpiredError(
                f"The URL for code '{code}' has expired."
            )

    return url
