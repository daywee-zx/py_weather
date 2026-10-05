class WeatherData:
    def __init__(self, name: str, temp: int, country: str):
        self.name = name
        self.temp = temp
        self.country = country

    def __str__(self):
        return f"{self.name}, {self.country} {self.temp} °C"