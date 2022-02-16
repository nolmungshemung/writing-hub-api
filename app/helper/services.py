from app.database.schema import Content
from sqlalchemy.orm import Session


def get_content_total_pages(session: Session = None, writer_id: str = ''):
    total_count = Content.get_content_total_count(session, writer_id)
    result = ((total_count - 1) / 9) + 1
    return int(result)
