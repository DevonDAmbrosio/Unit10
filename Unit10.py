import requests
import pytest

url = 'https://api.duckduckgo.com/'

response = requests.get(url + '?q=presidents+of+the+united+states&format=json')

my_json = response.json()

# Made variable for readability
relatedTopics = my_json['RelatedTopics']

pres_list = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Buren", "Harrison", "Tyler",
             "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes", "Garfield",
             "Arthur", "Cleveland", "Harrison", "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding",
             "Coolidge", "Hoover", "Roosevelt", "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Carter",
             "Reagan", "Bush", "Clinton", "Bush", "Obama", "Trump", "Biden"]



