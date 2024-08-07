from marshmallow import fields
from wazo_confd.helpers.mallow import BaseSchema


class QueueFeaturesSchema(BaseSchema):
    id = fields.Integer(dump_only=True)
    tenant_uuid = fields.String(dump_only=True)
    queue_id = fields.String(dump_only=False)
    play_agentnumber_enable = fields.String(dump_only=False)
    queue_survey_enable = fields.String(dump_only=False)

    
class SurveySchema(BaseSchema):
    id = fields.Integer(dump_only=True)
    tenant_uuid = fields.String(dump_only=True)
    agent_id = fields.String(dump_only=True)
    agent_number = fields.String(dump_only=True)
    queue_id = fields.String(dump_only=True)
    queue_name = fields.String(dump_only=True)
    queue_number = fields.String(dump_only=False)
    queue_exten = fields.String(dump_only=False)
    caller_id = fields.String(dump_only=False)
    call_id = fields.String(dump_only=False)
    timestamp = fields.String(dump_only=True)
    rate = fields.String(dump_only=True)


