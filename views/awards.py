from flask import render_template
from flask.views import MethodView


class Awards(MethodView):
    """
    Object that serves the Awards page.
    """
    def get(self):
        return render_template('awards.html')
