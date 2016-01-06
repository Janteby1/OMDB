import requests

spell = requests.get("http://spell-buddy.herokuapp.com/api/spells?name=magic%20missile").json()

print(spell)