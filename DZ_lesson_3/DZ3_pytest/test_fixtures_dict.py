import pytest

#Тестируем метод keys у dict
#Получаем на вход dict
def test_keys_dict(fixture_dict):
	keys_dict = fixture_dict.keys()
	assert len(keys_dict) != 0

#Тестируем метод get у dict 
#Используем параметризацию
#Получаем на вход dict
#Два теста из 3 не проваливаются, 2 не проходят
def test_get_dict(fixture_dict, fixture_with_params):
	m_dict = fixture_dict.get(fixture_with_params)
	if m_dict == None:
		print('Ключа нет в словаре')
	else:
		assert m_dict != None

#Тестируем метод copy у dict 
def test_copy_dict(fixture_dict):
	copy_dict = fixture_dict.copy()
	assert copy_dict == fixture_dict

#Тестируем метод clear у dict 
def test_clear_dict(fixture_dict):
	fixture_dict.clear()
	assert len(fixture_dict) == 0

