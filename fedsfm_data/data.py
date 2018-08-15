import requests


def strings_to_dicts(strings_list):
    dicts_list = []
    for entry in strings_list:
        number, data = entry.split('.', 1)

        try:
            fullname, birthday, place = data.split(',')
        except ValueError:
            pass  # todo handle cases when there's more than 2 commas

        entry_dict = {
            'number': int(number),
            'fullname': fullname.strip(),
            'birthday': birthday.strip(),
            'place': place.strip()
        }

        dicts_list.append(entry_dict)

    return dicts_list


def gather():
    url = 'http://fedsfm.ru/documents/terrorists-catalog-portal-act'
    response = requests.get(url)

    assert response.status_code == 200
    assert response.content

    raw = response.content.decode('utf-8')

    as_list = raw.split('Российские физические лица')[1].split('<li>')

    clean_list = [x.split('</li>')[0] for x in as_list if '. ' in x]

    assert 8000 < len(clean_list) < 10000

    dicts_list = strings_to_dicts(clean_list)

    assert len(dicts_list) == len(clean_list)
    assert isinstance(dicts_list[0], dict)

    return {'count': len(dicts_list),
            'entries': dicts_list}
