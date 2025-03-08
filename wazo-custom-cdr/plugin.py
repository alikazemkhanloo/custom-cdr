import logging

from .services import StatCallOnQueueService
from .http import CDRResource, CallOnQueueStatByAgentResource, CallOnQueueStatByQueueResource
from . import dao
from wazo_call_logd.plugins.cdr.services import CDRService, RecordingService
from wazo_auth_client import Client as AuthClient
from wazo_call_logd.plugins.export.notifier import ExportNotifier



logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        api = dependencies['api']
        config = dependencies['config']
        dao = dependencies['dao']
        bus_publisher = dependencies['bus_publisher']
        export_notifier = ExportNotifier(bus_publisher)

        auth_client = AuthClient(**config['auth'])
        cdr_service = CDRService(dao)
        recording_service = RecordingService(dao, config, export_notifier)

        api.add_resource(
            CDRResource,
            '/custom-cdr',
            resource_class_args=[cdr_service],
        )


        logger.info('!!!!!!!!!!!!! workano custom cdr plugin loaded!!!!')
