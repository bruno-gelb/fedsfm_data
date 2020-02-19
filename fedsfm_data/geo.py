import requests


def place_to_region(place):
    if len(place) > 1 and len(place.split(' ')) > 1:
        city = place.split(' ')[1]
    else:
        city = ''

    payload = {'query': city, 'withParent': '1', 'contentType': 'city', 'limit': '1'}

    r = requests.get('http://kladr-api.ru/api.php', params=payload)
    query_results = r.json()
    if len(query_results["result"]) > 0:
        try:
            parents = query_results["result"][0]["parents"]
            if len(parents) > 0:
                parent = parents[0]
                region = f'{parent["name"]} {parent["type"]}'
            else:
                region = "undefined"
        except KeyError:
            region = "undefined"
    else:
        region = "undefined"
    return region
