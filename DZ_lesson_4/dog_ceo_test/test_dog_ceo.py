import pytest
import requests
import json

#Тестируем получение json со всеми породами LIST ALL BREEDS, проверяем статус код на 200
#Функция скачивает через API данные и сохраняет их в json, используем generate_test
def pytest_generate_tests(metafunc):
    if 'test_input' not in metafunc.fixturenames:
        return
    url = 'https://dog.ceo/api/breeds/list/all'
    responce = requests.get(url)
    if responce.status_code == 200:
        get_responce = responce.json()
    else:
        print('Server is not responding now')
    if not get_responce:
        raise ValueError('Get_responce in not loaded')
    breed_dict = get_responce.get('message')
    breed_subbreed = breed_dict.items()
    with open('breeds.json', 'w') as breed_data:
        get_responce = json.dumps(get_responce, indent=4)
        breed_data.write(get_responce)
    return metafunc.parametrize('test_input, expected_result', breed_subbreed)

#Тестируем получение LIST ALL SUB-BREEDS по запрашиваемой породе
def test_list_all_subbreeds(test_input, expected_result, fixture_dog_api_url):
    url = fixture_dog_api_url+f'breed/'+str(test_input)+f'/list'
    responce = requests.get(url)
    if responce.status_code == 200:
        get_responce = responce.json()
    else:
        print('Server is not responding now')
    if not get_responce:
        raise ValueError('Get_responce in not loaded')
    list_all_subbreeds = get_responce.get('message')
    assert list_all_subbreeds == expected_result

# Тестируем получение MULTIPLE IMAGES FROM A SUB-BREED COLLECTION
def test_multiple_image_subbreed(test_input, expected_result, fixture_dog_api_url, fixture_number_all_subbreed_image):
    if len(expected_result) != 0:
        url = fixture_dog_api_url+f'breed/'+str(test_input)+f'/'+str(expected_result[0])+f'/images/random/'+str(fixture_number_all_subbreed_image)
        responce = requests.get(url)
        if responce.status_code == 200:
            get_responce = responce.json()
        else:
            print('Server is not responding now')
        if not get_responce:
            raise ValueError('Get_responce in not loaded')
        list_image_multiple_subbreed = get_responce.get('message')
        assert len(list_image_multiple_subbreed) == int(fixture_number_all_subbreed_image)
    else:
        print('Breed don\'t have any sub-breed')

#Тестируем получение DISPLAY MULTIPLE RANDOM IMAGES FROM ALL DOGS COLLECTION 
#Рандомно перебираем числа до 50 и сравниваем полученное число элементов в листе в значении (должно совпадать))
@pytest.mark.parametrize('number', [1, 4, 9, 7, 30, 50, 49, 25])
def test_breeds_image_random(fixture_dog_api_url, number):
    url = fixture_dog_api_url+f'breeds/image/random/'+str(number)
    responce = requests.get(url)
    if responce.status_code == 200:
        get_responce = responce.json()
    else:
        print('Server is not responding now')
    if not get_responce:
        raise ValueError('Get_responce in not loaded')
    list_image_random = get_responce.get('message')
    assert len(list_image_random) == int(number)

#Тестируем получение DISPLAY SINGLE RANDOM IMAGE FROM ALL DOGS COLLECTION
def test_breeds_image_random_one(fixture_dog_api_url):
    url = fixture_dog_api_url+f'breeds/image/random/'
    responce = requests.get(url)
    if responce.status_code == 200:
        get_responce = responce.json()
    else:
        print('Server is not responding now')
    if not get_responce:
        raise ValueError('Get_responce in not loaded')
    image_random = get_responce.get('message')
    jpg_symbol = ['.jpg']
    coincidental = [e for e in jpg_symbol if e in image_random]
    assert coincidental == jpg_symbol
    