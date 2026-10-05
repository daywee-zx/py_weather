import api
import weather
import cities
import asyncio

async def main():
    filename = "Cities.txt"
    timeout = 10

    city_list = cities.get_cities(filename)
    weather_data = await api.get_all(city_list, timeout=timeout)

    for data in weather_data:
        if isinstance(data, Exception):
            print(f"Error: {data}")
        else:
            print(data)

if __name__ == "__main__":
    asyncio.run(main())