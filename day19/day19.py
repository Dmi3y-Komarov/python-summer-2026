import json

with open("weather.json", "r", encoding="utf-8") as f:
    data = json.loads(f)
print(f'Сегодня в {data["city"]} {data["temp"]} градуса, но ощущается как {data["feels_like"]}')

