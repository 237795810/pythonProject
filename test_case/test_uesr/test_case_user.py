import pytest
import allure
import requests
from api_method.add_uesr import User_project
from common_method.connect_sqlite import execute_sqlite_system
from test_case.test_uesr.contest import get_test_data

@allure.feature("用户")
@allure.story("用户列表添加用户")
@allure.title("添加角色成功")
@allure.severity("normal")
@pytest.mark.parametrize("role_name, description, code", [get_test_data()["data01"]])
def test_case_user_001(base_url, role_name, description, code):
    s = requests.session()
    api = User_project(s, base_url)
    execute_sqlite_system("delete from role where RoleName = '{}'".format(role_name))
    r = api.add_role(role_name, description)
    assert r.status_code == 200
    assert r.json().get("code") == code

@allure.feature("用户")
@allure.story("用户列表删除role")
@allure.title("删除role成功")
@allure.severity("normal")
@pytest.mark.parametrize("role_name, description, code", [get_test_data()["data02"]])
def test_case_user_002(base_url, role_name, description, code):
    s = requests.session()
    api = User_project(s, base_url)
    api.add_role(role_name, description)
    r = api.delete_role(role_name)
    assert r.status_code == 200
    assert r.json().get("code") == code

@allure.feature("用户")
@allure.story("用户列表修改role")
@allure.title("修改role成功")
@allure.severity("normal")
@pytest.mark.parametrize("role_name, description, code", [get_test_data()["data03"]])
def test_case_user_003(base_url, role_name, description, code):
    s = requests.session()
    api = User_project(s, base_url)
    execute_sqlite_system("delete from role where RoleName = '{}'".format(role_name))
    api.add_role("test007","8888")
    r = api.updata_role(role_name, description)
    print(r.json())
    assert r.status_code == 200
    assert r.json().get("code") == code

@allure.feature("用户")
@allure.story("新增用户")
@allure.title("新增成功")
@allure.severity("normal")
@pytest.mark.parametrize("name, role, code", [get_test_data()["data04"]])
def test_case_user_004(base_url, name, role, code):
    s = requests.session()
    api = User_project(s, base_url)
    execute_sqlite_system("delete from User where name = '{}'".format(name))
    r = api.add_user_name(name, role)
    assert r.status_code == 200
    assert r.json().get("code") == 20000

@allure.feature("用户")
@allure.story("删除用户")
@allure.title("删除成功")
@allure.severity("normal")
@pytest.mark.parametrize("name, role, code", [get_test_data()["data05"]])
def test_case_user_005(base_url, name, role, code):
    s = requests.session()
    api = User_project(s, base_url)
    api.add_user_name(name, role)
    r = api.del_user_name(name)
    assert r.status_code == 200
    assert r.json().get("code") == 20000

@allure.feature("用户")
@allure.story("修改用户密码")
@allure.title("修改成功")
@allure.severity("normal")
@pytest.mark.parametrize("name, role, role_up, code", [get_test_data()["data06"]])
def test_case_user_006(base_url, name, role, role_up, code):
    s = requests.session()
    api = User_project(s, base_url)
    api.add_user_name(name, role)
    r = api.updata_user_name(name, role_up)
    assert r.status_code == 200
    assert r.json().get("code") == code


