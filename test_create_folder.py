import pytest
from main import create_folder_yandex_disc,token
import requests
params = [('test_1', 201), ('test_1', 409)]
@pytest.mark.parametrize('name_folder, expected', params)
def test_create_folder_yandex_disk(name_folder, expected):
    assert create_folder_yandex_disc(name_folder) == expected
params = (('test_1',200),)
@pytest.mark.parametrize('name_folder, expected',params)
def test_has_the_folder_appeared(name_folder,expected):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    param = {'path': 'disk:/',
             'fields': '_embedded.items.path,_embedded.items.type'}
    headers = {'Authorization': f'OAuth {token}'}
    response = requests.get(url, params=param, headers=headers)
    data = response.json()
    folder_exist = 404
    for i in data['_embedded']['items']:
        if i['path'] == f'disk:/{name_folder}':
            folder_exist = 200
    status = response.status_code
    assert folder_exist == expected

