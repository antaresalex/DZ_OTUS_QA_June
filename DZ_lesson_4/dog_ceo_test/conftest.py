import pytest
import requests
import json


@pytest.fixture()
def fixture_dog_api_url():
    return 'https://dog.ceo/api/'


# Получение количества всех картинок по указанной подпороде LIST ALL SUB-BREED IMAGES
@pytest.fixture()
def fixture_number_all_subbreed_image(test_input, expected_result, fixture_dog_api_url):
    if len(expected_result) != 0:
        url = fixture_dog_api_url + f'breed/' + str(test_input) + '/' + str(expected_result[0]) + f'/images'
        responce = requests.get(url)
        if responce.status_code == 200:
            get_responce = responce.json()
        else:
            print('Server is not responding now')
        if not get_responce:
            raise ValueError('Get_responce in not loaded')
        list_image_multiple_subbreed = get_responce.get('message')
        number_image_subbreed = len(list_image_multiple_subbreed)
        return number_image_subbreed
