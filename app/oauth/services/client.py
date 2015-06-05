from app import oauth
from ..models.client import Client

@oauth.clientgetter
def load_client(client_id):
    return Client.query.filter_by(client_id=client_id).first()
