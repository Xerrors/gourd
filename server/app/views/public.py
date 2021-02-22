from flask import Blueprint
from flask import request, jsonify, abort, json, session
from app import app, db
from app.utils.articles import get_article_list_from_dirs, get_articles_from_db, scan_article_to_db, rename_markdown
from app.utils.articles import get_articles_from_zhihu, get_articles_from_csdn, parse_markdown
from app.utils.validate import validate_server_token
from app.utils.database import rtn_zones, get_all_messages, get_all_zhuanlan, get_page_view_by_path, rtn_friends
from app.config import DOMAIN_PRE, TOKEN
from datetime import datetime

mod = Blueprint('public', __name__)

