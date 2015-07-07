import json
from pkg_resources import resource_string

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


def load_json(x):
    contents = resource_string(__name__, "resources/" + x)
    return json.loads(contents.decode('utf-8'))


ahrqComorbidAll = load_json("ahrqComorbidAll.json")
elixComorbid = load_json("elixComorbid.json")
icd9Hierarchy = load_json("icd9Hierarchy.json")
ahrqComorbid = load_json("ahrqComorbid.json")
icd9Chapters = load_json("icd9Chapters.json")
quanElixComorbid = load_json("quanElixComorbid.json")

DIAGNOSIS = 'diagnosis'
PROCEDURE = 'procedure'


from .convert import (decimal_to_parts, decimal_to_short, short_to_decimal, short_to_parts, parts_to_short, parts_to_decimal)
from .counter import Counter


__all__= ['ahrqComorbidAll', 'elixComorbid', 'icd9Hierarchy', 'ahrqComorbid', 'icd9Chapters', 'quanElixComorbid',
          'decimal_to_parts', 'decimal_to_short', 'short_to_decimal', 'short_to_parts', 'parts_to_short', 'parts_to_decimal',
          'Counter', 'DIAGNOSIS', 'PROCEDURE']
