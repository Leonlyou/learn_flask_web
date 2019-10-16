#!/usr/bin/python3
# @author：luomin
# @Time  ：2019/10/15 14:26
from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes