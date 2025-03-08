import logging

from .dao import CallLogDAO

from .http import CustomCDRResource
from wazo_call_logd.plugins.cdr.services import CDRService, RecordingService
from wazo_auth_client import Client as AuthClient
from wazo_call_logd.plugins.export.notifier import ExportNotifier



logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        api = dependencies['api']
        dao = dependencies['dao']
        dao._dao.call_logd = CallLogDAO
        cdr_service = CDRService(dao)

        api.add_resource(
            CustomCDRResource,
            '/custom-cdr',
            resource_class_args=[cdr_service],
        )


        logger.info('!!!!!!!!!!!!! workano custom cdr plugin loaded!!!!')
