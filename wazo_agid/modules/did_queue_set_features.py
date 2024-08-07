# -*- coding: utf-8 -*-
# Copyright 2006-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from uuid import uuid4
from wazo_agid import agid, objects_workano

def did_queue_set_features(agi, cursor, args):
    queue_id = agi.get_variable('WAZO_DSTID')
    tenant_uuid = agi.get_variable('WAZO_TENANT_UUID')
    
    agi.set_variable('WAZO_PLAY_AGENTNUMBER_ENABLE', '0')
    agi.set_variable('WAZO_SURVEY_ENABLE', '0')

    try:
        queue_features = objects_workano.QueueworkanoFeatures(agi, cursor, tenant_uuid, queue_id)
        agi.set_variable('WAZO_PLAY_AGENTNUMBER_ENABLE', queue_features.play_agentnumber_enable)
        agi.set_variable('WAZO_SURVEY_ENABLE', queue_features.queue_survey_enable)
    except (ValueError, LookupError) as e:
        agi.verbose(f"Error: {str(e)}")
        agi.dp_break(str(e))

agid.register(did_queue_set_features)
