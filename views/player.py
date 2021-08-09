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
        print(self.data)
        return render_template('players.html', players=self.players)

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
