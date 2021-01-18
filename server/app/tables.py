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

    def update_count(self, read, comment):
        self.read_count = read
        self.comment_count = comment


class LocalArticlesTable(db.Model):
    __tablename__ = 'LocalArticlesTable'
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(50), unique=True)
    local_path = db.Column(db.String(50))
    read_count = db.Column(db.Integer, default=0)
    like_count = db.Column(db.Integer, default=0)

    def add_like(self):
        self.like_count += 1

    def add_read(self):
        self.read_count += 1


class LocalArticlesComment(db.Model):
    __tablename__ = 'LocalArticlesComment'
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(50), db.ForeignKey('LocalArticlesTable.path'))
    date = db.Column(db.String(30), default=datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    reviewer = db.Column(db.String(20))
    follow_id = db.Column(db.Integer, default=None) # 被评论的评论的 id
    content = db.Column(db.Text)


class Messages(db.Model):
    __tablename__ = 'Messages'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(30), default=datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    type = db.Column(db.String(20))
    link = db.Column(db.String(50))
    content = db.Column(db.Text)
    readed = db.Column(db.Boolean, default=False)

    def to_json(self):
        json_msgs = {
            'id': self.id,
            'date': self.date,
            'type': self.type,
            'link': self.link,
            'content': self.content,
            'readed': self.readed,
        }
        return json_msgs


# 暂时觉得没有启用的必要
class Visitors(db.Model):
    __tablename__ = "Visitors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    avatar = db.Column(db.String(50))  # 头像的链接，暂时不启用
    email = db.Column(db.String(20))
    site = db.Column(db.String(20))





