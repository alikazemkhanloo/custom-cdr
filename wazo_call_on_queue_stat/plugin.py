import logging

from .services import StatCallOnQueueService
from .http import CallOnQueueStatResource
from . import dao

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        api = dependencies['api']

        state_call_on_queue_service = StatCallOnQueueService(dao)

        api.add_resource(
            CallOnQueueStatResource,
            '/call-on-queue-stat/agents/<int:agent_id>/',
            resource_class_args=(state_call_on_queue_service,)
        )

            # '/call-on-queue-stat/queues/<int:queue_id>/',


        logger.info('!!!!!!!!!!!!! workano survey plugin loaded!!!!')
