import logging

from .survey.resource import SurveyListResource, SurveyAgentItemResource, SurveyQueueItemResource, \
    SurveyQueueAverageItemResource, SurveyAgentAverageItemResource, QueueFeaturesListResource, QueueFeaturesItemResource, \
    SurveyAllAgentAverageItemResource, SurveyAllQueueAverageItemResource, SurveyAgentInQueueAverageItemResource, SurveyAllAgentsInQueueAverageItemResource
from .survey.services import build_survey_service, build_queuefeature_service
from .db import init_db

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info('workano survey plugin start loading')
        init_db(
            'postgresql://asterisk:proformatique@localhost/asterisk?application_name=wazo-survey-plugin')
        api = dependencies['api']
        survey_service = build_survey_service()
        queuefeature_service = build_queuefeature_service()

        # survey
        api.add_resource(
            SurveyListResource,
            '/surveys',
            endpoint='surveys',
            resource_class_args=(survey_service,)
        )

        # survey by agent_id
        api.add_resource(
            SurveyAgentItemResource,
            '/surveys/agent/<agent_id>',
            resource_class_args=(survey_service,)
        )

        # survey by queueid
        api.add_resource(
            SurveyQueueItemResource,
            '/surveys/queue/<queue_id>',
            resource_class_args=(survey_service,)
        )

        # survey by queueid
        api.add_resource(
            SurveyQueueAverageItemResource,
            '/surveys/average/queue/<queue_id>',
            resource_class_args=(survey_service,)
        )

        # survey by agentid
        api.add_resource(
            SurveyAgentAverageItemResource,
            '/surveys/average/agent/<agent_id>',
            resource_class_args=(survey_service,)
        )

        # survey by agentid in specific queue_id
        api.add_resource(
            SurveyAgentInQueueAverageItemResource,
            '/surveys/average/queue/<queue_id>/agent/<agent_id>',
            resource_class_args=(survey_service,)
        )

        # survey all agents in specific queue_id
        api.add_resource(
            SurveyAllAgentsInQueueAverageItemResource,
            '/surveys/average/queue/<queue_id>/agents',
            resource_class_args=(survey_service,)
        )
        # survey by queueid
        api.add_resource(
            SurveyAllAgentAverageItemResource,
            '/surveys/average/allagent',
            resource_class_args=(survey_service,)
        )

        api.add_resource(
            SurveyAllQueueAverageItemResource,
            '/surveys/average/allqueue',
            resource_class_args=(survey_service,)
        )

        # queue-features
        api.add_resource(
            QueueFeaturesListResource,
            '/queue-features',
            endpoint='queuefeatures',
            resource_class_args=(queuefeature_service,)
        )

        # queue-features
        api.add_resource(
            QueueFeaturesItemResource,
            '/queue-features/<int:uuid>',
            resource_class_args=(queuefeature_service,)
        )

        logger.info('!!!!!!!!!!!!! workano survey plugin loaded!!!!')
