from app.tables import Zone

def rtn_zones():
    results = Zone.query.all()
    zones = [zone.to_json() for zone in results]
    return zones