import pytest
from main import create_folder_yandex_disc,token
import requests
params = [('test_1', 201), ('test_1', 409)]
@pytest.mark.parametrize('name_folder, expected', params)
def test_create_folder_yandex_disk(name_folder, expected):
    assert create_folder_yandex_disc(name_folder) == expected
@pytest.fixture()
def presence_of_folder():
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    param = {'path': 'test_1'}
    headers = {'Authorization': f'OAuth {token}'}
    response = requests.get(url, params=param, headers=headers)
    status = response.status_code
    return status

def test_has_the_folder_appeared(presence_of_folder):
    assert presence_of_folder == 200