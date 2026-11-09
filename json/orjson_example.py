import orjson
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    name: str
    signup_ts: datetime

user = User("Елена", datetime.now())

# orjson легко сериализует dataclass и datetime
json_bytes = orjson.dumps(user)
print(json_bytes)
# b'{"name":"\xd0\x95\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb0","signup_ts":"2025-10-26T08:22:00.123456+00:00"}'

# Десериализация
data = orjson.loads(json_bytes)
print(data)
# {'name': 'Елена', 'signup_ts': '2025-10-26T08:22:00.123456+00:00'}


my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}  
json_bytes = orjson.dumps(my_dict)  
print(json_bytes)  
