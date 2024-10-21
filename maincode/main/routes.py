from flask import render_template, request, Blueprint, flash
from maincode import db
from maincode.models import Project
main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('homepage.html')


@main.route('/about')
def about():
    return render_template('about.html', title='About')

@main.route('/ivideopornodiachille')
def achille():
    return render_template('achille.html')

