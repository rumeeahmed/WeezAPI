from flask import render_template
from flask.views import MethodView


class Players(MethodView):
    """
    View that serves the Players.
    """
    def get(self):
        return render_template('home.html')
