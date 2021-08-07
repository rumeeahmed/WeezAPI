from flask import render_template
from flask.views import MethodView
from models.weezbase import WeezBase
import random


class Players(MethodView):
    """
    View that serves the Players page.
    """
    def get(self):
        weezbase = WeezBase()
        player_data = weezbase.db.collection('players').get()
        players = [player.to_dict() for player in player_data]
        random.shuffle(players)
        return render_template('players.html', players=players)
