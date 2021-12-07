import os
import yaml

def get_yaml_data(path):
    if not os.path.isfile(path):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确：s%ds" % path)  # raise后方的代码不会执行
    with open(path, "r", encoding='utf-8') as f:
        y = yaml.safe_load(f)
        return y
