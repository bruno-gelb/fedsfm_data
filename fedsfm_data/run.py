import requests

if __name__ == "__main__":
    url = 'http://fedsfm.ru/documents/terrorists-catalog-portal-act'
    response = requests.get(url)

    assert response.status_code == 200
    assert response.content

    raw = response.content.decode('utf-8')

    as_list = raw.split('<li>')

    assert 8000 < len(as_list) < 10000
