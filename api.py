import asyncio
import urllib.request
import weather
import json

def get(name, timeout):
    # had to swith to j2 due to server-side issues.
    url = f"https://wttr.in/{name}?format=j2"

    req = urllib.request.Request(url, headers={
        "User-Agent": "curl/8",
        "Accept": "application/json",
        "Connection": "close",
    })

    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = json.loads(r.read())

        return weather.WeatherData(
            name,
            int(data["current_condition"][0]["temp_C"]),
            data["nearest_area"][0]["country"][0]["value"]
        )

async def get_async(name, timeout):
    return await asyncio.to_thread(get, name, timeout)

async def get_all(cities, timeout=10):
    tasks = [
        get_async(c, timeout)
        for c in cities
    ]
    return await asyncio.gather(*tasks, return_exceptions=True)
