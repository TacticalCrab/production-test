import requests as r

def get_random_data():
    result = r.get("https://random-data-api.com/api/v2/users?size=number")
    return result