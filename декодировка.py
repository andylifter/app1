import json
from pprint import pprint

with open (r'fixtures\goods\prod.json', 'r', encoding='koi8_r') as f:
    s = json.load(f)


pprint(s)