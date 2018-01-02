## Test Python Command
* 単体ファイルテスト
```bazaar
python -m unittest -v tests/???
```

* 複体ファイルテスト
```bazaar
python -m unittest discover -v
```

## Test Api Curl Command
* Authorization
```bazaar
curl -i -v -X GET http://0.0.0.0:5000/lists -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
curl -i -v -X GET http://0.0.0.0:5000/lists/items/<string:playlist_id> -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
