import os
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Fetch Weather Data
def fetch_weather(city):
    API_key = ('22bda62b632140ab9c8375051e81dc80')

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric'

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        raise Exception(data.get('message', 'API Error'))
    return data

# Comfort Index Calculation

def calculate_comfort(temp, humidity):
    comfort_index = temp - (0.55 * (1 - humidity / 100) * (temp - 14.5))
    return round(comfort_index, 2)

# Visualization Dashboard
def visualize(city, temp, humidity, pressure, wind, comfort):
    sns.set_style('whitegrid')

    parameters = ['Temperature', 'Humidity', 'Pressure', 'Wind Speed', 'Comfort Index']
    values = [temp, humidity, pressure, wind, comfort]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=parameters, y=values)
    plt.title(f'Weather Comfort Dashboard{city}')
    plt.ylabel('Values')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

# Main Execution
if __name__ == '__main__':
    city = input('Enter city name: ')
    data = fetch_weather(city)

    temp = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']

    comfort = calculate_comfort(temp, humidity)
    
    # Analytical Output
    print('\n--- Weather Analysis Report ---')
    print(f'City: {city}')
    print(f'Temperature: {temp} °C')
    print(f'Humidity: {humidity} %')
    print(f'Comfort Index: {comfort}')

    if comfort < 20:
        print('Weather Condition: Comfortable ')
    elif comfort <= 25:
        print('Weather Condition: Moderate ')
    else:
        print('Weather Condition: Uncomfortable ')

    visualize(city, temp, humidity, pressure, wind, comfort)
