from app import db
from datetime import datetime

class Zone(db.Model):
    __tablename__ = 'ZoneTable'
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


class CsdnArticlesTable(db.Model):
    __tablename__ = 'CsdnArticlesTable'
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.String(20))
    title = db.Column(db.String(60))
    date = db.Column(db.String(30))
    read_count = db.Column(db.Integer)
    comment_cpint = db.Column(db.String)


class CsdnCount(db.Model):
    __tablename__ = 'CsdnReadCount'
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.String(20), db.ForeignKey('CsdnArticlesTable.article_id'))

