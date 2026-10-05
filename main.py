import api
import weather
import cities
import asyncio

async def main():
    filename = "Cities.txt"
    timeout = 10

    city_list = cities.get_cities(filename)
    weather_data = await api.get_all(city_list, timeout=timeout)

    countries = {}

    for data in weather_data:
        if isinstance(data, Exception):
            print(f"Error: {data}")
        else:
            country = data.get_country()
            if country not in countries.keys():
                countries[country] = weather.CountryWeather(country)
            
            countries[country].add_city(data)
            print(data)

    for c in countries.values():
        print(c)
    
if __name__ == "__main__":
    asyncio.run(main())