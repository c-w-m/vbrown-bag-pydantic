"""youtube tutorial flow"""
import json
from pprint import pprint
import pydantic

from models.people import Person, Address

# 1. Load some people from env/data.json

with open('environment/data.json') as fin:
    data = json.load(fin)

# pprint(data)

# 2. Make sure it validates the data

people = [Person(**p) for p in data]
for p in people:
    print(p)

# 3. People form code then back to JSON

people_as_json = [p.json() for p in people]
pprint(people_as_json)

# 4. How about app-level config files (pydantic.settings)

# see config.py file for examples

# 5. Error handling

people = []
bad_input = []
for p in data:
    try:
        people.append(Person(**p))
    except pydantic.ValidationError as err:
        print(err)
        bad_input.append(err, p)
