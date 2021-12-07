import os
from common_method.read_yaml import get_yaml_data


def get_test_data():
    """获取测试数据"""
    curr_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    yaml_path = os.path.join(curr_path, "test_data", "task.yaml")
    test_data = get_yaml_data(yaml_path)
    return test_data

if __name__ == '__main__':
    print(get_test_data()["data14"])