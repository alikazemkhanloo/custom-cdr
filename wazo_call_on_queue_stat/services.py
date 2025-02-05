import pytz
from . import dao
from dateutil.relativedelta import relativedelta


def _generate_subinterval(from_, until, time_delta, timezone):
    from_ = from_.replace(tzinfo=None)
    until = until.replace(tzinfo=None)
    current = from_
    next_datetime = current + time_delta
    while current < until:
        current_in_tz = timezone.normalize(timezone.localize(current))
        next_in_tz = timezone.normalize(timezone.localize(next_datetime))
        yield current_in_tz, next_in_tz
        current = next_in_tz.replace(tzinfo=None)  # This is essential for DST change
        next_datetime = current + time_delta
        if next_datetime > until:
            next_datetime = until


def _generate_interval(interval, from_, until, timezone):
    time_deltas = {
        "hour": relativedelta(hours=1),
        "day": relativedelta(days=1),
        "month": relativedelta(months=1),
    }

    time_delta = time_deltas.get(interval, "hour")

    if time_delta == time_deltas["hour"]:
        if timezone.normalize(timezone.localize(from_ + relativedelta(months=1))) < timezone.normalize(timezone.localize(until)):
            raise Exception(details="Maximum of 1 month for interval by hour")
    if interval:
        yield from _generate_subinterval(from_, until, time_delta, timezone)
    else:
        yield from_, until


class StatCallOnQueueService:
    def __init__(self, _dao):
        self.dao: dao = _dao

    def get_stat_for_agent(
        self,
        agent_id,
        tenant_uuid,
        week_days=None,
        start_time=None,
        end_time=None,
        from_=None,
        until=None,
        timezone=None,
        interval=None,
    ):
        timezone = pytz.timezone(timezone)
        items=[]
        if interval and from_ and until:
            for start, end in _generate_interval(interval, from_= from_, until=until, timezone=timezone):
                print('start,and', start, end)
                result = self.dao.get_call_on_queue_stat_by_agent(
                    agent_id=agent_id,
                    tenant_uuid=tenant_uuid,
                    week_days=week_days,
                    start_time=start_time,
                    end_time=end_time,
                    from_=start,
                    until=end,
                    timezone=timezone,
                )
                output = {
                    'start': start.isoformat(),
                    'end': end.isoformat(),
                    'interval': interval,
                    'data': [row._asdict() for row in result]
                }
                items.append(output)
        return items

    def get_stat_for_queue(self, queue_id, tenant_uuid, **args):
        result = self.dao.get_call_on_queue_stat_by_queue(
            queue_id=queue_id, tenant_uuid=tenant_uuid, **args
        )
        output = [row._asdict() for row in result]
        return output
