#!/usr/bin/python3
# @author：luomin
# @Time  ：2019/10/15 14:31
from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers