import logging

from flask import url_for, request, make_response
from flask_restful import Resource
from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ItemResource, ListResource

from .model import SurveyModel, QueueFeaturesModel
from .schema import SurveySchema, QueueFeaturesSchema
import json

logger = logging.getLogger(__name__)


class SurveyListResource(ListResource):
    schema = SurveySchema
    model = SurveyModel

    def build_headers(self, model):
        return {'Location': url_for('surveys', uuid=model.id, _external=True)}

    @required_acl('confd.surveys.read')
    def get(self):
        return super().get()


class SurveyAgentItemResource(ItemResource):
    def __init__(self, service):
        self.service = service
        self.schema = SurveySchema
        self.model = SurveyModel

    @required_acl('confd.surveys.read')
    def get(self, agent_id):
        tenant_uuid = request.headers.get('Wazo-Tenant')
        survey_list = self.service.get_all_survey_by_agent_id(
            tenant_uuid, agent_id)
        return {'total': survey_list.count(), 'items': self.schema().dump(survey_list, many=True)}


class SurveyQueueItemResource(ItemResource):
    def __init__(self, service):
        self.service = service
        self.schema = SurveySchema
        self.model = SurveyModel

    @required_acl('confd.surveys.read')
    def get(self, queue_id):
        tenant_uuid = request.headers.get('Wazo-Tenant')
        survey_list = self.service.get_all_survey_by_queue_id(
            tenant_uuid, queue_id)
        return {'total': survey_list.count(), 'items': self.schema().dump(survey_list, many=True)}


class SurveyQueueAverageItemResource(ItemResource):
    def __init__(self, service):
        self.service = service
        self.schema = SurveySchema
        self.model = SurveyModel

    @required_acl('confd.surveys.read')
    def get(self, queue_id):
        tenant_uuid = request.headers.get('Wazo-Tenant')
        from_date = request.args.get('from')
        until_date = request.args.get('until')
        survey_list = self.service.get_average_survey_by_queue_id(
            tenant_uuid, queue_id, from_date, until_date)

        result = []
        average = 0
        if survey_list.count() > 0:
            for survey in survey_list:
                average += int(survey.rate)
            result.append({"queue_id": queue_id,  "average_rate": round(
                average/survey_list.count(), 2)})

        return {'total': len(result), 'items': result}


class SurveyAgentAverageItemResource(ItemResource):
    def __init__(self, service):
        self.service = service
        self.schema = SurveySchema
        self.model = SurveyModel

    @required_acl('confd.surveys.read')
    def get(self, agent_id):
        tenant_uuid = request.headers.get('Wazo-Tenant')
        from_date = request.args.get('from')
        until_date = request.args.get('until')
        survey_list = self.service.get_average_survey_by_agent_id(
            tenant_uuid, agent_id, from_date, until_date)

        result = []
        average = 0
        if survey_list.count() > 0:
            for survey in survey_list:
                average += int(survey.rate)
            result.append({"agent_id": agent_id,  "average_rate": round(
                average/survey_list.count(), 2)})

        return {'total': len(result), 'items': result}


class SurveyAllAgentAverageItemResource(ItemResource):
    def __init__(self, service):
        self.service = service
        self.schema = SurveySchema
        self.model = SurveyModel

    @required_acl('confd.surveys.read')
    def get(self):
        tenant_uuid = request.headers.get('Wazo-Tenant')
        from_date = request.args.get('from')
        until_date = request.args.get('until')
        survey_list = self.service.get_average_survey_all_agent(
            tenant_uuid, from_date, until_date)

        rates = {}
        average = {}
        count = {}

        for survey in survey_list:
            if survey.agent_id not in rates:
                rates[survey.agent_id] = int(survey.rate)
                count[survey.agent_id] = 1
            else:
                rates[survey.agent_id] += int(survey.rate)
                count[survey.agent_id] += 1

        result = []
        for key, value in rates.items():
            average[key] = round(value / count[key], 2)
            result.append(
                {"agent_id": key,  "average_rate": round(value / count[key], 2)})

        return {'total': len(average), 'items': result}


