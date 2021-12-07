import allure
import pytest
import requests
from api_method.Statics_api import Statics_module
from test_case.test_statics.conftest import get_test_data


@allure.feature("统计模块")
@allure.story("查询任务")
@allure.title("查询成功")
@allure.severity("normal")
@pytest.mark.parametrize("start_time, end_time, code", [get_test_data()["data01"]])
def test_statics_01(base_url, start_time, end_time, code):
    s = requests.session()
    api = Statics_module(s, base_url)
    res = api.statics_find(start_time, end_time)
    assert res.status_code == 200
    assert res.json()["code"] == code
