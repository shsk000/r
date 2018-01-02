# -*- coding: utf-8 -*-
from functools import wraps
from flask import abort
from flask_restful import Resource, reqparse

import sys
import re

from oauth2client import client
from googleapiclient.errors import HttpError

from .build_youtube import build_youtube


def is_required_header_of_authorization(f):
    @wraps(f)
    def _is_required(self, *args, **kwargs):
        request_header = self.parser.parse_args()
        pattern = r"Bearer\s+(.*)"
        search_request_header = re.search(pattern, request_header.Authorization)

        """
        AccessTokenの不正常処理
        """
        # 空文字
        if search_request_header is None or not search_request_header[1]:
            abort(401)

        self.access_token = search_request_header[1]

        """
        正常処理
        """
        return f(self, *args, **kwargs)

    return _is_required


class UserPlaylists(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Authorization', type=str, location='headers', required=True)

    @is_required_header_of_authorization
    def get(self):
        build = build_youtube(self.access_token)

        try:
            lists = build.playlists().list(
                mine=True,
                part='snippet'
            ).execute()

            return lists
        except client.AccessTokenCredentialsError:
            abort(401)
        except:
            print("Unexpected error: ", sys.exc_info()[0])
            raise


class UserPlaylistItems(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Authorization', type=str, location='headers', required=True)

    @is_required_header_of_authorization
    def get(self, playlist_id):
        build = build_youtube(self.access_token)

        try:
            items = build.playlistItems().list(
                playlistId=playlist_id,
                part="snippet",
                maxResults=50
            ).execute()

            return items
        except client.AccessTokenCredentialsError:
            abort(401)
        except HttpError:
            abort(404)
        except:
            print("Unexpected error: ", sys.exc_info()[0])
            raise


if __name__ == '__main__':
    pass
