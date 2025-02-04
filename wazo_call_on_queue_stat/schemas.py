import pytz
from xivo.mallow_helpers import Schema
from xivo.mallow.validate import ContainsOnly, OneOf, Range, Regexp, Length
from marshmallow import (
    EXCLUDE,
    fields,
    Schema,
)


HOUR_REGEX = r"^([0,1][0-9]|2[0-3]):[0-5][0-9]$"

class StateCallOnQueueRequestSchema(Schema):
    from_ = fields.DateTime(data_key='from', load_default=None)
    until = fields.DateTime(load_default=None)
    timezone = fields.String(validate=OneOf(pytz.all_timezones), load_default='UTC')



class CallOnStatQueueResultSchema(Schema):
    agent_id = fields.Integer()
    queue_id = fields.Integer()
    agent_number = fields.Integer()
    talktime = fields.Integer()
    waittime = fields.Integer(),
    rinttime = fields.Integer(),
    status = fields.String()

# Copyright 2020-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later



# class QueueLogListRequestSchema(Schema):
#     class Meta:
#         unknown = EXCLUDE

#     limit = fields.Integer(validate=Range(min=0), load_default=1000)
#     callid = fields.String(validate=Length(min=1))
#     queuename = fields.String(validate=Length(min=1))
#     agent = fields.String(validate=Length(min=1))
#     event = fields.String(validate=Length(min=1))



# class QueueLogSchema(Schema):
#     class Meta:
#         ordered = True
#         unknown = EXCLUDE

#     id = fields.String()
#     time = fields.DateTime()
#     callid = fields.String()
#     queuename = fields.String()
#     agent = fields.String()
#     event = fields.String()
#     data1 = fields.String()
#     data2 = fields.String()
#     data3 = fields.String()
#     data4 = fields.String()
#     data5 = fields.String()