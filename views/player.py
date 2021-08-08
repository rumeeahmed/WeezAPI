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
        return render_template('players.html', players=self.players)

    def _initialise_database(self):
        self.data = []
        weezbase = WeezBase()
        # Retrieve document ID's
        documents = weezbase.db.collection('games').stream()
        for doc in documents:
            # Use the document ID to get the collections inside the document.
            collections = weezbase.db.collection('games').document(doc.id).collections()
            # Get all the data from the collection add the player_name field and append it.
            for col in collections:
                stats = col.document('stats').get().to_dict()
                stats['player_name'] = col.id
                self.data.append(stats)

        player_data = weezbase.db.collection('players').get()
        self.players = [player.to_dict() for player in player_data]
        random.shuffle(self.players)
