# -*- coding: utf-8 -*-
# project/server/__init__.py
import os

from flask import Flask, request, url_for, render_template, session, redirect
from flask_restful import Api

from .resources.oauth import Oauth
from .resources.api_youtube import UserPlaylists, UserPlaylistItems
from .views import list

server_directory_path = os.path.dirname(os.path.abspath(__file__))
app = Flask(
    __name__,
    instance_relative_config=True,
    instance_path=os.path.join(server_directory_path, 'instance'),
    template_folder='../client/templates',
    static_folder='../client/r/dist',
    static_url_path='/static'
)

app.config.from_pyfile('config_develop.py')

"""
Flask Session Setting
"""
app.secret_key = app.config['SESSION_SECRET_KEY']

"""
Flask Register blueprint
"""
app.register_blueprint(list.bp)

"""
Flask Restful Setting
"""
api = Api(app)
api.add_resource(UserPlaylists, '/lists')
api.add_resource(UserPlaylistItems, '/lists/items/<string:playlist_id>')

"""
Flask Routing
"""


@app.route('/debug/session_clear')
def session_clear():
    session.clear()
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html', oauthUrl=Oauth().get_authorize_url())


@app.route('/oauth2callback')
def oauth2callback():
    o = Oauth(session)

    if 'code' not in request.args:
        return redirect(o.get_authorize_url())

    else:
        code = request.args.get('code')
        o.save_credentials(code)
        # TODO テストコードのため後で削除
        print(session['credentials'])
        return redirect(url_for('list.playlist'))
