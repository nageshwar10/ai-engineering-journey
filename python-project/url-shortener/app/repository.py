
from sqlalchemy import select, update
from sqlalchemy.orm import Session

from app.models import URL


def create_url(db: Session, url: URL) -> URL:
    try:
        db.add(url)
        db.commit()
        db.refresh(url)
        return url
    except Exception:
        db.rollback()
        raise


def get_url_by_code(db: Session, code: str) -> URL | None:
    statement = select(URL).where(URL.code == code)

    return db.execute(statement).scalar_one_or_none()


def increment_click_count(db: Session, code: str) -> bool:
    statement = (
        update(URL)
        .where(URL.code == code)
        .values(click_count=URL.click_count + 1)
    )

    result = db.execute(statement)
    db.commit()

    return result.rowcount == 1
