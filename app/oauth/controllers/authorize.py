from .. import oauth_blueprint
from ..models.client import Client
from app import oauth
from flask import render_template, request
from flask_login import login_required

@oauth_blueprint.route('/oauth/authorize', methods=['GET', 'POST'])
@login_required
@oauth.authorize_handler
def authorize(*args, **kwargs):
    if request.method == 'GET':
        client_id = kwargs.get('client_id')
        client = Client.query.filter_by(client_id=client_id).first()
        kwargs['client'] = client
        return render_template('oauthorize.html', **kwargs)

    confirm = request.form.get('confirm', 'no')
    return confirm == 'yes'

@oauth_blueprint.route('/token', methods=['POST'])
@oauth.token_handler
def access_token():
    return None

@oauth_blueprint.route('/oauth/revoke', methods=['POST'])
@oauth.revoke_handler
def revoke_token():
    pass