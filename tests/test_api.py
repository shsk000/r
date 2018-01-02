import unittest
import httplib2

from .read_test_data import load_test_data
from project.server.instance.config_develop import HOST

credentials_data = load_test_data()
access_token = credentials_data['access_token']
h = httplib2.Http()


class TestUserPlaylistsApi(unittest.TestCase):
    def testRequireHeaders(self):
        """
        RequestHeaderにAuthorizationがない場合400を返す
        """
        resp, content = h.request(
            'http://' + HOST + ':5000/lists',
            'GET'
        )
        self.assertEqual(resp.status, 400)

    def testAuthorizationAccessToken(self):
        """
        Authorization Access Tokenから正常認可されなかった場合401を返す
        """
        resp, content = h.request(
            'http://' + HOST + ':5000/lists',
            'GET',
            headers={
                'Authorization': 'Bearer aaaaa'
            }
        )
        self.assertEqual(resp.status, 401)

    def testGetPlaylists(self):
        """
        正常にplaylistsが取得できる
        """
        resp, content = h.request(
            'http://' + HOST + ':5000/lists',
            'GET',
            headers={
                'Authorization': 'Bearer ' + access_token
            }
        )

        self.assertEqual(resp.status, 200)


class TestUserPlaylistItemsApi(unittest.TestCase):
    def testRequireHeaders(self):
        """
        RequestHeaderにAuthorizationがない場合400を返す
        """
        resp, content = h.request(
            'http://' + HOST + ':5000/lists/items/test',
            'GET'
        )
        self.assertEqual(resp.status, 400)

    def testAuthorizationAccessToken(self):
        """
        Authorization Access Tokenから正常認可されなかった場合401を返す
        """
        resp, content = h.request(
            'http://' + HOST + ':5000/lists/items/test',
            'GET',
            headers={
                'Authorization': 'Bearer aaaaa'
            }
        )
        self.assertEqual(resp.status, 401)

    def testCannotGetPlaylistItems(self):
        """
        存在しないplaylistItemsをリクエストした際404を返す
        """
        resp, content = h.request(
            'http://' + HOST + ':5000/lists/items/aaaa',
            'GET',
            headers={
                'Authorization': 'Bearer ' + access_token
            }
        )
        self.assertEqual(resp.status, 404)

    def testGetPlaylistItems(self):
        """
        存在するplaylistItemsをリクエストした際200を返す
        """
        resp, content = h.request(
            'http://' + HOST + ':5000/lists/items/PLhv4QKCpeSWbZ9oj5GIZIX-t4yjYH_b7s',
            'GET',
            headers={
                'Authorization': 'Bearer ' + access_token
            }
        )
        self.assertEqual(resp.status, 200)


if __name__ == '__main__':
    unittest.main()
