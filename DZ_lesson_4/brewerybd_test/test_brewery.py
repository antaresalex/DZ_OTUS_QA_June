import json
import requests
import pytest


# Тестируем получение List Breweries с использованием тегов by_city (используя параметризацию по городам), выдаем json
# Проверяем совпадение в полученном json значения по ключу город с городом из запроса в url
# При запросе несуществующего города получаем пустой list, а не ошибку.
def test_city(url_city):
    url = f'https://api.openbrewerydb.org/breweries?by_city={url_city}'
    response = requests.get(url=url)
    json_response = response.json()
    if len(json_response) != 0:
        for bar in json_response:
            assert bar.get('city') == url_city
    else:
        print("This response return empty json")


# Тестируем получение json by_type, с параметризацией из списка элементов (micro, regional, brewpub, large, planning,
# bar, contract, proprietor). Проверяем наличие в json в словарях ключа brewery_type со значением из url-запроса.
def test_type(fixture_by_type):
    url = f'https://api.openbrewerydb.org/breweries?by_type={fixture_by_type}'
    response = requests.get(url=url)
    json_response = response.json()
    for brewery_type in json_response:
        assert fixture_by_type == brewery_type.get('brewery_type')


def test_type_and_city(fixture_by_type, url_city):
    url = f'https://api.openbrewerydb.org/breweries?by_type={fixture_by_type}&by_city={url_city}'
    response = requests.get(url=url)
    json_response = response.json()
    assert type(json_response) == list


# Тестируем получение запроса через Autocomplete (получаем ID и название)
def test_autocomplete_name(fixture_query_name):
    url = f'https://api.openbrewerydb.org/breweries/autocomplete?query={fixture_query_name}'
    response = requests.get(url=url)
    json_response = response.json()
    assert type(json_response) == list
# Не работает проверка вхождения слова поиска query= в название пивных тк Autocomplete выдает пивные не только по
# совпадению с названием
# if len(json_response) != 0:
#     for query_name in json_response:
#         query_name = query_name.get('name')
#         print(query_name)
#         query_name = query_name.lower()
#         query_symbol = [fixture_query_name]
#         coincidental = [e for e in query_symbol if e in query_name]
#         assert coincidental == [f'{fixture_query_name}']


# Тестируем совпадение ID и названия бара, полученного через Get Brewery по данному ID
def test_id_get_brewery(test_input, expected_result):
    url = f'https://api.openbrewerydb.org/breweries/{test_input}'
    response = requests.get(url=url)
    json_response = response.json()
    assert json_response.get('name') == expected_result
