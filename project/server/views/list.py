import httplib2
from apiclient import discovery
from flask import Blueprint, url_for, session, redirect, render_template, g
from oauth2client import client

from ..resources.build_youtube import build_youtube

bp = Blueprint('list', __name__)


def oauth_required(func):
    def _is_required(*args, **kwargs):
        if 'credentials' not in session:
            return redirect(url_for('index'))

        func(*args, **kwargs)

    return _is_required


# @bp.before_request
# @oauth_required
# def before_request():
#     credentials = client.OAuth2Credentials.from_json(session['credentials'])
#
#     if credentials.access_token_expired:
#         return redirect(url_for('index'))
#
#     http_auth = credentials.authorize(httplib2.Http())
#     youtube = discovery.build('youtube', 'v3', http_auth)
#     g.api = Api(youtube)


@bp.route('/playlist')
def playlist():
    build_youtube()
    # playlists = g.api.get_user_playlists()
    return render_template('list.html')


# @bp.route('/playlist/<playlist_id>')
# def playlist_detail(playlist_id):
#     playlist_items = g.api.get_user_playlist_items(playlist_id)
#
#     return render_template('list2.html', listItems=playlist_items['items'])

