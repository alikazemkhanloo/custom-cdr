
from xivo_dao.helpers.db_manager import daosession
from xivo_dao.alchemy.stat_call_on_queue import StatCallOnQueue
from xivo_dao.alchemy.stat_agent import StatAgent
from xivo_dao.alchemy.stat_queue import StatQueue
from sqlalchemy import func, text

from .schemas import CallOnStatQueueResultSchema

@daosession
def get_call_on_queue_stat_by_agent(session , agent_id):
    query = (
        session.query(
            func.min(StatAgent.agent_id),
            func.min(StatQueue.queue_id),
            func.min(StatAgent.number).label('agent_number'),
            func.sum(StatCallOnQueue.talktime),
            func.sum(StatCallOnQueue.ringtime),
            func.sum(StatCallOnQueue.waittime),
            func.count(StatCallOnQueue.status)
        )
        .select_from(StatCallOnQueue)
        .filter(StatAgent.agent_id == agent_id)
        .join(StatAgent)
        .join(StatQueue)
        .group_by(StatCallOnQueue.stat_queue_id)
        .group_by(StatCallOnQueue.status)
    )

    return query.all()

@daosession
def get_call_on_queue_stat_by_queue(session , queue_id):
    query = (
        session.query(
            func.min(StatAgent.agent_id),
            func.min(StatQueue.queue_id),
            func.min(StatAgent.number).label('agent_number'),
            func.sum(StatCallOnQueue.talktime),
            func.sum(StatCallOnQueue.ringtime),
            func.sum(StatCallOnQueue.waittime),
            func.count(StatCallOnQueue.status)
        )
        .select_from(StatCallOnQueue)
        .filter(StatQueue.queue_id == queue_id)
        .join(StatAgent)
        .join(StatQueue)
        .group_by(StatCallOnQueue.stat_agent_id)
        .group_by(StatCallOnQueue.status)
    )

    return query.all()
