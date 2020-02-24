from flask import (
    Blueprint
)
from flask import Flask, render_template

bp = Blueprint('render', __name__, url_prefix='/')


@bp.route('/user/<username>')
def index(username):
    return render_template('index.html', username=username)




@bp.route("/home")
def home():
    return render_template(
        'index1.html', my_string="Wheeeee!", 
        my_list=[0,1,2,3,4,5], title="Home")

@bp.route("/about")
def about():
    return render_template(
        'about.html', my_string="Wheeeee!", 
        my_list=[0,1,2,3,4,5], title="About")

@bp.route("/contact")
def contact():
    return render_template(
        'contact.html', my_string="Wheeeee!", 
        my_list=[0,1,2,3,4,5], title="Contact Us")