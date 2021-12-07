import requests
import pytest
from test_case.test_task.conftest import get_test_data
from common_method.connect_sqlite import execute_sqlite_pms_v4,select_sqlite_pms_v4
from api_method.Task_api import Task_configuration
import allure


# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("任务-任务配置-库位设置")
@allure.story("重复添加库位失败，首次添加库位成功")
@allure.title("添加库位数据成功，重复添加库位数据失败")
@allure.severity("blocker")
@pytest.mark.parametrize("ware_house_id, ware_house_name, station_id, code", [get_test_data()["data01"], get_test_data()["data02"]])
def test_location_setting_01(base_url, ware_house_id, ware_house_name, station_id, code):
    """避免数据库存在该数据，所以先删除"""
    execute_sqlite_pms_v4("delete FROM WarehouseInfo where WarehouseName = 3")
    s = requests.session()
    """调用类"""
    api = Task_configuration(s, base_url)
    """调用类下面对应方法"""
    r = api.location_settings(ware_house_id, ware_house_name, station_id)
    assert r.json()["code"] == code
    assert r.status_code == 200

# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("任务-任务配置-库位设置")
@allure.story("删除库位")
@allure.title("删除库位成功")
@allure.severity("normal")
@pytest.mark.parametrize("data, code", [get_test_data()["data03"]])
def test_location_setting_02(base_url, data, code):
    execute_sqlite_pms_v4("delete FROM WarehouseInfo where WarehouseName = 2")
    s = requests.session()
    api = Task_configuration(s, base_url)
    """调用类下面对应方法"""
    api.location_settings("8", "2", 8)
    api = Task_configuration(s, base_url)
    r = api.delete_location(data)
    assert r.json()["code"] == code
    assert r.status_code == 200

# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("任务-任务配置-库位设置")
@allure.story("修改库位")
@allure.title("修改库位成功")
@allure.severity("normal")
@pytest.mark.parametrize("ware_house_id, ware_house_name, station_id, code", [get_test_data()["data04"]])
def test_location_setting_03(base_url, ware_house_id, ware_house_name, station_id, code):
    execute_sqlite_pms_v4("delete from WareHouseInfo where WarehouseID = 66")
    s = requests.session()
    api = Task_configuration(s, base_url)
    api.location_settings(ware_house_id, 77, 33)
    r = api.updata_location(ware_house_id, ware_house_name, station_id)
    assert r.json()["code"] == code
    assert r.status_code == 200

# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("任务-任务配置-模板配置")
@allure.story("执行任务模板")
@allure.title("执行任务模板成功")
@allure.severity("critical")
@pytest.mark.parametrize("book_name, count, car_nums, agv_id, code", [get_test_data()["data05"]])
def test_location_setting_04(base_url, book_name, count, car_nums, agv_id, code):
    s = requests.session()
    api = Task_configuration(s, base_url)
    r = api.execution_template(book_name, count, car_nums, agv_id)
    assert r.json()["code"] == code
    assert r.status_code == 200

# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("任务-任务配置-库位设置")
@allure.story("添加库位组")
@allure.title("添加库位组添加动作成功")
@allure.severity("critical")
@pytest.mark.parametrize("warehouse_type, remark, operation_name, param1, param2, param3, code, message", [get_test_data()["data06"]])
def test_location_setting_05(base_url, warehouse_type, remark, operation_name, param1, param2, param3, code, message):
    execute_sqlite_pms_v4("DELETE FROM WarehouseGroupInfo WHERE WareHouseType = 'group1'")
    s = requests.session()
    api = Task_configuration(s, base_url)
    r = api.add_warehouse_group(warehouse_type, remark, operation_name, param1, param2, param3)
    assert r.json()["code"] == code
    assert r.status_code == 200
    assert r.json()["message"] == message

# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("任务-任务配置-库位设置")
@allure.story("修改库位组名称")
@allure.title("修改库位组名称成功")
@allure.severity("critical")
@pytest.mark.parametrize("warehouse_type, remark, message, code", [get_test_data()["data07"]])
def test_location_setting_06(base_url, warehouse_type, remark, message, code):
    s = requests.session()
    api = Task_configuration(s, base_url)
    execute_sqlite_pms_v4("DELETE FROM WarehouseGroupInfo WHERE WareHouseType = 9")
    api.add_warehouse_group(warehouse_type, remark, "Laserlift", 1, 1, 1)
    group_id = select_sqlite_pms_v4("select GroupId from WarehouseGroupInfo where WareHouseType =9 and Param1=0")[0][0]
    r = api.update_group_by_id(group_id, warehouse_type, remark)
    assert r.json()["code"] == code
    assert r.status_code == 200
    assert r.json().get("message") == message

# pytest.mark.skip(reason="no way of currently testing this")
def test_location_setting_07():
    """修改库位里的动作"""
    pass

# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("任务-任务配置-库位设置")
@allure.story("删除库位组")
@allure.title("删除库位组成功")
@allure.severity("critical")
@pytest.mark.parametrize("warehouse_type, remark, message, code", [get_test_data()["data08"]])
def test_location_setting_08(base_url, warehouse_type, remark, message, code):
    s = requests.session()
    api = Task_configuration(s, base_url)
    api.add_warehouse_group(warehouse_type, remark, "Laserlift", 3, 3, 3)
    group_id = select_sqlite_pms_v4("select GroupId from WarehouseGroupInfo where WareHouseType ={} and Param1=0".format(warehouse_type))[0][0]
    r = api.delete_group_by_id(group_id)
    assert r.json().get("code") == code
    assert r.status_code == 200
    assert r.json().get("message") == message

# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("任务-任务查询-历史任务")
@allure.story("查询任务")
@allure.title("查询成功")
@allure.severity("critical")
@pytest.mark.parametrize("task_id, code", [get_test_data()["data09"]])
def test_location_setting_08(base_url, task_id, code):
    s = requests.session()
    api = Task_configuration(s, base_url)
    r = api.find_task(task_id)
    assert r.status_code == 200
    assert r.json().get("code") == code

# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("任务-任务配置-动作配置")
@allure.story("添加动作")
@allure.title("添加动作成功")
@allure.severity("critical")
@pytest.mark.parametrize("name, code, is_agv_behavior, remark, is_edit, is_delete, code1", [get_test_data()["data10"]])
def test_location_setting_09(base_url, name, code, is_agv_behavior, remark, is_edit, is_delete, code1):
    s = requests.session()
    api= Task_configuration(s, base_url)
    execute_sqlite_pms_v4("delete from OperateInfo where Name = {}".format(name))
    r = api.add_operate(name, code, is_agv_behavior, remark, is_edit, is_delete)
    assert r.json().get("code") == code1
    assert r.status_code == 200

# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("任务-任务配置-动作配置")
@allure.story("删除动作")
@allure.title("删除动作成功")
@allure.severity("critical")
@pytest.mark.parametrize("name, code, is_agv_behavior, remark, is_edit, is_delete, code1", [get_test_data()["data11"]])
def test_location_setting_10(base_url, name, code, is_agv_behavior, remark, is_edit, is_delete, code1):
    s = requests.session()
    api = Task_configuration(s, base_url)
    api.add_operate(name, code, is_agv_behavior, remark, is_edit, is_delete)
    r = api.delete_operate(name)
    assert r.json().get("code") == code1
    assert r.status_code == 200

# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("任务-任务配置-动作配置")
@allure.story("修改动作")
@allure.title("修改动作成功")
@allure.severity("critical")
@pytest.mark.parametrize("name, code, code2, is_agv_behavior, is_agv_behavior_2, remark, remark_2, is_edit, is_delete, code1", [get_test_data()["data12"]])
def test_location_setting_11(base_url, name, code, code2, is_agv_behavior, is_agv_behavior_2, remark, remark_2, is_edit, is_delete, code1):
    s = requests.session()
    api = Task_configuration(s, base_url)
    """先删除旧数据再，新增一个动作"""
    execute_sqlite_pms_v4("delete from OperateInfo where Name = '{}'".format(name))
    api.add_operate(name, code2, is_agv_behavior_2, remark_2, is_edit, is_delete)
    r = api.updata_operate(name, code, is_agv_behavior, remark, is_edit, is_delete)
    assert r.status_code == 200
    assert r.json().get("code") == code1

# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("任务-任务配置")
@allure.story("添加模板")
@allure.title("添加作成功")
@allure.severity("critical")
@pytest.mark.parametrize("name, describe, remark, code", [get_test_data()["data13"]])
def test_location_setting_12(base_url, name, describe, remark, code):
    s = requests.session()
    api = Task_configuration(s, base_url)
    execute_sqlite_pms_v4("delete from TaskBookInfo where Name = '{}'".format(name))
    r = api.add_task_book(name, describe, remark)
    assert r.status_code == 200
    assert r.json().get("code") == code

# pytest.mark.skip(reason="no way of currently testing this")
@allure.feature("AGV模块")
@allure.story("添加任务")
@allure.title("{title}")
@allure.severity("critical")
@pytest.mark.parametrize("title, task_id, agv_id, parameterse, template_name, code, message", get_test_data()["data14"])
def test_location_setting_13(base_url, title, template_name, code, message, task_id, agv_id, parameterse):
    print(task_id, template_name, agv_id, parameterse, code, message)
    s = requests.session()
    api = Task_configuration(s, base_url)
    r = api.add_task(task_id, template_name, agv_id, parameterse)
    print(r.json())
    assert r.status_code == 200
    pytest.assume(str(message) in str(r.json()))
    pytest.assume(str(code) in str(r.json()))
    allure.dynamic.title(title)

@allure.feature("AGV模块")
@allure.story("指派任务")
@allure.title("{title}")
@allure.severity("critical")
@pytest.mark.parametrize("task_id, agv_id, title, message", get_test_data()["data15"])
def test_location_setting_14(base_url, task_id, agv_id, title, message):
    s = requests.session()
    api = Task_configuration(s, base_url)
    r = api.change_agv(task_id, agv_id)
    print(r.json())
    pytest.assume(str(message) in str(r.json()))
    allure.dynamic.title(title)
