from wazo_call_logd.http import AuthResource
from flask import request
from .schemas import StateCallOnQueueRequestSchema
from .services import StatCallOnQueueService
from xivo.auth_verifier import required_acl

# class _MultiTenantAuthResource(AuthResource):
#     def visible_tenants(self, recurse=True):
#         tenant_uuid = Tenant.autodetect().uuid
#         if recurse:
#             return [tenant.uuid for tenant in token.visible_tenants(tenant_uuid)]
#         else:
#             return [tenant_uuid]


class CallOnQueueStatByAgentResource(AuthResource):
    def __init__(self, service):
        super().__init__()
        self.service: StatCallOnQueueService = service

    @required_acl('call-logd.agents.statistics.read')
    def get(self, agent_id):
        args = StateCallOnQueueRequestSchema().load(request.args)
        # tenant_uuids = self.visible_tenants(recurse=True)
        # queue_stats = self.service.list(tenant_uuids, **args)
        call_on_queue_stats = self.service.get_stat_for_agent(agent_id = agent_id)
        return call_on_queue_stats
    

class CallOnQueueStatByQueueResource(AuthResource):
    def __init__(self, service):
        super().__init__()
        self.service: StatCallOnQueueService = service

    @required_acl('call-logd.agents.statistics.read')
    def get(self, queue_id):
        args = StateCallOnQueueRequestSchema().load(request.args)
        # tenant_uuids = self.visible_tenants(recurse=True)
        # queue_stats = self.service.list(tenant_uuids, **args)
        call_on_queue_stats = self.service.get_stat_for_queue(queue_id = queue_id)
        return call_on_queue_stats
    