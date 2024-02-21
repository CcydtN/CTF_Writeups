#!/usr/bin/env python3
from random import random
import requests
import time
import json
import sys
import re

def parse_data(form):
    items = []
    for i, entry in enumerate(form):
        if i % 2 == 0:
            continue
        # entry[0]
        item = {
            "question": entry[1],
            # "type": entry[3],
            "reqid": entry[4][0][0],
            "options": {x[0]: x[-1]or x[2] for x in entry[4][0][1]}
        }
        items.append(item)
    return items

def process(entry):
    freq = {}
    for key, value in entry["options"].items():
        if value not in freq:
            freq.update({value:[]})
        freq[value].append(key)

    filtered = filter(lambda x: len(x)==1, freq.values())
    mapped = map(lambda x: x[0], filtered)
    ret = list(mapped)
    return ret[0] if len(ret) != 0 else None

def analysis(file_path):
    with open(file_path, 'r') as file:
        raw_data = file.read()
        data = json.loads(raw_data)
    form_data = data[1][1]
    form = parse_data(form_data[1:-2]) # The only data we care is [1][1] and ignore the first and last two page
    data = [process(entry) for entry in form]
    data = [x for x in data if x is not None]
    print("".join(data))


if __name__ == '__main__':
    # url = 'https://docs.google.com/forms/d/e/1FAIpQLSc-A-Vmx_Te-bAqnu3TrRj-DAsYTgn52uSk92v3fECQb3T83A/viewform'
    analysis("data.json")
