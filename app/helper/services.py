from app.database.schema import Content
from sqlalchemy.orm import Session


def get_content_total_pages(session: Session = None, writer_id: str = '', count: int = 10):
    total_count = Content.get_content_total_count(session, writer_id)
    result = ((total_count - 1) / count) + 1
    return int(result)
