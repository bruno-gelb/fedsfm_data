def place_to_region(place):
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
