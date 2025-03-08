from wazo_call_logd.http import AuthResource
from flask import request
from .schemas import StateCallOnQueueRequestSchema
from .services import StatCallOnQueueService
from xivo.auth_verifier import required_acl
from wazo_call_logd.plugins.cdr.http import CDRAuthResource, format_cdr_result
from wazo_call_logd.plugins.cdr.schemas import CDRListRequestSchema, CDRSchemaList
from wazo_call_logd.auth import (
    extract_token_id_from_query_or_header,
)


class CDRResource(CDRAuthResource):
    @required_acl(
        'call-logd.cdr.read', extract_token_id=extract_token_id_from_query_or_header
    )
    def get(self):
        args = CDRListRequestSchema().load(request.args)
        print('args', args)
        args['tenant_uuids'] = self.query_or_header_visible_tenants(args['recurse'])
        cdrs = self.cdr_service.list(args)
        return format_cdr_result(CDRSchemaList().dump(cdrs))
