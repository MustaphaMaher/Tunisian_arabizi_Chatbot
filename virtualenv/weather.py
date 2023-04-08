import requests

# Define the weather API function
def get_weather(location="Tunis"):
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=92f54ec043c006fd6e476a85676c76ac"
    response = requests.get(url)
    data = response.json()
    #print(data)
    # Extraction des info comme temperature et humidité
    #description = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 1)  
    humidity = data['main']['humidity']
    #message
    message =f"🤖Fi {location} aana temperature :{temperature} °C wel humidité : {humidity}%."
    return message
