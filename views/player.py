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
        :return:
        """
        return render_template('players.html', players=self.players, display_stats=self._process_player_stats())

    def _initialise_database(self) -> None:
        """
        Initialise the database and retrieve the data to be passed into the Player's template.
        :return: None
        """
        weezbase = WeezBase()
        player_data = weezbase.db.collection('players').get()
        self.players = [player.to_dict() for player in player_data]
        random.shuffle(self.players)

        self.data = []
        # Retrieve document ID's
        documents = weezbase.db.collection('games').stream()
        for doc in documents:
            # Use the document ID to get the collections inside the document.
            collections = weezbase.db.collection('games').document(doc.id).collections()

            # Get all the data from the collection add the player_name field and append it.
            for col in collections:
                # Get the stats in question from the database
                stats = col.document('stats').get()
                games_played = stats.get('games_played')
                kills = stats.get('kills')
                deaths = stats.get('deaths')
                assists = stats.get('assists')

                # Add each individual stat retrieved into a dict for the player.
                stats_dict = {
                    'player_name': col.id,
                    'games_played': games_played,
                    'kills': kills,
                    'deaths': deaths,
                    'assists': assists,
                }
                self.data.append(stats_dict)

    def _process_player_stats(self) -> dict:
        """
        Process the raw player data and the statistics together for each player.
        :return: A dict object containing dictionaries for each player and their total stats.
        """
        display_stats = {}
        # Iterate over each player and then create a dictionary of stats for the player.
        for player in self.players:
            player_dict = {
                'games_played': 0,
                'kills': 0,
                'deaths': 0,
                'assists': 0,
            }

            # Iterate over all the individual match stats and combine them per player and add them to the dictionary.
            for data in self.data:
                if data['player_name'] == player['player']:
                    player_dict['games_played'] += data['games_played']
                    player_dict['kills'] += data['kills']
                    player_dict['deaths'] += data['deaths']
                    player_dict['assists'] += data['assists']

            display_stats[player['player']] = player_dict
        return display_stats


class Player(MethodView):
    """
    Object that serves a Player and their data.
    """
    def get(self, player_name: str) -> str:
        pass
