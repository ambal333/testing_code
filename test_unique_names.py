import pytest
from main import unique_names


params = [(['Олег Булыгин','Дмитрий Демидов'],'Дмитрий, Олег')]
@pytest.mark.parametrize('name,expected',params)
def test_only_names(name,expected):
    assert unique_names(name) == expected

params = [(['Олег Булыгин','Дмитрий Демидов','Олег Булыгин'],'Дмитрий, Олег')]
@pytest.mark.parametrize('names, expected',params)
def test_unique_name_list(names,expected):
    assert unique_names(names) == expected

