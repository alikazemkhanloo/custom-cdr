# -*- coding: utf-8 -*-
# Copyright 2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import logging

from wazo_agid import agid
from wazo_agid.handlers import queue_survey

logger = logging.getLogger(__name__)


def queue_survey_log(agi, cursor, args):
    handler = queue_survey.SurveyLogHandler(agi, cursor, args)
    handler.execute()


agid.register(queue_survey_log)
