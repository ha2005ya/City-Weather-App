import requests

def display_weather(data_dic):
    for key, value in data_dic.items():
        print(f'{key.title()} : {value}')

def weather_data(city):
    my_key = '2e5256639905e8614ccd1c761d197435'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={my_key}'
    response = requests.get(url)
    data = response.json()
    if data['cod'] != 200:
        return 'City is not Found'
    else:
        print(f'## Weather in {data["name"]} ##')
        return display_weather(data['main'])


def display_weather(data_dic):
    for key, value in data_dic.items():
        print(f'{key.title()} : {value}')