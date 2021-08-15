from flask import render_template
from flask.views import MethodView
from models.weezbase import WeezBase


class TeamStats(MethodView):
    """
    Object that serves the Total Team Stats page.
    """
    def get(self) -> str:
        self._initialise_database()
        return render_template('team_stats.html', heading='TEAM STATS', labels=self.labels, data=self.data)

    def _initialise_database(self) -> None:
        """
        Initialise the database and retrieve the data to be processed passed into the Team_Stats template.
        :return: None
        """
        weezbase = WeezBase()
        self.labels = []
        self.data = {
            'Score': [],
            'Kills': [],
            'Deaths': [],
            'Assists': [],
            'K/D': [],
            'Damage': [],
            'Damage Taken': [],
            'Headshots': [],
            'Revives': [],
            'Teams Wiped': [],
        }

        documents = weezbase.db.collection('total_team_stats').stream()
        for document in documents:
            self.labels.append(document.id)
            self.data['Score'].append(document.get('team_score'))
            self.data['Kills'].append(document.get('team_kills'))
            self.data['Deaths'].append(document.get('team_deaths'))
            self.data['Assists'].append(document.get('team_assists'))
            self.data['K/D'].append(document.get('team_kd_average'))
            self.data['Damage'].append(document.get('team_damage'))
            self.data['Damage Taken'].append(document.get('team_damage_taken'))
            self.data['Headshots'].append(document.get('team_headshots'))
            self.data['Revives'].append(document.get('team_revives'))
            self.data['Teams Wiped'].append(document.get('team_teams_wiped'))


class TeamStatsPerGame(MethodView):
    """
    Object that serves the Team Stats Per Game page.
    """
    def get(self):
        self._initialise_database()
        return render_template('team_stats.html', heading='TEAM STATS PER GAME', labels=self.labels, data=self.data)

    def _initialise_database(self) -> None:
        """
        Initialise the database and retrieve the data to be processed passed into the Team_Stats template.
        :return: None
        """
        weezbase = WeezBase()
        self.labels = []
        self.data = {
            'Score Per Game': [],
            'Kills Per Game': [],
            'Deaths Per Game': [],
            'Assists Per Game': [],
            'K/D Per Game': [],
            'Damage Per Game': [],
            'Damage Taken Per Game': [],
            'Headshots Per Game': [],
            'Revives Per Game': [],
            'Teams Wiped Per Game': [],
        }

        documents = weezbase.db.collection('team_stats_per_game').stream()
        for document in documents:
            self.labels.append(document.id)
            self.data['Score Per Game'].append(document.get('team_score_per_game'))
            self.data['Kills Per Game'].append(document.get('team_kills_per_game'))
            self.data['Deaths Per Game'].append(document.get('team_deaths_per_game'))
            self.data['Assists Per Game'].append(document.get('team_assists_per_game'))
            self.data['K/D Per Game'].append(document.get('team_kd_average_per_game'))
            self.data['Damage Per Game'].append(document.get('team_damage_per_game'))
            self.data['Damage Taken Per Game'].append(document.get('team_damage_taken_per_game'))
            self.data['Headshots Per Game'].append(document.get('team_headshots_per_game'))
            self.data['Revives Per Game'].append(document.get('team_revives_per_game'))
            self.data['Teams Wiped Per Game'].append(document.get('teams_wiped_per_game'))
