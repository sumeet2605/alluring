from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, stream_template
)
from werkzeug.exceptions import abort

from .auth import login_required
from .db import get_db

bp = Blueprint('clients', __name__)