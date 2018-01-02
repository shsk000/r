import unittest
from project.server.resources.oauth import Oauth, _generate_flow_from_clientsecrets, _read_client_secrets

oauth = Oauth()


class TestOauthPrivateDef(unittest.TestCase):

    def test_read_client_secrets(self):
        file = _read_client_secrets()
        has_client_id = file.get('client_id', None)

        self.assertTrue(has_client_id)

    def test_generate_flow_from_clientsecrets(self):
        flow = _generate_flow_from_clientsecrets()
        class_name = flow.__class__.__name__
        self.assertTrue(class_name is 'OAuth2WebServerFlow')


if __name__ == '__main__':
    unittest.main()
