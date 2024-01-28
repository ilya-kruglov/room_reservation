from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.meeting_room import MeetingRoom


class CRUDMeetingRoom(CRUDBase):

    @staticmethod
    async def get_room_id_by_name(
            room_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_room_id = await session.execute(
            select(MeetingRoom.id).where(
                MeetingRoom.name == room_name
            )
        )
        db_room_id = db_room_id.scalars().first()
        return db_room_id

    async def get_by_id(
            self,
            room_id: int,
            session: AsyncSession,
    ) -> Optional[MeetingRoom]:
        return await self.get(room_id, session)


meeting_room_crud = CRUDMeetingRoom(MeetingRoom)
