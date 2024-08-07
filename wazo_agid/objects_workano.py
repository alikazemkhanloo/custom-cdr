# -*- coding: utf-8 -*-
# Copyright 2007-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import logging
import re
from wazo_agid.schedule import ScheduleAction, SchedulePeriodBuilder, Schedule, \
    AlwaysOpenedSchedule

import datetime

from xivo_dao import user_dao

logger = logging.getLogger(__name__)


class DBUpdateException(Exception):
    pass


class QueueSurvey(object):
    def __init__(self, agi, cursor, tenant_uuid, agent_id, agent_number, queue_id, queue_name, queue_number,  queue_exten, caller_id, call_id, vote_number):
        self.agi = agi
        self.cursor = cursor
        self.tenant_uuid = tenant_uuid
        self.queue_id = queue_id
        self.queue_name = queue_name
        self.queue_number = queue_number
        self.agent_id = agent_id
        self.agent_number = agent_number
        self.call_id = call_id
        self.queue_exten = queue_exten
        self.caller_id = caller_id
        self.vote_number = vote_number
        ct = datetime.datetime.now()
        timestamp = ct.strftime("%Y-%m-%d %H:%M:%S")

        survey_log_columns = [
            'tenant_uuid', 'agent_id', 'agent_number', 'queue_id', 'queue_name', 'queue_number', 'queue_exten', 'caller_id', 'call_id', 'timestamp', 'rate'
        ]

        query = "INSERT INTO plugin_survey ({}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(
            ', '.join(survey_log_columns))
        arguments = (self.tenant_uuid, self.agent_id, self.agent_number, self.queue_id,
                     self.queue_name, self.queue_number, self.queue_exten, self.caller_id, self.call_id, timestamp, self.vote_number)

        self.cursor.execute(query, arguments)  # Corrected from `query` to `execute`

    def save_queue_survey_log_(self):
        pass


class QueueworkanoFeatures(object):
    def __init__(self, agi, cursor, tenant_uuid, queue_id):
        self.agi = agi
        self.cursor = cursor

        features_columns = [
            'id', 'tenant_uuid', 'queue_id', 'play_agentnumber_enable', 'queue_survey_enable'
        ]

        columns = ["plugin_queue_workano_features." + c for c in features_columns]

        query = "SELECT {} FROM plugin_queue_workano_features WHERE tenant_uuid = %s and queue_id = %s".format(
            ', '.join(columns))
        arguments = (tenant_uuid, queue_id)

        self.cursor.execute(query, arguments)  # Execute the query
        res = self.cursor.fetchone()  # Fetch one result

        if not res:
            raise LookupError(
                'Unable to find queue_workano_features {} with queue_id {}'.format(
                    tenant_uuid, queue_id)
            )

        # Debug print the result
        agi.verbose(f"Query Result: {res}")

        # Adjust these lines according to the actual result format
        self.play_agentnumber_enable = res['play_agentnumber_enable']
        self.queue_survey_enable = res['queue_survey_enable']
