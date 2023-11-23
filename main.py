from weather_api import get_weather, get_weather_details, Weather

def main():
    # ask the user for their city
    user_city: str = input('Enter a city: ')

    # get the current weather details
    current_weather: dict = get_weather(user_city, mock=False)
    # print(current_weather)
    weather_details: list[Weather] = get_weather_details(current_weather)

    # get the current days:
    dfmt: str = '%d/%m/%y'
    days: list[str] = sorted({f'{date.date:{dfmt}}' for date in weather_details})

    for day in days:
        print(day)
        print('---')

        # group the weather data by date to make it easier to read
        grouped: list[Weather] = [current for current in weather_details if f'{current.date:{dfmt}}' == day]
        for element in grouped:
            print(element)

        print('') # an empty line


if __name__ == '__main__':
    main()