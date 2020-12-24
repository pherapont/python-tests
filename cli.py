import requests
import click

print("in workflow")

SAMPLE_API_KEY = '3047bc13be32b1e2d8fa24e6be864e6a'

def current_weather(location, api_key=SAMPLE_API_KEY):
    print("in current_weather:")
    url = 'http://api.openweathermap.org/data/2.5/weather'

    query_params = {
        'q': location,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)

    return response.json()['weather'][0]['description']

@click.command()
@click.argument('location')
def main(location):
    print("im main")
    weather = current_weather(location)
    print(f"The weather in {location} right now {weather}")