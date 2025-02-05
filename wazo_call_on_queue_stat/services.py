from . import dao


class StatCallOnQueueService:
    def __init__(self, _dao):
        self.dao: dao = _dao

    def get_stat_for_agent(self, agent_id, tenant_uuid, **args):
        result = self.dao.get_call_on_queue_stat_by_agent(
            agent_id=agent_id, tenant_uuid=tenant_uuid, **args
        )
        output = [row._as_dict() for row in result]
        return output

    def get_stat_for_queue(self, queue_id, tenant_uuid, **args):
        result = self.dao.get_call_on_queue_stat_by_queue(
            queue_id=queue_id, tenant_uuid=tenant_uuid, **args
        )
        output = [row._as_dict() for row in result]
        return output
