import pytest
from main import create_folder_yandex_disc

params = [('test_1', 201), ('test_1', 409)]
@pytest.mark.parametrize('name_folder, expected', params)
def test_create_folder_yandex_disk(name_folder, expected):
    assert create_folder_yandex_disc(name_folder) == expected

