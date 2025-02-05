import logging

from .services import StatCallOnQueueService
from .http import CallOnQueueStatByAgentResource, CallOnQueueStatByQueueResource
from . import dao

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        api = dependencies['api']

        state_call_on_queue_service = StatCallOnQueueService(dao)

        api.add_resource(
            CallOnQueueStatByAgentResource,
            '/agents/<int:agent_id>/call-on-queue-stat/',
            resource_class_args=(state_call_on_queue_service,)
        )

        api.add_resource(
            CallOnQueueStatByQueueResource,
            '/queues/<int:queue_id>/call-on-queue-stat/',
            resource_class_args=(state_call_on_queue_service,)
        )

            # '/queues/<int:queue_id>/call-on-queue-stat/',


        logger.info('!!!!!!!!!!!!! workano survey plugin loaded!!!!')
