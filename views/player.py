from flask import render_template
from flask.views import MethodView
from models.weezbase import WeezBase
import random


class Players(MethodView):
    """
    View that serves the Players page.
    """
    def __init__(self):
        self._initialise_database()

    def get(self) -> str:
        """
        Handle the get request made to this route. Return the details of all the players in the Firebase database.
        :return: a HTML template.
        """
        return render_template('players.html', players=self.players, display_stats=self.data)

    def _initialise_database(self) -> None:
        """
        Initialise the database and retrieve the data to be passed into the Player's template.
        :return: None
        """
        weezbase = WeezBase()
        player_data = weezbase.db.collection('players').get()

        self.players = []
        self.data = {}
        for player in player_data:
            # Create a list containing the player names.
            player = player.to_dict()
            self.players.append(player['player'])

            # Create a dictionary to hold the players games_played, kills, deaths and assists.
            self.data[player['player']] = [0, 0, 0, 0]

        random.shuffle(self.players)

        # Retrieve document ID's
        documents = weezbase.db.collection('games').stream()
        for doc in documents:
            # Use the document ID to get the collections inside the document.
            collections = weezbase.db.collection('games').document(doc.id).collections()

            # Get all the data from the collection add the player_name field and append it.
            for col in collections:
                for player in self.players:
                    if col.id == player:
                        stats = col.document('stats').get()
                        self.data[player][0] += stats.get('games_played')
                        self.data[player][1] += stats.get('kills')
                        self.data[player][2] += stats.get('deaths')
                        self.data[player][3] += stats.get('assists')


class Player(MethodView):
    """
    Object that serves a Player and their data.
    """
    def get(self, player_name: str) -> str:
        self._initialise_database(player_name)
        return render_template('player.html', player_name=player_name, labels=self.labels, data=self.data)

    def _initialise_database(self, player_name: str) -> None:
        """
        Initialise the database and retrieve the data to be passed into the Player's template.
        :return: None
        """
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

        weezbase = WeezBase()
        # Retrieve document ID's
        documents = weezbase.db.collection('games').stream()
        for doc in documents:
            # Use the document ID to get the collections inside the document.
            stats = weezbase.db.collection('games').document(doc.id).collection(player_name).document('stats').get()
            stats = stats.to_dict()

            if stats:
                # Create the labels for the graphs
                self.labels.append(doc.id)

                # Create the data lists for the graphs to display.
                self.data['Score'].append(stats['score'])
                self.data['Kills'].append(stats['kills'])
                self.data['Deaths'].append(stats['deaths'])
                self.data['Assists'].append(stats['assists'])
                self.data['K/D'].append(stats['kd'])
                self.data['Damage'].append(stats['damage'])
                self.data['Damage Taken'].append(stats['damage_taken'])
                self.data['Headshots'].append(stats['headshots'])
                self.data['Revives'].append(stats['revives'])
                self.data['Teams Wiped'].append(stats['teams_wiped'])
