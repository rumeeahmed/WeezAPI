from flask import render_template
from flask.views import MethodView
from models.weezbase import WeezBase


class Awards(MethodView):
    """
    Object that serves the Awards page.
    """
    def get(self) -> str:
        """
        Handle the get request made to this route. Return the details of all awards in the Firebase database.
        :return: a HTML template.
        """
        self._initialise_database()
        awards_length = len(self.data[0])
        awards_data = self._process_awards_data()

        awards_dict = {
            'bullet_bitch': [0, ''],
            'gummy_bear': [0, ''],
            'head_master': [0, ''],
            'lethal_killer': [0, ''],
            'least_lethal_killer': [0, ''],
            'medic': [0, ''],
            'pussio': [0, ''],
            'tank': [0, ''],
            'team_demolisher': [0, ''],
            'team_hater': [0, ''],
            'team_lover': [0, ''],
            'top_assister': [0, ''],
        }

        for key, value in awards_data.items():
            for key2, value2 in value.items():
                if awards_data[key][key2] > awards_dict[key2][0]:
                    awards_dict[key2][0] = value2
                    awards_dict[key2][1] = key



        return render_template('awards.html', awards_length=awards_length)

    def _initialise_database(self) -> None:
        """
        Initialise the database and retrieve the data to be passed into the Awards template.
        :return: None
        """
        weezbase = WeezBase()
        player_data = weezbase.db.collection('players').get()
        self.players = [player.to_dict() for player in player_data]

        self.data = []
        documents = weezbase.db.collection('awards').stream()
        for doc in documents:
            # Use the document ID to get the fields inside the document.
            awards = weezbase.db.collection('awards').document(doc.id).get().to_dict()
            self.data.append(awards)

    def _process_awards_data(self) -> dict:
        """
        Process the raw data retrieved from firebase and add the count of the awards together for the awards.
        :return: a dictionary containing a dictionary for each player and the count of the awards received.
        """
        data = {}
        for player in self.players:
            player_dict = {
                'bullet_bitch': 0,
                'gummy_bear': 0,
                'head_master': 0,
                'lethal_killer': 0,
                'least_lethal_killer': 0,
                'medic': 0,
                'pussio': 0,
                'tank': 0,
                'team_demolisher': 0,
                'team_hater': 0,
                'team_lover': 0,
                'top_assister': 0,
            }

            # Iterate over the award dicts in the list
            for award in self.data:
                # Iterate ove the keys in the dicts
                for key in award.keys():
                    # If the award key contains players name then add 1 to the value associated award key in player_dict
                    if award[key] == player['player']:
                        player_dict[key] += 1

            data[player['player']] = player_dict
        return data
