from wazo_call_logd.plugins.cdr.schemas import CDRListRequestSchema as OriginalCDRListRequestSchema
from xivo.mallow import fields


class CDRListRequestSchema(OriginalCDRListRequestSchema):
  answered = fields.Boolean(load_default=None)
  