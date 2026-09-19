# первое задание



def check_month(month: int):
    if month == 12 or month == 1 or month == 2:
        result = 'Зима'
    elif month == 3 or month == 4 or month == 5:
        result = 'Весна'
    elif month == 6 or month == 7 or month == 8:
        result = 'Лето'
    elif month == 9 or month == 10 or month == 11:
        result = 'Осень'
    else:
        result = 'Некорректный номер месяца'
    return result

# второе задание
def unique_names(mentors: list) -> str:
    names = set()
    for i in mentors:
        name_parts = i.split()
        name = name_parts[0]
        names.add(name)
    sorted_names = list(names)
    sorted_names = sorted(sorted_names)
    result = ', '.join(sorted_names)
    return result

def vk_api_connect():
    return 'connect'
# третье задание
def order_courses(courses: list, durations: list) -> str:
    durations_dict = {}
    for idx, course in enumerate(courses):
        key = durations[idx]
        durations_dict.setdefault(key,[])
        durations_dict[key].append(course)
    durations_dict = sorted(durations_dict.items())
    durations_dict=dict(durations_dict)
    result = []
    for u,j in durations_dict.items():
        if len(j)==1:
            result.append(f'{j[0]}, {u} месяцев')
        else:
            for i in j:
                result.append(f'{i}, {u} месяцев')
    result='\n'.join(result)
    return result

def new_function():
    pass
# Задача №2 Автотест API Яндекса
import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('YANDEX_DISC_TOKEN')

def create_folder_yandex_disc(name_folder):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': f'{name_folder}'}
    response = requests.put(url,params=params, headers=headers)
    # response.raise_for_status()
    data = response.json()
    status = response.status_code
    return status
# print(create_folder_yandex_disc('test_2'))

def db_connection():
    pass

def vk_api_create_user():
    user = 'create.user'
    return user