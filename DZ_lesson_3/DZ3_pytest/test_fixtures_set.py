import pytest

#Тестируем метод copy у set
#Получаем на вход set длинной 7
def test_copy_set(fixture_set):
	copy_fixture_set = fixture_set.copy()
	assert fixture_set == copy_fixture_set

#Тестируем метод add у set
#Получаем на вход set длинной 7
def test_add_set(fixture_set):
	fixture_set.add(7)
	assert len(fixture_set) == 8

#Тестируем метод c параметризацией
#Тестируем метод clear у set
#Получаем на вход set длинной 7 и добавляем разные значения до очистки
def test_clear_set(fixture_set, fixture_with_params):
	fixture_set.add(fixture_with_params)
	fixture_set.clear()
	assert len(fixture_set) == 0

#Тестируем метод isdisjoint у set
#Получаем на вход set длинной 7
def test_isdisjoint_set(fixture_set):
	other = fixture_set
	assert fixture_set.isdisjoint(other) == False

#Тестируем метод pop у set
#Получаем на вход set длинной 7
def test_pop_set(fixture_set):
	fixture_set.pop()
	assert len(fixture_set) == 6

