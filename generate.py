import json
from jinja2 import Environment, FileSystemLoader

# Load JSONs
with open("data/hero.json", encoding="utf-8") as f:
    hero = json.load(f)

with open("data/contact.json", encoding="utf-8") as f:
    contact = json.load(f)

with open("data/papers.json", encoding="utf-8") as f:
    papers = json.load(f)

years = sorted(set(p["year"] for p in papers), reverse=True)

# Jinja2
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("index.html")

# Render
html = template.render(hero=hero, contact=contact, papers=papers, years=years)

# Write
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Página gerada com sucesso em 'index.html'")
