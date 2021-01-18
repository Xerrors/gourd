from app import *
from app.tables import *
from app.utils.articles import scan_article_to_db

db.drop_all()
db.create_all()
scan_article_to_db()
