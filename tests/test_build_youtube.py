import unittest
from project.server.resources.build_youtube import build_youtube
from .read_test_data import load_test_data

credentials_data = load_test_data()


class TestBuildYoutube(unittest.TestCase):
    def test_none_arguments(self):
        """
        引数の指定をしていない場合Falseを返す
        """
        build = build_youtube()
        self.assertFalse(build)

        """
        文字以外もFalseを返す
        """
        build = build_youtube(1234)
        self.assertFalse(build)

    def test_generate_youtube_api(self):
        build = build_youtube(credentials_data['access_token'])
        self.assertEqual(build.__class__.__name__, 'Resource')


if __name__ == '__main__':
    unittest.main()
