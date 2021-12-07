# -*- coding: utf-8 -*-
# @Time     : 2021-11-30 9:00
# @Author   : Mr.z
# @Software : PyCharm


import requests
from api_method.AGVS_login import get_token
from common_method.connect_sqlite import select_sqlite_system


class Move_agv(object):
    """监控页面移动AGV"""

    def __init__(self, s: requests.Session, base_url):
        self.s = s
        self.base_url = base_url

    def move_agvs_navigation(self, carrier_index, vertex):
        api = self.base_url + "/api/CarrierGroup/MoveToVertex"
        body = {
            "carrierIndex": carrier_index,
            "vertex": vertex,
        }
        headers = {"token": get_token()}
        res = self.s.post(api, json=body, headers=headers)
        return res

    def move_agvs_site(self, carrier_index, station, action):
        api = self.base_url + "/api/CarrierGroup/MoveToStation"
        body = {
            "carrierIndex": carrier_index,
            "station": station,
            "action": action
        }
        headers = {"token": get_token()}
        res = self.s.post(api, json=body, headers=headers)
        return res

    def carrier_list_resume(self, data=None):
        api = self.base_url + "/api/CarrierGroup/CarrierListResume"
        headers = {"token": get_token()}
        res = self.s.post(api, data, headers=headers)
        return res

    def carrier_list_pause(self, data=None):
        api = self.base_url + "/api/CarrierGroup/CarrierListPause"
        headers = {"token": get_token()}
        res = self.s.post(api, data, headers=headers)
        return res

    def update_carrier_info(self, carrier_index, shape_type, is_home_station, is_start_vertxe):
        api = self.base_url + "/api/System/UpdateCarrierTypeInfo"
        data = select_sqlite_system("select IsEnable from Carrier where CarrierIndex = {}".format(carrier_index))[0][0]
        is_enable = ""
        if data == 1:
            is_enable = "true"
        elif data == 0:
            is_enable = "flase"
        else:
            print("data查询为空")
        body = {
            "CarrierIndex": carrier_index,
            "ShapeType": shape_type,
            "ID": select_sqlite_system("select ID from Carrier where CarrierIndex = {}".format(carrier_index))[0][0],
            "IsEnable": is_enable,
            "Type": select_sqlite_system("select Type from Carrier where CarrierIndex = {}".format(carrier_index))[0][0],
            "CarrierLength": select_sqlite_system("select CarrierLength from Carrier where CarrierIndex = {}".format(carrier_index))[0][0],
            "CarrierWidth": select_sqlite_system("select CarrierWidth from Carrier where CarrierIndex = {}".format(carrier_index))[0][0],
            "HomeStation": select_sqlite_system("select HomeStation from Carrier where CarrierIndex = {}".format(carrier_index))[0][0],
            "IntStartVertex": select_sqlite_system("select IntStartVertex from Carrier where CarrierIndex = {}".format(carrier_index))[0][0],
            "IsHomeStation": is_home_station,
            "IsStartVertex": is_start_vertxe
        }
        headers = {
            "token": get_token()
        }
        r = self.s.post(api,json=body,headers=headers)
        return r

    def look_status(self):
        api = self.base_url + "/api/Agv/GetPmsVersion"
        res = self.s.get(api)
        return res

    def alarm_find(self, start_time, end_time, level):
        api = self.base_url + "/api/Statics/GetAllHistoryAlarmListByIndex?startTime={}&endTime={}&level={} ".format(start_time, end_time, level)
        headers = {"token": get_token()}
        res = self.s.get(api, headers=headers)
        return res
