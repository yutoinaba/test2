"""JSONファイルの書き込み"""
import json

j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}

with open('test.json', 'w') as f:
    json.dump(j, f)