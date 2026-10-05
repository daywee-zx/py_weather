class WeatherData:
    def __init__(self, name: str, temp: int, country: str):
        self.name = name
        self.temp = temp
        self.country = country

    def __str__(self):
        return f"{self.name}, {self.country} {self.temp} °C"

    def get_name(self):
        return self.name

    def get_temp(self):
        return self.temp

    def get_country(self):
        return self.country


class CountryWeather:
    def __init__(self, name):
        self.name = name
        self.sum = 0
        self.cities = 0
        self.min = 0
        self.max = 0

    def __str__(self):
        return f"{self.name}\t- {self.cities} cities, avg: {self.get_avg()} °C, min: {self.min} °C, max: {self.max} °C"

    def add_city(self, wd: WeatherData):
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

