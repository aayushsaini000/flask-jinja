from flask import (
    Blueprint
)
from flask import Flask, render_template

bp = Blueprint('render', __name__, url_prefix='/')


@bp.route('/user/<username>')
def index(username):
    return render_template('index.html', username=username)


@bp.route("/page1")
def template_test():
    return render_template('index1.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])


