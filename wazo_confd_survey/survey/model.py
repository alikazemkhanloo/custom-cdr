from __future__ import unicode_literals

from sqlalchemy.schema import (
    Column,
    Index,
    ForeignKey,
    PrimaryKeyConstraint,
    UniqueConstraint,
)

from sqlalchemy.sql.schema import CheckConstraint
from sqlalchemy.types import Integer, String, Text, Enum
from sqlalchemy.dialects.postgresql import ARRAY

from xivo_dao.alchemy import enum
from xivo_dao.helpers.db_manager import Base, UUIDAsString


from ..db import Base


class QueueFeaturesModel(Base):
    __tablename__ = 'plugin_queue_workano_features'

    id = Column(Integer, nullable=False)
    tenant_uuid = Column(UUIDAsString(36), nullable=False)
    queue_id = Column(String(50), nullable=True)
    play_agentnumber_enable = Column(String(10), nullable=True)
    queue_survey_enable = Column(String(10), nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id'),
        UniqueConstraint('tenant_uuid', 'queue_id'),
    )


class SurveyModel(Base):
    __tablename__ = 'plugin_survey'

    id = Column(Integer, nullable=False)
    tenant_uuid = Column(UUIDAsString(36), nullable=False)
    agent_id = Column(String(128), nullable=True)
    agent_number = Column(String(128), nullable=True)
    queue_id = Column(String(128), nullable=True)
    queue_name = Column(String(128), nullable=True)
    queue_number = Column(String(128), nullable=True)
    queue_exten = Column(String(128), nullable=True)
    caller_id = Column(String(128), nullable=True)
    call_id = Column(String(128), nullable=True)
    timestamp = Column(String(50), nullable=True)
    rate = Column(String(50), nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id'),
    )
