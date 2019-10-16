#!/usr/bin/python3
# @author：luomin
# @Time  ：2019/10/15 14:32
from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes