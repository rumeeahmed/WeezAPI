from flask import render_template
from flask.views import MethodView


class Home(MethodView):
    """
    View that serves the Homepage.
    """

    def get(self):
        return render_template('home.html')
