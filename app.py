from flask import Flask
from views.team_stats import TeamStats, TeamStatsPerGame
from views.player import Players, Player
from views.awards import Awards
from views.home import Home
from datetime import datetime

app = Flask(__name__)

app.add_url_rule('/', view_func=Home.as_view('home'))
app.add_url_rule('/players', view_func=Players.as_view('players'))
app.add_url_rule('/players/<player_name>', view_func=Player.as_view('player'))
app.add_url_rule('/awards', view_func=Awards.as_view('awards'))
app.add_url_rule('/team_stats', view_func=TeamStats.as_view('team_stats'))
app.add_url_rule('/team_stats_per_game', view_func=TeamStatsPerGame.as_view('team_stats_per_game'))


@app.context_processor
def inject_year() -> dict:
    """
    Generate the current year and send it across to all of the templates.
    :return: a dictionary object that contains the year.
    """
    year = datetime.now().strftime('%Y')
    return dict(year=year)


if __name__ == '__main__':
    app.run(debug=True)
