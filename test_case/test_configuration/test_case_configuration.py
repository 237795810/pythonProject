import pytest
import allure
import requests
from api_method.Configuration import Configuration_module
from common_method.connect_sqlite import select_sqlite_system, execute_sqlite_system
from test_case.test_configuration.conftest import get_test_data

# class Test_configiguration(object):

# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("配置")
@allure.story("agv配置新增数据")
@allure.title("新增数据成功")
@pytest.mark.parametrize("is_enable, carrier_index, type_, shape_type, carrier_length, carrier_width, home_station,"
                         "int_start_vertex, is_home_station, is_start_vertex, code", [get_test_data()["data01"]])
def test_agv_configuration_01(base_url, is_enable, carrier_index, type_, shape_type, carrier_length, carrier_width,
                              home_station, int_start_vertex, is_home_station, is_start_vertex, code):
    execute_sqlite_system("delete from carrier where CarrierIndex = 3")
    s = requests.Session()
    api = Configuration_module(s, base_url)
    r = api.add_agv_configuration(is_enable, carrier_index, type_, shape_type, carrier_length, carrier_width,
                                  home_station, int_start_vertex, is_home_station, is_start_vertex)
    assert r.json()["code"] == code
    assert r.status_code == 200

# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("配置")
@allure.story("删除配置")
@allure.title("删除配置成功")
@pytest.mark.parametrize("number, started, type_, share_type, long, width, standpoint, "
                         "stand_point_flag, enable, enable_flag, code", [get_test_data()["data02"]])
def test_agv_configuration_02(base_url, number, started, type_, share_type, long, width, standpoint, stand_point_flag, enable,
                              enable_flag, code):
    s = requests.Session()
    api = Configuration_module(s, base_url)
    api.add_agv_configuration(started, number, 0, share_type, long, width, standpoint, enable, stand_point_flag, enable_flag)
    # time.sleep(5)
    re = select_sqlite_system("select * from Carrier where CarrierIndex = {}".format(number))
    if re is not None:
        r = api.delete_configuration(number, started, type_, share_type, long, width, standpoint, stand_point_flag, enable, enable_flag)
        assert r.json().get("code") == code
        assert r.status_code == 200
    else:
        print("新增数据失败,删除无法判断")
        assert 1 > 1


# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("配置")
@allure.story("修改配置")
@allure.title("修改配置成功")
@pytest.mark.parametrize("id_, is_enable, carrier_index, type_, shape_type, carrier_length, carrier_width, home_station, int_start_vertex, is_home_station, is_start_vertex, code", [get_test_data()["data03"]])
def test_agv_configuration_03(base_url, id_, is_enable, carrier_index, type_, shape_type, carrier_length, carrier_width, home_station, int_start_vertex, is_home_station, is_start_vertex, code):
    s = requests.Session()
    api = Configuration_module(s, base_url)
    """新增一条数据"""
    api.add_agv_configuration("true", id_, 0, 1, 300, 500, 22, 47, "true", "true")
    """删除旧数据"""
    execute_sqlite_system("delete from carrier where CarrierIndex = {}".format(carrier_index))
    """新增的ID不会变，所以要去取值ID，此时ID为 上述id传入的参数"""
    r = api.updata_configuration(id_, is_enable, carrier_index, type_, shape_type, carrier_length, carrier_width,
                                   home_station, int_start_vertex, is_home_station, is_start_vertex)
    assert r.json().get("code") == code
