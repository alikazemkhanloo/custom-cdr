from __future__ import annotations

import re
from typing import TypedDict, cast

import wazo_call_logd.database.queries.call_log as call_log_dao
from datetime import datetime

from uuid import UUID
from wazo_call_logd.datatypes import CallDirection, OrderDirection

RECORDING_FILENAME_RE = re.compile(r'^.+-(\d+)-([a-z0-9-]{36})(.*)?$')

class SearchParams(TypedDict, total=False):
    search: str
    order: str
    direction: OrderDirection
    limit: int
    offset: int
    distinct: str
    start: datetime
    end: datetime
    call_direction: CallDirection
    cdr_ids: list[int]
    number: str
    tags: list[str]
    tenant_uuids: list[UUID]
    me_user_uuid: UUID
    user_uuids: list[UUID]
    recorded: bool
    conversation_id: str
    answered: bool


class ListParams(TypedDict, total=False):
    search: str
    order: str
    direction: OrderDirection
    limit: int
    offset: int
    distinct: str
    start: datetime
    end: datetime
    call_direction: CallDirection
    id: int
    start_id: int
    cdr_ids: list[int]
    number: str
    tags: list[str]
    tenant_uuids: list[str]
    me_user_uuid: str
    user_uuids: list[str]
    terminal_user_uuids: list[str]
    recorded: bool


class CDRService:
    def __init__(self, dao):
        self.dao = dao

    def list(self, search_params: SearchParams):
        searched = search_params.get('search')
        rec_search_params = {}
        dao_params = dict(search_params)
        if searched:
            matches = RECORDING_FILENAME_RE.search(searched)
            if matches:
                del dao_params['search']
                dao_params['id'] = matches.group(1)
                rec_search_params['uuid'] = matches.group(2)
        if user_uuids := search_params.get('user_uuids'):
            # api level 'user_uuids' is reinterpreted to avoid matching hidden participants
            del dao_params['user_uuids']
            dao_params['terminal_user_uuids'] = user_uuids

        count = self.dao.count_in_period(dao_params)

        call_logs = self.dao.find_all_in_period(
            cast(ListParams, dao_params)
        )
        rec_search_params['call_log_ids'] = [call_log.id for call_log in call_logs]
        return {
            'items': call_logs,
            'filtered': count['filtered'],
            'total': count['total'],
        }

    def get(self, cdr_id, tenant_uuids, user_uuids=None):
        return self.dao.get_by_id(cdr_id, tenant_uuids, user_uuids)
