__author__ = 'kneuharth'

from flask import Blueprint

site = Blueprint('site',
    __name__,
    template_folder='templates',
    static_folder='assets')