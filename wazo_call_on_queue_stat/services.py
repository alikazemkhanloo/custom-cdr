from wazo_call_on_queue_stat.schemas import CallOnStatQueueResultSchema
from . import dao

class StatCallOnQueueService():
    def __init__(self, _dao):
        self.dao: dao = _dao

    def get_stat_for_agent(self, agent_id):
        result = self.dao.get_call_on_queue_stat_by_agent(agent_id=agent_id)
        return CallOnStatQueueResultSchema().dump(result)
    
    def get_stat_for_queue(self, queue_id):
        result = self.dao.get_call_on_queue_stat_by_queue(queue_id=queue_id)
        return CallOnStatQueueResultSchema().dump(result)
