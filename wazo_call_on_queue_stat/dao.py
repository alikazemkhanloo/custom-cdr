
from xivo_dao.helpers.db_manager import daosession
from xivo_dao.alchemy.stat_call_on_queue import StatCallOnQueue
from xivo_dao.alchemy.stat_agent import StatAgent
from xivo_dao.alchemy.stat_queue import StatQueue
from sqlalchemy import func, text

@daosession
def get_call_on_queue_stat_by_agent(session , agent_id):
    query = (
        session.query(
            func.min(StatAgent.agent_id).label('agent_id'),
            func.min(StatAgent.queue_id).label('queue_id'),
            func.min(StatAgent.number).label('agent_number'),
            func.sum(StatCallOnQueue.talktime).label('talktime'),
        )
        .select_from(StatCallOnQueue)
        .filter(StatAgent.agent_id == agent_id)
        .join(StatAgent)
        .join(StatQueue)
        .group_by(StatCallOnQueue.stat_queue_id)
        .group_by(StatCallOnQueue.status)
    )
    print(str(query.statement))
    all_stats = query.all()
    return all_stats
