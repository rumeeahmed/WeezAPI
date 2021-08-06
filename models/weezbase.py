from firebase_admin import credentials, firestore
import firebase_admin


class WeezBase:

    def __init__(self):
        self._initialize_app()

    def _initialize_app(self) -> None:
        """
        Get the credentials, initialise the app and create a connection to the Firestore database.
        :return: None
        """
        if not firebase_admin._apps:
            cred = credentials.Certificate('/Users/rumeeahmed/Documents/Weez/DataTools/service_key.json')
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()