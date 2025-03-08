from wazo_call_logd.database.queries.call_log import CallLogDAO as OriginalCallLogDAO
from wazo_call_logd.database.models import CallLog
from sqlalchemy.orm import Query
from typing import Any
class CallLogDAO(OriginalCallLogDAO):
    def _apply_filters(self, query: Query, params: dict[str, Any]) -> Query:
        query = super()._apply_filters(query, params)
        if answered := params.get('answered'):
            if(answered == True):
                query = query.filter(CallLog.date_answer.is_not(None))
            elif (answered == False):
                query = query.filter(CallLog.date_answer.is_(None))


