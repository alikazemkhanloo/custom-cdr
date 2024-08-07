# -*- coding: utf-8 -*-
# Copyright 2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import re
import logging

from wazo_agid import objects_workano
from wazo_agid.handlers import handler

logger = logging.getLogger(__name__)

AGENT_CHANNEL_RE = re.compile(r'^Local/id-(\d+)@agentcallback-[a-f0-9]+;1$')

class SurveyLogHandler(handler.Handler):
    def execute(self):
        vote_number = self._agi.get_variable('WAZO_VOTE_NUMBER')
        self._agi.verbose('AGI: vote_number {}'.format(vote_number))

        if vote_number:
            tenant_uuid = self._agi.get_variable('WAZO_TENANT_UUID') or 'default_tenant_uuid'
            agent_id = self._agi.get_variable('MEMBERNAME')
            queue_exten = self._agi.get_variable('XIVO_REAL_NUMBER') or 'default_queue_exten'
            caller_id = self._agi.get_variable('WAZO_SRCNUM') or 'default_caller_id'
            agent_number = 'unknown_agent_number'

            if agent_id:
                agent_id = agent_id.split('/')[1]
                agent_number = agent_id

            queue_id = self._agi.get_variable('WAZO_DSTID') or 'default_queue_id'
            queue_name = self._agi.get_variable('WAZO_QUEUENAME') or 'default_queue_name'
            queue_number = self._agi.get_variable('WAZO_ENTRY_EXTEN') or 'default_queue_number'
            call_id = self._agi.get_variable('WAZO_SIP_CALL_ID') or 'default_call_id'

            objects_workano.QueueSurvey(self._agi, self._cursor, tenant_uuid, agent_id,
                                        agent_number, queue_id, queue_name, queue_number, queue_exten, caller_id,
                                        call_id, vote_number)
            logger.debug('handler saved ')
