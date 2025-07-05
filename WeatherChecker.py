import requests
import os
from bs4 import BeautifulSoup 

def getdata():
    API_KEY = "3866ffdd8b588876d9265b7d9a8e450f"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={17.3850}&lon={78.4867}&appid={API_KEY}&units=metric"
    responce = requests.get(url)
    return responce.json()

def notification(title,message):
    os.system(f'''osascript -e 'display notification "{message}" with title "{title}"' ''')

data = getdata()

if data and data.get("main"):
    temp = data['main']['temp']
    condition = data['weather'][0]['description'].capitalize()
    city = data['name']
    notification(f"🌤️Weather in {city}",f"{temp}°C\n{condition}")
else:
    notification("Weather Info","Failed to fetch Data")


        

