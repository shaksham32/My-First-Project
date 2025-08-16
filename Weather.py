import requests

# Define the city and your OpenWeatherMap API key
city_name = 'delhi'
API_Key = 'a1e38680e8c7785a5333e7f233579e1f'  

# Construct the API request URL
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'

try:
    # Send a GET request to the OpenWeatherMap API
    response = requests.get(url)
    response.raise_for_status()  # Raises HTTPError for bad status codes

    # Parse the JSON response
    data = response.json()

    # Extract and print weather details
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']

    print(f"Weather in {city_name}: {weather_description.capitalize()}")
    print(f"Current Temperature: {temperature}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Humidity: {humidity}%")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    try:
        error_data = response.json()
        print(f"API Error Message: {error_data.get('message', 'No message')}")
    except:
        print("Unable to parse error message from response.")

except requests.exceptions.RequestException as err:
    print(f"Request failed: {err}")

except Exception as e:
    print(f"An error occurred: {e}")
import requests

# Define the city and your OpenWeatherMap API key
city_name = 'delhi'
API_Key = 'a1e38680e8c7785a5333e7f233579e1f'  # Replace with your real API a1e38680e8c7785a5333e7f233579e1fkey

# Construct the API request URL
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'

try:
    # Send a GET request to the OpenWeatherMap API
    response = requests.get(url)
    response.raise_for_status()  # Raises HTTPError for bad status codes

    # Parse the JSON response
    data = response.json()

    # Extract and print weather details
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']

    print(f"Weather in {city_name}: {weather_description.capitalize()}")
    print(f"Current Temperature: {temperature}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Humidity: {humidity}%")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    try:
        error_data = response.json()
        print(f"API Error Message: {error_data.get('message', 'No message')}")
    except:
        print("Unable to parse error message from response.")

except requests.exceptions.RequestException as err:
    print(f"Request failed: {err}")

except Exception as e:
    print(f"An error occurred: {e}")

