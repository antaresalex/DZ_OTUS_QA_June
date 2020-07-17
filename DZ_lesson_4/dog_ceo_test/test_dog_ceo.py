import pytest
import requests

#Тестируем получение статус кода 200 OK
def test_breed_random(fixture_dogceo_random):
	url = f'https://dog.ceo/api/breed/{fixture_dogceo_random}/images/random'
	responce = requests.get(url=url)
	assert responce.status_code == 200


#Проверка рандомного получения пароды

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