class SurveyAllQueueAverageItemResource(ItemResource):
    def __init__(self, service):
        self.service = service
        self.schema = SurveySchema
        self.model = SurveyModel

    @required_acl('confd.surveys.read')
    def get(self):
        tenant_uuid = request.headers.get('Wazo-Tenant')
        from_date = request.args.get('from')
        until_date = request.args.get('until')
        survey_list = self.service.get_average_survey_all_queue(
            tenant_uuid, from_date, until_date)

        rates = {}
        average = {}
        count = {}

        for survey in survey_list:
            if survey.queue_id not in rates:
                rates[survey.queue_id] = int(survey.rate)
                count[survey.queue_id] = 1
            else:
                rates[survey.queue_id] += int(survey.rate)
                count[survey.queue_id] += 1

        result = []
        for key, value in rates.items():
            average[key] = round(value / count[key], 2)
            result.append(
                {"queue_id": key,  "average_rate": round(value / count[key], 2)})

        return {'total': len(average), 'items': result}


class SurveyAgentInQueueAverageItemResource(ItemResource):
    def __init__(self, service):
        self.service = service
        self.schema = SurveySchema
        self.model = SurveyModel

    @required_acl('confd.surveys.read')
    def get(self, queue_id, agent_id):
        tenant_uuid = request.headers.get('Wazo-Tenant')
        from_date = request.args.get('from')
        until_date = request.args.get('until')
        survey_list = self.service.get_average_survey_agent_queue(
            tenant_uuid, queue_id, agent_id, from_date, until_date)

        result = []
        average = 0
        if survey_list.count() > 0:
            for survey in survey_list:
                average += int(survey.rate)
            result.append({"queue_id": queue_id, "agent_id": agent_id,
                          "average_rate": average/survey_list.count()})

        return {'total': len(result), 'items': result}


class SurveyAllAgentsInQueueAverageItemResource(ItemResource):
    def __init__(self, service):
        self.service = service
        self.schema = SurveySchema
        self.model = SurveyModel

    @required_acl('confd.surveys.read')
    def get(self, queue_id):
        tenant_uuid = request.headers.get('Wazo-Tenant')
        from_date = request.args.get('from')
        until_date = request.args.get('until')
        survey_list = self.service.get_average_survey_all_agents_in_queue(
            tenant_uuid, queue_id, from_date, until_date)

        rates = {}
        average = {}
        count = {}

        for survey in survey_list:
            if survey.agent_id not in rates:
                rates[survey.agent_id] = int(survey.rate)
                count[survey.agent_id] = 1
            else:
                rates[survey.agent_id] += int(survey.rate)
                count[survey.agent_id] += 1

        result = []
        for key, value in rates.items():
            average[key] = round(value / count[key], 2)
            result.append(
                {"agent_id": key,  "average_rate": round(value / count[key], 2)})

        return {'total': len(average), 'items': result}


class QueueFeaturesListResource(ListResource):
    def __init__(self, service):
        self.service = service
        schema = QueueFeaturesSchema
        self.schema = QueueFeaturesSchema
        self.model = QueueFeaturesModel

    def build_headers(self, model):
        return {'Location': url_for('queuefeatures', uuid=self.model.id, _external=True)}

    @required_acl('confd.queuefeatures.read')
    def get(self):
        tenant_uuid = request.headers.get('Wazo-Tenant')
        featurs_list = self.service.get_all_queue_features(tenant_uuid)
        return {'total': featurs_list.count(), 'items': self.schema().dump(featurs_list, many=True)}

    @required_acl('confd.queuefeatures.create')
    def post(self):
        return super().post()

    @required_acl('confd.queuefeatures.update')
    def put(self, uuid):
        return super().put(uuid)


class QueueFeaturesItemResource(ItemResource):
    schema = QueueFeaturesSchema
    model = QueueFeaturesModel

    @required_acl('confd.queuefeatures.update')
    def put(self, uuid):
        return super().put(uuid)
