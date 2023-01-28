import requests

url = 'https://akabab.github.io/superhero-api/api//all.json'

respones = requests.get(url)


def get_intelligence_super_hero(name):
    for list_ in respones.json():
        if list_.get('name') == name:
            i = list_['powerstats']
            j = i['intelligence']
            return j


dict_hero = {}

dict_hero['Hulk'] = (get_intelligence_super_hero('Hulk'))
dict_hero['Thanos'] = (get_intelligence_super_hero('Thanos'))
dict_hero['Captain America'] = (get_intelligence_super_hero('Captain America'))

print(f'Самый умный из супергероев:{max(dict_hero)}:{max(dict_hero.values())}')
