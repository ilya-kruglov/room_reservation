"""Импорты класса Base и всех моделей для Alembic."""
# alembic revision --autogenerate -m "Add Reservation model"
# alembic upgrade head
from app.core.db import Base  # noqa
from app.models.meeting_room import MeetingRoom  # noqa
from app.models.reservation import Reservation # noqa
