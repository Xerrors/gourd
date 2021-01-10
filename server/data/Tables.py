from app import db
import datetime

class Zone(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    date = db.Column(db.DateTime, default=datetime.now)
    msg = db.Column(db.Text)
    status = db.Column(db.String(20))

    def to_json(self):
        json_zone = {
            'id': self.id,
            'date': self.date,
            'msg': self.msg,
            'status': self.status
        }
        return json_zone