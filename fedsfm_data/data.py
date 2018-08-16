import math
from datetime import datetime

import requests


def clean_birthday(raw_birthday):
    birthday = raw_birthday. \
        strip(). \
        replace('г.р. ;', ''). \
        replace('г.р.', '')

    return birthday.strip()


def place_to_region(place):
    place = place.strip()

    if 'ЧИАССР' in place:
        region = 'Чечено-Ингушская ССР'
    elif 'АССР' in place and 'ЧИАССР' not in place:
        region = 'Азербайджанская ССР'
    elif 'ДАГЕСТАН' in place:
        region = 'Дагестан'
    elif 'Чечен' in place or 'чечен' in place or 'ЧЕЧЕН' in place:
        region = 'Чечня'
    elif 'ИНГУШЕТИЯ' in place:
        region = 'Ингушетия'
    elif 'КАБАРДИН' in place or ' КБР' in place:
        region = 'Кабардино-Балкария'
    elif 'СТАВРОПОЛЬ' in place:
        region = 'Ставропольский край'
    elif 'БАШКОРТОСТАН' in place:
        region = 'Башкортостан'
    elif 'ТАДЖИК' in place:
        region = 'Таджикистан'
    elif 'ТАТАРС' in place:
        region = 'Татарстан'
    elif 'КЫРГЫЗ' in place or 'КИРГИЗ' in place:
        region = 'Киргизия'
    elif 'КАЗАХ' in place:
        region = 'Казахстан'
    elif 'УЗБЕК' in place:
        region = 'Узбекистан'
    elif 'ЧЕЛЯБИН' in place:
        region = 'Челябинская область'
    elif 'АЛТАЙ' in place:
        region = 'Алтайский край'
    elif 'МОСКОВ' in place or 'МОСКВ' in place:
        region = 'Москва'
    else:
        region = 'undefined'

    return region


def strings_to_dicts(strings_list):
    dicts_list = []
    for entry in strings_list:
        old_fullname = ''
        place = ''
        number, data = entry.split('.', 1)

        if ', (' in data or ',  (' in data:
            splitted = data.split(',', 3)
            if len(splitted) == 4:
                fullname, old_fullname, birthday, place = splitted
            else:
                fullname, old_fullname, birthday = splitted
        else:
            splitted = data.split(',', 2)
            if len(splitted) == 3:
                fullname, birthday, place = splitted
            else:
                fullname, birthday = splitted

        fullname = fullname.strip()
        is_terrorist = False
        if '*' in fullname:
            fullname = fullname[:-1]
            is_terrorist = True

        birthday = clean_birthday(birthday)
        try:
            birthday_dt = datetime.strptime(birthday, '%d.%m.%Y')
        except ValueError:
            age = None
        else:
            # todo improve age calc, this is not 100% correct
            age = math.floor(
                (datetime.now() - birthday_dt).days / 365
            )

        if old_fullname:
            old_fullname = old_fullname.strip()[1:-1]

        if place:
            place = place.strip()[:-1]

        entry_dict = {
            'number': int(number),
            'fullname': fullname,
            'old_fullname': old_fullname if old_fullname else None,
            'is_terrorist': is_terrorist,
            'birthday': birthday,
            'age': age,
            'gender': None,  # todo
            'place': place if place else None,
            'region': place_to_region(place)
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

    assert len(clean_list) == len(dicts_list)
    assert isinstance(dicts_list[0], dict)

    return {'count': len(dicts_list),
            'entries': dicts_list}
