from flask import render_template
from flask.views import MethodView
from datetime import datetime


class Home(MethodView):
    """
    View that serves the Homepage.
    """

    def get(self):
        return render_template('home.html')
