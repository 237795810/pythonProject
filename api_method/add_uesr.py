import requests
from api_method.AGVS_login import get_token
from common_method.connect_sqlite import select_sqlite_system

class User_project(object):

    """初始化数据"""
    def __init__(self, s: requests.session(), base_url):
        self.s = s
        self.base_url = base_url

    """继承初始化数据，base_url写在配置文件中"""
    def add_role(self, role_name, description):
        api = self.base_url + "/api/User/AddRole"
        body = {
            "RoleName": role_name,
            "Description": description,
            "RolePermission":"["
                         "{\"name\":\"Map\","
                         "\"title\":\"监控\","
                         "},"
                         "{\"name\":\"BoardConfig\","
                         "\"title\":\"看板\"}"
                         "]"
        }
        headers = {
            "token": get_token()
        }
        r = self.s.post(api, body,headers=headers)
        return r

    def delete_role(self,role_name):
        api = self.base_url + "/api/User/DeleteRole"
        body = select_sqlite_system("select ID from role where RoleName = '{}'".format(role_name))[0][0]
        headers = {
            "token": get_token()
        }
        r = self.s.post(api, json=body, headers=headers)
        return r

    def updata_role(self, role_name, description):
        api = self.base_url + "/api/User/UpdateRole"
        id_ = select_sqlite_system("select ID from role where RoleName = 'test007'")[0][0]
        body = {
            "ID": id_,
            "RoleName": role_name,
            "Description": description,
            "RolePermission": "[{’name':'Map','title':'监控','disabled':'true'},{'name':'Statics','title':'统计'}]"
        }
        headers = {"token": get_token(),
                   "Content-Type": "application/json; charset=utf-8"
                   }
        r = self.s.post(api, json=body, headers=headers)
        return r

    def add_user_name(self, name, role):
        api = self.base_url + "/api/User/AddUser"
        body = {
            "Name": name,
             "Role": role,
             "Password": "YYPwCLM0pp1Wq3vIqFPVsKos472CmYfCrCv2fmK8YxP09TphrSSBvp1uGJXwYMP5RQ3og4ZswVRErssaxSHntRSZb3+w02GsfuXDKDkfoKNHXMAKCjgsCoqWEJxxMqNTJxF69zhpJxPps/JaFf5vHymBFzCzlBsZ+3f9PuQr2is="
        }

        headers = {
            "token": get_token()
                   }
        r = self.s.post(api, body, headers=headers)
        return r

    def del_user_name(self, name):
        api = self.base_url + "/api/User/DeleteUser"
        body = name
        headers = {
            "token": get_token()}
        r = self.s.post(api, json=body, headers=headers)
        return r

    def updata_user_name(self, name, role):
        api = self.base_url + "/api/User/UpdateUser"
        body = {
            "ID": select_sqlite_system("select ID from User where Name = '{}'".format(name))[0][0],
            "Name": name,
            "Role": role,
            "Password": "X6hhqpoNCww2ulXnEh9WIHZEtcejv8SBGgABRQHw+2fgq7G7X+RGhKzmICBwRjVDRXXGIumyttnmyAQlJ6ysJkTqWayTCT7QVdtjl+QIi4wFSvfMPiZcd9jNqNj50I0aUnq28MxOsLkIdYIDJx6Agkw7CeJa8Ja83EM6UzujeKI="
        }
        headers = {
            "token": get_token()}
        r = self.s.post(api, json=body, headers=headers)
        return r

