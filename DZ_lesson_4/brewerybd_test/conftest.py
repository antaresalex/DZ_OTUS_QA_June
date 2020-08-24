import pytest
from pytest import fixture
import requests


@fixture(params=['dog', 'green', 'fun', 'bar', 'music', 'pub', 'dance'])
def fixture_query_name(request):
    return request.param


@fixture(params=['micro', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'proprietor'])
def fixture_by_type(request):
    return request.param


file = open('url_city.txt', 'r')
r = file.readlines()
new_lst = [i.replace(' ', '_') for i in r]
new_lst = [i.lower() for i in r]
new_lst = [i.strip('\n') for i in r]
file.close()


@fixture(name='url_city', params=new_lst)
def get_url_city(request):
    yield request.param


def pytest_generate_tests(metafunc):
    if 'test_input' not in metafunc.fixturenames:
        return
    url = 'https://api.openbrewerydb.org/breweries'
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.json()
        brewery_list_all = []
        for brewery in json_response:
            brewery_id = brewery.get('id')
            brewery_name = brewery.get('name')
            brewery_list = [brewery_id, brewery_name]
            brewery_list_all.append(brewery_list)
        return metafunc.parametrize('test_input, expected_result', brewery_list_all)
    else:
        raise Exception('RequestException, HTTP Code != 200')
