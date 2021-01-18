from app.tables import Zone, Messages

def rtn_zones():
    query_result = Zone.query.all()
    zones = [zone.to_json() for zone in query_result]
    return zones


def get_all_messages():
    query_result = Messages.query.all()
    msgs = [msg.to_json() for msg in query_result]
    return msgs