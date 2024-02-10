"""Импорты класса Base и всех моделей для Alembic."""
# alembic revision --autogenerate -m "Add Reservation model"
# alembic upgrade head
from app.core.db import Base  # noqa
from app.models import MeetingRoom, Reservation, User  # noqa
