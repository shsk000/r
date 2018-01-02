import httplib2
from apiclient import discovery
from oauth2client import client


def get_credentials(access_token=None):
    return client.AccessTokenCredentials(access_token, 'my-user-agent/1.0')


def build_youtube(access_token=None):
    """
    YouTube APIのラッパーインスタンスを生成し返す

    :param str access_token: アクセストークン
    :return: YouTube APIのラッパーインスタンス
    """

    # 引数の設定をしていない,str_credentialsが文字列でない場合Falseを返す
    if access_token is None or isinstance(access_token, str) is False:
        return False

    credentials = get_credentials(access_token)

    # 有効期限切れの場合もFalseを返す
    if credentials.access_token_expired:
        return False

    http_auth = credentials.authorize(httplib2.Http())
    youtube = discovery.build('youtube', 'v3', http_auth)

    return youtube


if __name__ == '__main__':
    pass
