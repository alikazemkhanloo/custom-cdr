from xivo_dao.helpers.db_manager import daosession
from .persistor import SurveyPersistor, QueueFeatursPersistor
from .search import survey_search, queuefeature_search

from datetime import timedelta


@daosession
def _persistor(session, tenant_uuids=None):
    return SurveyPersistor(session, survey_search, tenant_uuids)


@daosession
def _persistorFeatures(session, tenant_uuids=None):
    return QueueFeatursPersistor(session, queuefeature_search, tenant_uuids)


def create(queuefeatures):
    return _persistorFeatures().create(queuefeatures)


def put(queuefeatures):
    _persistorFeatures().put(queuefeatures)


def delete(queuefeatures):
    _persistorFeatures().delete(queuefeatures)


def get(queuefeatures_uuid, tenant_uuids=None):
    return _persistorFeatures(tenant_uuids).get_by({'id': queuefeatures_uuid})


def get_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).get_by(criteria)


def find(queuefeatures_uuid, tenant_uuids=None):
    return _persistorFeatures(tenant_uuids).find_by({'id': queuefeatures_uuid})


def find_by(tenant_uuids=None, **criteria):
    return _persistorFeatures(tenant_uuids).find_by(criteria)


def search(tenant_uuids=None, **parameters):
    return _persistor(tenant_uuids).search(parameters)


def find_all_by(tenant_uuids=None, **criteria):
    return _persistorFeatures(tenant_uuids).find_all_by(criteria)


def edit(queuefeatures):
    _persistorFeatures().edit(queuefeatures)


def delete(queuefeatures):
    _persistorFeatures().delete(queuefeatures)


def get_all_queue_features(tenant_uuid):
    return _persistorFeatures().get_all_queue_features(tenant_uuid)


def set_queue_features(tenant_uuid, queue_id, params):
    return _persistorFeatures().set_queue_features(tenant_uuid, queue_id, params)


def get_all_surveys(tenant_uuid, queue_id):
    return _persistor().get_all_surveys(tenant_uuid, queue_id)


def get_all_survey_by_queue_id(tenant_uuid, queue_id):
    return _persistor().get_all_survey_by_queue_id(tenant_uuid, queue_id)


def get_all_survey_by_agent_id(tenant_uuid, agent_id):
    return _persistor().get_all_survey_by_agent_id(tenant_uuid, agent_id)


def get_average_survey_by_queue_id(tenant_uuid, queue_id, from_date, until_date):
    return _persistor().get_average_survey_by_queue_id(tenant_uuid, queue_id, from_date, until_date)


def get_average_survey_by_agent_id(tenant_uuid, agent_id, from_date, until_date):
    return _persistor().get_average_survey_by_agent_id(tenant_uuid, agent_id, from_date, until_date)


def get_average_survey_all_agent(tenant_uuid, from_date, until_date):
    return _persistor().get_average_survey_all_agent(tenant_uuid, from_date, until_date)


def get_average_survey_all_queue(tenant_uuid, from_date, until_date):
    return _persistor().get_average_survey_all_queue(tenant_uuid, from_date, until_date)


def get_average_survey_agent_queue(tenant_uuid, queue_id, agent_id, from_date, until_date):
    return _persistor().get_average_survey_agent_queue(tenant_uuid, queue_id, agent_id, from_date, until_date)


def get_average_survey_all_agents_in_queue(tenant_uuid, queue_id, from_date, until_date):
    return _persistor().get_average_survey_all_agents_in_queue(tenant_uuid, queue_id, from_date, until_date)
