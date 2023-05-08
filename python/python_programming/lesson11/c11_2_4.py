"""GETでパラメーターを付加してアクセスするときのURL"""
import urllib.request

payload = {"key1": "value1", "key2": "value2"}
url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
print(url)