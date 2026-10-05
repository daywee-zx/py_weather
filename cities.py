def get_cities(filepath: str):
    with open(filepath, "r") as file:
        cities = [line.strip() for line in file]
    return cities
