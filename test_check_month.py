import pytest
from main import check_month

params = [('Зима', 12), ('Зима', 1), ('Зима', 2),
          ('Весна', 3), ('Весна', 4), ('Весна', 5),
          ('Лето', 6), ('Лето', 7), ('Лето', 8),
          ('Осень', 9), ('Осень', 10), ('Осень', 11)]
@pytest.mark.parametrize('expected, correct_number',params)
def test_number_month(correct_number, expected):
   assert check_month(correct_number) == expected
@pytest.mark.xfail
def test_incorrect_number():
    assert check_month(12) == 'Лето'

def test_incorrect_number_of_month():
    assert check_month(13) == 'Некорректный номер месяца'





















# def test_main_1():
#     assert summarise(12,5) == 17
#
# @pytest.mark.xfail
# def test_main_2():
#     assert summarise(0,7) == 7
#
# @pytest.mark.skipif(True, reason='Боевой сервер')
# def test_main_3():
#     assert summarise(0,7) == 7
#
# params = [(12,5,17),(1,7,8),(2,4,6)]
#
# @pytest.mark.parametrize('x,y,expected',params)
# def test_with_params(x, y, expected):
#     assert summarise(x,y) == expected
