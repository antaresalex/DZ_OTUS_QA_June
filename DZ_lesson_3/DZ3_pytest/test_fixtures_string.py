import pytest

#Тестируем конкатенцию у string
#Получаем на вход строку
#Используем параметризацию
def test_plus_sting(fixture_string, fixture_with_params):
	old_len_string = len(fixture_string)
	fixture_string = fixture_string + str(fixture_with_params)
	print(fixture_string)
	assert len(fixture_string) == old_len_string + int(len(str(fixture_with_params)))

#Тестируем метод определяющий состоит ли строка из числел
#Подаем в функцию строку из букв
def test_isdigit_string(fixture_string):
	assert fixture_string.isdigit() == False

#Тестируем метод, где мы задаем длину строки 
#Подаем строку меньшей длины, чем задаем методом
def test_ljust_string(fixture_string):
	new_len_string = fixture_string.ljust(70, "w")
	print(len(fixture_string))
	print(len(new_len_string))
	assert len(new_len_string) == 70

#Тестируем повторение строки
def test_repeat_string(fixture_string):
	assert len(fixture_string * 3) == len(fixture_string) * 3
