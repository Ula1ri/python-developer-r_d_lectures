import requests
import json


city_name = input("Enter city name: ")

response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1")
data = json.loads(response.content.decode("utf-8"))

if data and len(data) > 0:
    latitude = data['results'][0]['latitude']
    longitude = data['results'][0]['longitude']
    if latitude and longitude:
        print(f"{city_name}: {latitude}, {longitude}")

        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m")
        data2 = json.loads(response.content.decode("utf-8"))

        if data2 and len(data2) > 0:
            current_weather = data2['current_weather']
            temperature = current_weather['temperature']
            windspeed = current_weather['windspeed']
            winddirection = current_weather['winddirection']
            weathercode = current_weather['weathercode']
            print(f"Temperature: {temperature}")
            print(f"Wind speed: {windspeed}")
            print(f"Wind direction: {winddirection}")
            print(f"Weather code: {weathercode}")
        else:
            print("Failed to get weather for city")
    else:
        print("Failed to get coordinates for city")
else:
    print("City not found")