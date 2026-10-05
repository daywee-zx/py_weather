import api
import weather
import cities
import asyncio

class CountryWeather:
    def __init__(self, name):
        self.name = name
        self.sum = 0
        self.cities = 0
        self.min = 0
        self.max = 0

    def __str__(self):
        return f"{self.name}\t- {self.cities} cities, avg: {self.get_avg()} °C, min: {self.min} °C, max: {self.max} °C"

    def add_city(self, wd: weather.WeatherData):
        temp = wd.get_temp()

        self.min = temp if temp < self.min else self.min
        self.max = temp if temp > self.max else self.max

        self.sum += temp
        self.cities = self.cities + 1

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max

    def get_avg(self):
        return self.sum / self.cities

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
                countries[country] = CountryWeather(country)
            
            countries[country].add_city(data)
            print(data)

    for c in countries.values():
        print(c)
    
if __name__ == "__main__":
    asyncio.run(main())