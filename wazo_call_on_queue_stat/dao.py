from xivo_dao.helpers.db_manager import daosession
from xivo_dao.alchemy.stat_call_on_queue import StatCallOnQueue
from xivo_dao.alchemy.stat_agent import StatAgent
from xivo_dao.alchemy.stat_queue import StatQueue
from sqlalchemy import func, text


# This only work because tables used have same column name
def _add_interval_query(
    table,
    query,
    tenant_uuids=None,
    week_days=None,
    start_time=None,
    end_time=None,
    from_=None,
    until=None,
    timezone=None,
    **ignored,
):
    if from_:
        query = query.filter(table.time >= from_)

    if until:
        query = query.filter(table.time < until)

    if timezone:
        timezone_name = str(timezone)
    else:
        timezone_name = "UTC"

    if start_time is not None and end_time is not None:
        hour = func.extract("HOUR", table.time.op("AT TIME ZONE")(timezone_name))
        query = query.filter(hour.between(start_time, end_time))

    if week_days is not None:
        day_of_week = func.extract(
            "ISODOW", table.time.op("AT TIME ZONE")(timezone_name)
        )
        query = query.filter(day_of_week.in_(week_days))
    elif not week_days and week_days is not None:
        query = query.filter(text("false"))

    return query


@daosession
def get_call_on_queue_stat_by_agent(
    session,
    agent_id,
    tenant_uuid,
    week_days=None,
    start_time=None,
    end_time=None,
    from_=None,
    until=None,
    timezone=None,
):
    print("agent_id, tenant_uuid >>>", agent_id, tenant_uuid)
    query = (
        session.query(
            func.min(StatAgent.agent_id).label("agent_id"),
            func.min(StatQueue.queue_id).label("queue_id"),
            func.min(StatAgent.number).label("agent_number"),
            func.sum(StatCallOnQueue.talktime).label("talktime"),
            func.sum(StatCallOnQueue.ringtime).label("ringtime"),
            func.sum(StatCallOnQueue.waittime).label("waittime"),
            func.avg(StatCallOnQueue.talktime).label("avg_talktime"),
            func.avg(StatCallOnQueue.ringtime).label("avg_ringtime"),
            func.avg(StatCallOnQueue.waittime).label("avg_waittime"),
            func.min(StatCallOnQueue.talktime).label("min_talktime"),
            func.min(StatCallOnQueue.ringtime).label("min_ringtime"),
            func.min(StatCallOnQueue.waittime).label("min_waittime"),
            func.max(StatCallOnQueue.talktime).label("max_talktime"),
            func.max(StatCallOnQueue.ringtime).label("max_ringtime"),
            func.max(StatCallOnQueue.waittime).label("max_waittime"),
            func.count(StatCallOnQueue.status).label("count"),
            func.min(StatCallOnQueue.status).label("status"),
        )
        .select_from(StatCallOnQueue)
        .filter(StatAgent.agent_id == agent_id)
        .filter(StatAgent.tenant_uuid == tenant_uuid)
        .join(StatAgent)
        .join(StatQueue)
        .group_by(StatCallOnQueue.stat_queue_id, StatCallOnQueue.status)
    )

    # query = _add_interval_query(
    #     StatCallOnQueue,
    #     query,
    #     None,
    #     week_days,
    #     start_time,
    #     end_time,
    #     from_,
    #     until,
    #     timezone,
    # )

    return query.all()


@daosession
def get_call_on_queue_stat_by_queue(
    session,
    queue_id,
    tenant_uuid,
    week_days=None,
    start_time=None,
    end_time=None,
    from_=None,
    until=None,
    timezone=None,
):
    query = (
        session.query(
            func.min(StatAgent.agent_id).label("agent_id"),
            func.min(StatQueue.queue_id).label("queue_id"),
            func.min(StatAgent.number).label("agent_number"),
            func.sum(StatCallOnQueue.talktime).label("talktime"),
            func.sum(StatCallOnQueue.ringtime).label("ringtime"),
            func.sum(StatCallOnQueue.waittime).label("waittime"),
            func.avg(StatCallOnQueue.talktime).label("avg_talktime"),
            func.avg(StatCallOnQueue.ringtime).label("avg_ringtime"),
            func.avg(StatCallOnQueue.waittime).label("avg_waittime"),
            func.min(StatCallOnQueue.talktime).label("min_talktime"),
            func.min(StatCallOnQueue.ringtime).label("min_ringtime"),
            func.min(StatCallOnQueue.waittime).label("min_waittime"),
            func.max(StatCallOnQueue.talktime).label("max_talktime"),
            func.max(StatCallOnQueue.ringtime).label("max_ringtime"),
            func.max(StatCallOnQueue.waittime).label("max_waittime"),
            func.count(StatCallOnQueue.status).label("count"),
            func.min(StatCallOnQueue.status).label("status"),
        )
        .select_from(StatCallOnQueue)
        .filter(StatAgent.agent_id == queue_id)
        .filter(StatAgent.tenant_uuid == tenant_uuid)
        .join(StatAgent)
        .join(StatQueue)
        .group_by(StatCallOnQueue.stat_agent_id, StatCallOnQueue.status)
    )

    query = _add_interval_query(
        StatCallOnQueue,
        query,
        None,
        week_days,
        start_time,
        end_time,
        from_,
        until,
        timezone,
    )

    return query.all()
