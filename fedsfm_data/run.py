import requests

if __name__ == "__main__":
    url = 'http://fedsfm.ru/documents/terrorists-catalog-portal-act'
    response = requests.get(url)
    
    assert response.status_code == 200
    assert response.content
