import requests


def gather():
    url = 'http://fedsfm.ru/documents/terrorists-catalog-portal-act'
    response = requests.get(url)

    assert response.status_code == 200
    assert response.content

    raw = response.content.decode('utf-8')

    as_list = raw.split('Российские физические лица')[1].split('<li>')

    clean_list = [x for x in as_list if '. ' in x]

    assert 8000 < len(clean_list) < 10000

    return clean_list
