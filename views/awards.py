from flask import render_template
from flask.views import MethodView
from models.weezbase import WeezBase


class Awards(MethodView):
    """
    Object that serves the Awards page.
    """
    def get(self) -> str:
        """

        :return:
        """
        self._initialise_database()
        awards_length = len(self.data[0])
        awards_data = self._process_awards_data()
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
            for award in self.data:
                if award['bullet_bitch'] == player['player']:
                    player_dict['bullet_bitch'] += 1

                elif award['gummy_bear'] == player['player']:
                    player_dict['gummy_bear'] += 1

                elif award['head_master'] == player['player']:
                    player_dict['head_master'] += 1

                elif award['lethal_killer'] == player['player']:
                    player_dict['lethal_killer'] += 1

                elif award['least_lethal_killer'] == player['player']:
                    player_dict['lethal_killer'] += 1

                elif award['medic'] == player['player']:
                    player_dict['medic'] += 1

                elif award['pussio'] == player['player']:
                    player_dict['pussio'] += 1

                elif award['tank'] == player['player']:
                    player_dict['tank'] += 1

                elif award['team_demolisher'] == player['player']:
                    player_dict['team_demolisher'] += 1

                elif award['team_hater'] == player['player']:
                    player_dict['team_hater'] += 1

                elif award['team_lover'] == player['player']:
                    player_dict['team_lover'] += 1

                elif award['top_assister'] == player['player']:
                    player_dict['top_assister'] += 1

            data[player['player']] = player_dict
        return data
