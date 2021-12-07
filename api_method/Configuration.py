# -*- coding: utf-8 -*-
# @Time     : 2021-11-30 9:00
# @Author   : Mr.z
# @Software : PyCharm


import requests
from api_method.AGVS_login import get_token
from common_method.connect_sqlite import select_sqlite_system


class Configuration_module(object):

    def __init__(self, s: requests.Session, base_url):
        self.s = s
        self.base_url = base_url

    def add_agv_configuration(self, is_enable, carrier_index, type_, shape_type, carrier_length, carrier_width, home_station,
                              int_start_vertex, is_home_station, is_start_vertex):
        """
        "IsEnable": AGV是否启动 (启动true)
        "CarrierIndex": AGV编号
        "Type": AGV类型
        "ShapeType": AGV形态
        "CarrierLength": AGV长度
        "CarrierWidth": AGV宽度
        "HomeStation": 待命点编号
        "IntStartVertex": 导航点编号
        "IsHomeStation": true(true 绑定待命点 )
        "IsStartVertex": true(true 绑定上线点为)
        """
        api = self.base_url + "/api/System/AddCarrierTypeInfo"
        body = {
            "IsEnable": is_enable,
            "CarrierIndex": carrier_index,
            "Type": type_,
            "ShapeType": shape_type,
            "CarrierLength": carrier_length,
            "CarrierWidth": carrier_width,
            "HomeStation": home_station,
            "IntStartVertex": int_start_vertex,
            "IsHomeStation": is_home_station,
            "IsStartVertex": is_start_vertex
        }
        headers = {
            "token": get_token()
        }
        r = self.s.post(api, body, headers=headers)
        return r

    def delete_configuration(self, number, started, type_, share_type, long, width, standpoint, stand_point_flag, enable,
                             enable_flag):
        """删除AGV配置接口"""
        api = self.base_url + "/api/System/DeleteCarrierTypeInfo"
        body = {
            "id": select_sqlite_system("select ID from Carrier where CarrierIndex = {}".format(number))[0][0],
            "number": number,
            "started": started,
            "type": type_,
            "shareType": share_type,
            "long": long,
            "width": width,
            "standPoint": standpoint,
            "standPointFlag": stand_point_flag,
            "enable": enable,
            "enableFlag": enable_flag
        }
        headers = {
            "token": get_token()
        }
        r = self.s.post(api, body, headers=headers)
        return r


    def updata_configuration(self, id_, is_enable, carrier_index, type_, shape_type, carrier_length, carrier_width, home_station, int_start_vertex, is_home_station, is_start_vertex):
        api = self.base_url + "/api/System/UpdateCarrierTypeInfo"
        body = {
            "id": select_sqlite_system("select ID from Carrier where CarrierIndex = {}".format(id_))[0][0],
            "IsEnable": is_enable,
            "CarrierIndex": carrier_index,
            "Type": type_,
            "ShapeType": shape_type,
            "CarrierLength": carrier_length,
            "CarrierWidth": carrier_width,
            "HomeStation": home_station,
            "IntStartVertex": int_start_vertex,
            "IsHomeStation": is_home_station,
            "IsStartVertex": is_start_vertex
        }
        headers = {
            "token": get_token()
        }
        r = self.s.post(api, body, headers=headers)
        return r
