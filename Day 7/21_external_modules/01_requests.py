import requests

r = requests.get('https://api.github.com/events')

with open("Aditya.txt", "w", encoding="utf-8") as f:
    f.write(r.text)