from serpapi import GoogleSearch
from pprint import pprint
import json
import os

params = {
  "engine": "google_scholar_author",
  "author_id": "Xp4tZ0cAAAAJ",
  "api_key": os.environ['API_KEY_SERPAPI']
}

search = GoogleSearch(params)
results = []

pages = search.pagination(page_size=57)

for page in pages:
    results.extend(page.get("articles", []))

results = sorted(results, key=lambda x: x['year'], reverse=True)

for paper in results:
    paper['google-scholar'] = paper.pop('link')

# dump results to a JSON file
with open('scholar.json', 'w') as f:
    json.dump(results, f, indent=4)