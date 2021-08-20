from firebase_admin import credentials, firestore
from dotenv import load_dotenv, find_dotenv
import firebase_admin
import os


class WeezBase:
    """
    Object that handles the connection with the Firebase database.
    """

    def __init__(self):
        self._initialize_app()

    def _initialize_app(self) -> None:
        """
        Get the credentials, initialise the app and create a connection to the Firestore database.
        :return: None
        """
        if not firebase_admin._apps:
            load_dotenv(find_dotenv())
            firebase_credentials = {
                "type": os.environ.get('FIREBASE_TYPE'),
                "project_id": os.environ.get('FIREBASE_PROJECT_ID'),
                "private_key_id": os.environ.get('FIREBASE_PRIVATE_KEY_ID'),
                "private_key": os.environ.get('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
                "client_email": os.environ.get('FIREBASE_CLIENT_EMAIL'),
                "client_id": os.environ.get('FIREBASE_CLIENT_ID'),
                "auth_uri": os.environ.get('FIREBASE_AUTH_URI'),
                "token_uri": os.environ.get('FIREBASE_TOKEN_URI'),
                "auth_provider_x509_cert_url": os.environ.get('FIREBASE_AUTH_PROVIDER_URI'),
                "client_x509_cert_url": os.environ.get('FIREBASE_AUTH_URl'),
            }
            print(firebase_credentials)
            cred = credentials.Certificate(firebase_credentials)
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()
