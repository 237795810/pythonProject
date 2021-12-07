import requests
import pytest
from test_case.test_monitor.conftest import get_test_data
from api_method.monitor_api import Move_agv
from common_method.connect_sqlite import select_sqlite_system
import allure


# pytest.mark.skip(reason="no way of currently testing this")
# noinspection PyTestParametrized
@allure.feature("监控")
@allure.story("执行强制任务导航")
@allure.title("执行导航点任务成功")
@allure.severity("critical")
@pytest.mark.parametrize("carrier_index, vertex, code", [get_test_data()["data01"]])
def test_mon01(base_url, carrier_index, vertex, code):
    """监控页面强制任务测试用例--导航点"""
    s = requests.Session()
    api = Move_agv(s, base_url)
    r = api.move_agvs_navigation(carrier_index, vertex)
    assert r.json()["code"] == code
    assert r.status_code == 200

# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("监控")
@allure.story("执行强制任务站点")
@allure.title("执行强制任务站点成功")
@allure.severity("critical")
@pytest.mark.parametrize("carrier_index, station, action, code", [get_test_data()["data02"]])
def test_mon02(base_url, carrier_index, station, action, code):
    """监控页面强制任务测试用例--站点任务"""
    s = requests.Session()
    api = Move_agv(s, base_url)
    r = api.move_agvs_site(carrier_index, station, action)
    assert r.json()["code"] == code
    assert r.status_code == 200


# pytest.mark.skip(reason="no way of currently testing this")
@allure.severity("critical")
@allure.feature("监控")
@allure.story("全部暂停")
@allure.title("暂停全部AGV成功")
@allure.severity("critical")
def test_mon3(base_url):
    """全部暂停"""
    s = requests.session()
    api = Move_agv(s, base_url)
    r = api.carrier_list_pause()
    assert r.json()["code"] == 20000
    assert r.status_code == 200


# pytest.mark.skip(reason="no way of currently testing this")
@allure.severity("critical")
@allure.feature("监控")
@allure.story("全部恢复")
@allure.title("恢复全部AGV成功")
@allure.severity("critical")
def test_mon4(base_url):
    """全部恢复"""
    s = requests.session()
    api = Move_agv(s, base_url)
    r = api.carrier_list_resume()
    assert r.json()["code"] == 20000
    assert r.status_code == 200


# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("监控")
@allure.story("单个暂停")
@allure.title("暂停单个AGV成功")
@allure.severity("critical")
@pytest.mark.parametrize("data, code", [get_test_data()["data03"]])
def test_mon5(base_url, data, code):
    """单个暂停
    data： 编号
    """
    s = requests.session()
    api = Move_agv(s, base_url)
    r = api.carrier_list_pause()
    assert r.json()["code"] == 20000
    assert r.status_code == 200


# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("监控")
@allure.story("单个恢复")
@allure.title("恢复单个AGV成功")
@allure.severity("critical")
@pytest.mark.parametrize("data, code", [get_test_data()["data04"]])
def test_mon6(base_url, data, code):
    """单个恢复"""
    s = requests.session()
    api = Move_agv(s, base_url)
    r = api.carrier_list_resume()
    assert r.json()["code"] == 20000
    assert r.status_code == 200


# pytest.mark.skip(reason="no way of currently testing this")
@allure.severity("normal")
@allure.feature("状态")
@allure.story("查看状态")
@allure.title("查看状态数据返回成功")
def test_mon7(base_url):
    s = requests.session()
    api = Move_agv(s, base_url)
    r = api.look_status()
    assert r.json()["code"] == 20000
    assert r.status_code == 200


# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("告警")
@allure.story("历史告警查询")
@allure.title("查询历史告警成功")
@allure.severity("normal")
@pytest.mark.parametrize("start_time ,end_time, code", [get_test_data()["data05"]])
@pytest.mark.parametrize("level", get_test_data()["data06"])
def test_mon8(base_url, start_time, end_time, level, code):
    """        s = requests.session()
    a =Move_agv(s,base_url="http://localhost:9528")
    r = a.alarm_find("2021-12-01 00:00:00", "2021-12-02 23:59:59", 1)
    print(r)"""
    s = requests.session()
    api = Move_agv(s, base_url)
    r = api.alarm_find(start_time, end_time, level)
    assert r.json()["code"] == 20000
    assert r.status_code == 200


# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("监控")
@allure.story("呈现设置")
@allure.title("设置车辆车型成功")
@allure.severity("normal")
@pytest.mark.parametrize("carrier_index, shape_type, is_home_station, is_start_vertxe, code", [get_test_data()["data07"]])
def test_mon_09(base_url, carrier_index, shape_type, is_home_station, is_start_vertxe, code):
    s = requests.session()
    api = Move_agv(s, base_url)
    data = select_sqlite_system("select ShapeType from Carrier where CarrierIndex = {}".format(carrier_index))[0][0]
    if data == 3:
        shape_type = 1
    r = api.update_carrier_info(carrier_index, shape_type, is_home_station, is_start_vertxe)
    assert r.json()["code"] == code
    assert r.status_code == 200
