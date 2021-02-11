from app import *
from app.tables import *
from app.utils.articles import scan_article_to_db

import json

def load_zones_data_to_db():
    # 读取 json 文件
    with open('../../Node/data/zoneMsg.json', 'r') as f:
        data = json.load(f)

        for item in data["data"][::-1]:
            db.session.add(Zone(
                date=item["date"],
                msg=item["msg"],
                status=item["status"]
            ))
        
        db.session.commit()

db.drop_all()
db.create_all()
scan_article_to_db()
load_zones_data_to_db()


