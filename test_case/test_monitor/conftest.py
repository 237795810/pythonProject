# -*- coding: utf-8 -*-
# @Time     : 2021-11-30 9:00
# @Author   : Mr.z
# @Software : PyCharm


import os
from common_method.read_yaml import get_yaml_data


def get_test_data():
    """获取测试数据"""
    curr_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    """获取绝对路径"""
    yaml_path = os.path.join(curr_path, "test_data", "monitor.yaml")
    """获取文件路径"""
    test_data = get_yaml_data(yaml_path)
    """读取文件"""
    return test_data

