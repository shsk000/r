# -*- coding: utf-8 -*-
import os
import json
from oauth2client.client import flow_from_clientsecrets

server_directory_path = os.path.dirname(os.path.abspath(__file__))
client_secrets_path = os.path.join(server_directory_path, '../', 'instance/client_secrets.json')


def _read_client_secrets():
    secrets_file = open(client_secrets_path, 'r')
    return json.load(secrets_file)['web']


def _generate_flow_from_clientsecrets():
    file = _read_client_secrets()

    return flow_from_clientsecrets(
        client_secrets_path,
        scope='https://www.googleapis.com/auth/youtube.readonly',
        redirect_uri=file['redirect_uris']
    )


class Oauth:
    server_directory_path = os.path.dirname(os.path.abspath(__file__))
    client_secrets_path = os.path.join(server_directory_path, 'instance/client_secrets.json')

    def __init__(self, save={}):
        self.flow = _generate_flow_from_clientsecrets()
        self.save = save
        return

    def get_authorize_url(self):
        return self.flow.step1_get_authorize_url()

    def get_credentials(self, code):
        return self.flow.step2_exchange(code)

    def save_credentials(self, code):
        credentials = self.get_credentials(code)
        self.save['credentials'] = credentials.to_json()

        return credentials


if __name__ == '__main__':
    pass
