from wazo_confd.helpers.resource import CRUDService

from . import dao
from .notifier import build_survey_notifier, build_queuefeature_notifier
from .validator import build_survey_validator, build_queuefeature_validator


class SurveyService(CRUDService):
    def get_all_surveys(self, tenant_uuid, queue_id):
        return dao.get_all_surveys(tenant_uuid, queue_id)

    def get_all_survey_by_queue_id(self, tenant_uuid, queue_id):
        return dao.get_all_survey_by_queue_id(tenant_uuid, queue_id)

    def get_all_survey_by_agent_id(self, tenant_uuid, agent_id):
        return dao.get_all_survey_by_agent_id(tenant_uuid, agent_id)

    def get_average_survey_by_agent_id(self, tenant_uuid, agent_id, from_date, until_date):
        return dao.get_average_survey_by_agent_id(tenant_uuid, agent_id, from_date, until_date)

    def get_average_survey_all_agent(self, tenant_uuid, from_date, until_date):
        return dao.get_average_survey_all_agent(tenant_uuid, from_date, until_date)

    def get_average_survey_by_queue_id(self, tenant_uuid, queue_id, from_date, until_date):
        return dao.get_average_survey_by_queue_id(tenant_uuid, queue_id, from_date, until_date)

    def get_average_survey_all_queue(self, tenant_uuid, from_date, until_date):
        return dao.get_average_survey_all_queue(tenant_uuid, from_date, until_date)

    def get_average_survey_agent_queue(self, tenant_uuid, queue_id, agent_id, from_date, until_date):
        return dao.get_average_survey_agent_queue(tenant_uuid, queue_id, agent_id, from_date, until_date)

    def get_average_survey_all_agents_in_queue(self, tenant_uuid, queue_id, from_date, until_date):
        return dao.get_average_survey_all_agents_in_queue(tenant_uuid, queue_id, from_date, until_date)


def build_survey_service():
    return SurveyService(dao, build_survey_validator(), build_survey_notifier())


class QueueFeatureService(CRUDService):

    def get_all_queue_features(self, tenant_uuid):
        return dao.get_all_queue_features(tenant_uuid)


def build_queuefeature_service():
    return QueueFeatureService(dao, build_queuefeature_validator(), build_queuefeature_notifier())
