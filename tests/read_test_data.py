import json


def load_test_data():
    secrets_file = open('./project/server/instance/test_data.json', 'r')
    return json.load(secrets_file)


if __name__ == '__main__':
    print(read_test_data())
