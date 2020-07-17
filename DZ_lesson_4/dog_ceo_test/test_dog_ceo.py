import pytest
import requests
import json

#Тестируем получение json со всеми породами LIST ALL BREEDS
#https://dog.ceo/api/breeds/list/all
#записываем его в json breeds.json
def test_all_breeds_list():
	url = 'https://dog.ceo/api/breeds/list/all'
	responce = requests.get(url=url)
	with open('breeds.json', 'w') as breed_data:
		responce = json.dumps(responce, indent=4)
		breed_data.write(responce)
	assert responce.status_code == 200

#Тестируем получение SINGLE RANDOM IMAGE FROM ALL DOGS

#Тестируем получение всех картинок по указанной породе

#Тестируем получение LIST ALL SUB-BREEDS по запрашиваемой породе

#Проверка рандомного получения фото из породы BREEDS LIST
# def test_breed_random(fixture_dogceo_random):
# 	url = f'https://dog.ceo/api/breed/{fixture_dogceo_random}/images/random'
# 	responce = requests.get(url=url)
# 	assert responce.status_code == 200

# #Тестируем метод c параметризацией
# #Тестируем метод sort у list
# #Получаем на вход список длинной 5
# @pytest.mark.parametrize('x', [1, 4, 9, 7])
# def test_sort_element(fixture_someone_list, x):
# 	fixture_someone_list.append(x)
# 	fixture_someone_list.sort()
# 	min_number = min(fixture_someone_list)
# 	max_number = max(fixture_someone_list)
# 	assert fixture_someone_list.index(min_number) == 0
# 	assert fixture_someone_list.index(max_number) == 5

# #Тестируем метод c параметризацией
# #Тестируем метод clear у list
# #Получаем на вход список длинной 5 и добавляем разные значения до очистки
# def test_clear_element(fixture_someone_list, fixture_with_params):
# 	fixture_someone_list.append(fixture_with_params)
# 	fixture_someone_list.clear()
# 	assert len(fixture_someone_list) == 0