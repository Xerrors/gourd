from app import db
from datetime import datetime

class Zone(db.Model):
    __tablename__ = 'ZoneTable'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    date = db.Column(db.String(20), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
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
    create_date = db.Column(db.String(30))


class CsdnCount(db.Model):
    __tablename__ = 'CsdnReadCount'
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.String(20), db.ForeignKey('CsdnArticlesTable.article_id'))
    date = db.Column(db.String(30), default=datetime.today().strftime('%Y-%m-%d'))
    read_count = db.Column(db.Integer)
    comment_count = db.Column(db.Integer)

    def update_count(read, comment):
        self.read_count = read
        self.comment_count = comment


