from . import dao

class StatCallOnQueueService():
    def __init__(self, _dao):
        self.dao: dao = _dao

    def get_stat_for_agent(self, agent_id):
        return self.dao.get_call_on_queue_stat_by_agent(agent_id)