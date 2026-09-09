from main import order_courses
import pytest

params = [(['Python-разработчик с нуля','Java-разработчик с нуля'],['12', '14'],'Python-разработчик с нуля, 12 месяцев\n'
                                                                                                'Java-разработчик с нуля, 14 месяцев')]
@pytest.mark.parametrize('courses, durations, expected',params)
def test_result_order_courses(courses, durations, expected):
    assert order_courses(courses, durations) == expected