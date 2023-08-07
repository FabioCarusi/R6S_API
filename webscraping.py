# scraping info of the operator
def info_operator(soup):

    info = {}

    name = soup.find_all('div', class_='operator__header__icons__names')
    side = soup.find_all('div', class_='operator__header__side__detail')
    squad = soup.find_all('div', class_='operator__header__squad__detail')
    specialties = soup.find_all('div', class_='operator__header__roles')

    info['Side'] = [s.find('span').get_text() for s in side][0]
    info['Name'] = [n.find('h1').get_text() for n in name][0]
    info['Squad'] = [q.find('span').get_text() for q in squad][0]
    info['Specialties'] = [p.get_text('', strip=True)
                           for p in specialties][0][16:] 

    element = soup.find_all(class_='operator__header__stat')
    for h in element:
        info[h.find('span').text] = len([e.get_text('', strip=True)
                                         for e in h.find_all(class_='is-active')])

    return info

# scraping info of loadout


def loadout(soup) -> dict:

    loadout_elements = soup.find_all(
        "div", class_='operator__loadout')
    loadout = {}

    for l in loadout_elements:
        for e, t in enumerate(l.find_all(class_='operator__loadout__category__title')):
            for i, value in enumerate(l.find_all(class_='operator__loadout__category__items')):
                if e == i:
                    loadout[t.get_text(' ', strip=True)] = value.get_text(
                        ', ', strip=True)

    return loadout

# scapring biography


def biography(soup) -> dict:

    bio_and_psy = {}
    bio = ''

    biography_elements = soup.find_all(
        "div", class_='operator__biography__description')

    for b in biography_elements:
        bio = b.get_text(' ', strip=True)

    bio = remove_unicode_characters(bio)
    bio_and_psy['Biography'] = bio

    return bio_and_psy


def biography_info(soup) -> dict:

    biography_info = soup.findAll(
        "div", class_="operator__biography__infos"
    )

    biography_elements = {}

    for b in biography_info:
        for e, title in enumerate(b.findAll(class_='operator__biography__info__title', text=True)):
            for i, value in enumerate(b.findAll(class_='operator__biography__info__value', text=True)):
                if e == i:
                    biography_elements[title.get_text('', strip=True)] = remove_unicode_characters(
                        value.get_text('', strip=True))

    return biography_elements

# create list of dictionaries


def export_json(soup):

    list_of_dicts = []

    list_of_dicts.append(info_operator(soup))
    list_of_dicts.append(loadout(soup))
    list_of_dicts.append(biography_info(soup))
    list_of_dicts.append(biography(soup))

    return list_of_dicts

# replace UNICODE characters -- ugly :-o


def remove_unicode_characters(text: str) -> str:
    return (text.replace(u"\u2018", "'")
                .replace(u"\u2019", "'")
                .replace(u"\u201c", '"')
                .replace(u"\u201d", '"')
                .replace(u"\u017c", 'z')
                .replace(u"\u0142", 'l')
                .replace(u"\u2026", '...')
                .replace(u"\u2013", '-')
                .replace(u"\u2014", '-')
                .replace(u"\u00e9", 'e')
                .replace(u"\u00e8", 'e')
                .replace(u"\u00ed", 'i')
                .replace(u"\u00e7", 'c')
                .replace(u"\u00f5", 'o')
                .replace(u"\u00e3", 'a')
                .replace(u"\u016b", 'u')
                .replace(u"\u014d", 'o')
                .replace(u"\u00c1", 'A')
                .replace(u"\u0107", 'c')
                .replace(u"\u00e1", 'a')
                .replace(u"\u0169", 'u')
                .replace(u"\u0129", 'i')
                .replace(u"\u00d8", 'o')
                .replace(u"\u00f8", 'o')
                .replace(u"\u00e6", 'e')
                .replace(u"\u00fc", 'u')
                .replace(u"\u00e4", 'e')
                .replace(u"\u00f6", 'u')
            )
