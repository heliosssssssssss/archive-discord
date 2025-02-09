import os
import json
from pprint import pprint

main =  r'auto-removed/-file=absolute'

with open(main, 'r', encoding='utf-8') as f:
    read = f.read()
    x = json.loads(read)

Quran = x['quran']

target_chapter = 2

for verses in Quran:
    if verses['chapter'] == target_chapter:
        pprint(verses)