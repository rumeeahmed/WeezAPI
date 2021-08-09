from flask import render_template
from flask.views import MethodView


class TeamStats(MethodView):
    """
    Object that serves the Total Team Stats page.
    """
    def get(self):
        return render_template('team_stats.html')


class TeamStatsPerGame(MethodView):
    """
    Object that serves the Team Stats Per Game page.
    """
    def get(self):
        return render_template('team_stats_per_game.html')
