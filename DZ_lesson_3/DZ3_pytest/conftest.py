import pytest

#Создаем список для тестирования
#Получаем список длинной 5
@pytest.fixture
def fixture_someone_list():
	return [1, 4, 3, 2, 5]

@pytest.fixture(params=[1, 4, 2, 6])
def fixture_with_params(request):
    return request.param

#Создаем set для тестирования
#Получаем set длинной 7
@pytest.fixture
def fixture_set():
	return {0, 1, 4, 64, 9, 16, 25}

@pytest.fixture
def fixture_dict():
	 fixture_dict = {a: a ** 2 for a in range(4)}
	 print(fixture_dict)
	 return fixture_dict


@pytest.fixture
def fixture_string():
	return "Конкатенация строки и параметра:\n "