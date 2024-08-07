from xivo_dao.helpers.persistor import BasePersistor
from xivo_dao.resources.utils.search import CriteriaBuilderMixin
from .model import SurveyModel, QueueFeaturesModel
from datetime import datetime, timedelta
from sqlalchemy import cast
from sqlalchemy.types import DateTime

class SurveyPersistor(CriteriaBuilderMixin, BasePersistor):
    _search_table = SurveyModel

    def __init__(self, session, survey_search, tenant_uuids=None):
        self.session = session
        self.search_system = survey_search
        self.tenant_uuids = tenant_uuids

    def _find_query(self, criteria):
        query = self.session.query(SurveyModel)
        return self.build_criteria(query, criteria)

    def _search_query(self):
        return self.session.query(self.search_system.config.table)

    def get_all_surveys(self, tenant_uuid, queue_id):
        query = self.session.query(SurveyModel)
        query = query.filter(SurveyModel.tenant_uuid == tenant_uuid)
        query = query.filter(SurveyModel.queue_id == queue_id)
        return query

    def get_all_survey_by_queue_id(self, tenant_uuid, queue_id):
        query = self.session.query(SurveyModel)
        query = query.filter(SurveyModel.tenant_uuid == tenant_uuid)
        query = query.filter(SurveyModel.queue_id == queue_id)
        return query

    def get_all_survey_by_agent_id(self, tenant_uuid, agent_id):
        query = self.session.query(SurveyModel)
        query = query.filter(SurveyModel.tenant_uuid == tenant_uuid)
        query = query.filter(SurveyModel.agent_id == agent_id)
        return query

    def get_average_survey_by_queue_id(self, tenant_uuid, queue_id, from_date, until_date):
        from_date = datetime.fromisoformat(from_date) if isinstance(from_date, str) else from_date
        until_date = datetime.fromisoformat(until_date) if isinstance(until_date, str) else until_date
        until_date = until_date + timedelta(days=1)  # Include the entire day for until_date

        query = self.session.query(SurveyModel)
        query = query.filter(SurveyModel.tenant_uuid == tenant_uuid)
        query = query.filter(SurveyModel.queue_id == queue_id)
        query = query.filter(cast(SurveyModel.timestamp, DateTime) >= from_date)
        query = query.filter(cast(SurveyModel.timestamp, DateTime) < until_date)
        return query

    def get_average_survey_by_agent_id(self, tenant_uuid, agent_id, from_date, until_date):
        from_date = datetime.fromisoformat(from_date) if isinstance(from_date, str) else from_date
        until_date = datetime.fromisoformat(until_date) if isinstance(until_date, str) else until_date
        until_date = until_date + timedelta(days=1)  # Include the entire day for until_date

        query = self.session.query(SurveyModel)
        query = query.filter(SurveyModel.tenant_uuid == tenant_uuid)
        query = query.filter(SurveyModel.agent_id == agent_id)
        query = query.filter(cast(SurveyModel.timestamp, DateTime) >= from_date)
        query = query.filter(cast(SurveyModel.timestamp, DateTime) < until_date)
        return query

    def get_average_survey_all_agent(self, tenant_uuid, from_date, until_date):
        from_date = datetime.fromisoformat(from_date) if isinstance(from_date, str) else from_date
        until_date = datetime.fromisoformat(until_date) if isinstance(until_date, str) else until_date
        until_date = until_date + timedelta(days=1)  # Include the entire day for until_date

        query = self.session.query(SurveyModel)
        query = query.filter(SurveyModel.tenant_uuid == tenant_uuid)
        query = query.filter(cast(SurveyModel.timestamp, DateTime) >= from_date)
        query = query.filter(cast(SurveyModel.timestamp, DateTime) < until_date)
        return query

    def get_average_survey_all_queue(self, tenant_uuid, from_date, until_date):
        from_date = datetime.fromisoformat(from_date) if isinstance(from_date, str) else from_date
        until_date = datetime.fromisoformat(until_date) if isinstance(until_date, str) else until_date
        until_date = until_date + timedelta(days=1)  # Include the entire day for until_date

        query = self.session.query(SurveyModel)
        query = query.filter(SurveyModel.tenant_uuid == tenant_uuid)
        query = query.filter(cast(SurveyModel.timestamp, DateTime) >= from_date)
        query = query.filter(cast(SurveyModel.timestamp, DateTime) < until_date)
        return query

    def get_average_survey_agent_queue(self, tenant_uuid, queue_id, agent_id, from_date, until_date):
        from_date = datetime.fromisoformat(from_date) if isinstance(from_date, str) else from_date
        until_date = datetime.fromisoformat(until_date) if isinstance(until_date, str) else until_date
        until_date = until_date + timedelta(days=1)  # Include the entire day for until_date

        query = self.session.query(SurveyModel)
        query = query.filter(SurveyModel.tenant_uuid == tenant_uuid)
        query = query.filter(SurveyModel.agent_id == agent_id)
        query = query.filter(SurveyModel.queue_id == queue_id)
        query = query.filter(cast(SurveyModel.timestamp, DateTime) >= from_date)
        query = query.filter(cast(SurveyModel.timestamp, DateTime) < until_date)
        return query

    def get_average_survey_all_agents_in_queue(self, tenant_uuid, queue_id, from_date, until_date):
        from_date = datetime.fromisoformat(from_date) if isinstance(from_date, str) else from_date
        until_date = datetime.fromisoformat(until_date) if isinstance(until_date, str) else until_date
        until_date = until_date + timedelta(days=1)  # Include the entire day for until_date

        query = self.session.query(SurveyModel)
        query = query.filter(SurveyModel.tenant_uuid == tenant_uuid)
        query = query.filter(SurveyModel.queue_id == queue_id)
        query = query.filter(cast(SurveyModel.timestamp, DateTime) >= from_date)
        query = query.filter(cast(SurveyModel.timestamp, DateTime) < until_date)
        return query


class QueueFeatursPersistor(CriteriaBuilderMixin, BasePersistor):
    _search_table = QueueFeaturesModel

    def __init__(self, session, queuefeature_search, tenant_uuids=None):
        self.session = session
        self.search_system = queuefeature_search
        self.tenant_uuids = tenant_uuids

    def get_all_queue_features(self, tenant_uuid):
        query = self.session.query(QueueFeaturesModel)
        query = query.filter(QueueFeaturesModel.tenant_uuid == tenant_uuid)
        return query

    def _find_query(self, criteria):
        query = self.session.query(QueueFeaturesModel)
        return self.build_criteria(query, criteria)

    def _search_query(self):
        return self.session.query(self.search_system.config.table)
