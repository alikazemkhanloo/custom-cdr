import logging

from .dao import CallLogDAO

from .http import CustomCDRResource
from wazo_call_logd.plugins.cdr.services import  RecordingService
from wazo_auth_client import Client as AuthClient
from wazo_call_logd.plugins.export.notifier import ExportNotifier
from .services import CDRService
from xivo_dao.helpers.db_manager import daosession


logger = logging.getLogger(__name__)


class Plugin:
    @daosession
    def getDao(session, self):
        dao  = CallLogDAO(session)
        return dao
        
        
    def load(self, dependencies):
        api = dependencies['api']
        dao = self.getDao()
        cdr_service = CDRService(dao)

        api.add_resource(
            CustomCDRResource,
            '/custom-cdr',
            resource_class_args=[cdr_service],
        )


        logger.info('!!!!!!!!!!!!! workano custom cdr plugin loaded!!!!')
