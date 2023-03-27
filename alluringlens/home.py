from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, stream_template
)
from werkzeug.exceptions import abort

from .auth import login_required
from .db import get_db

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    return stream_template('index.html')


@bp.route('/contact')
def contact():
    return stream_template('contact.html')

@bp.route('/about')
def about():
    return stream_template('about.html')