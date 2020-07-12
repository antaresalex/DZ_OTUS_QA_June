import pytest

#Тестируем метод remove у list
#Получаем на вход список длинной 5
def test_remove_element(fixture_someone_list):
	fixture_someone_list.remove(1)
	assert len(fixture_someone_list) == 4

#Тестируем метод append у list
#Получаем на вход список длинной 5
def test_append_element(fixture_someone_list):
	fixture_someone_list.append(7)
	assert len(fixture_someone_list) == 6

#Тестируем метод count у list
#Получаем на вход список длинной 5
def test_count_element(fixture_someone_list):
	count_number = fixture_someone_list.count(2)
	assert count_number == 1
	fixture_someone_list.append(2)
	count_number = fixture_someone_list.count(2)
	assert count_number == 2

#Тестируем метод c параметризацией
#Тестируем метод sort у list
#Получаем на вход список длинной 5
@pytest.mark.parametrize('x', [1, 4, 9, 7])
def test_sort_element(fixture_someone_list, x):
	fixture_someone_list.append(x)
	fixture_someone_list.sort()
	min_number = min(fixture_someone_list)
	max_number = max(fixture_someone_list)
	assert fixture_someone_list.index(min_number) == 0
	assert fixture_someone_list.index(max_number) == 5

#Тестируем метод c параметризацией
#Тестируем метод clear у list
#Получаем на вход список длинной 5 и добавляем разные значения до очистки
def test_clear_element(fixture_someone_list, fixture_with_params):
	fixture_someone_list.append(fixture_with_params)
	fixture_someone_list.clear()
	assert len(fixture_someone_list) == 0
