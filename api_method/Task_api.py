from api_method.AGVS_login import get_token
import requests
from common_method.connect_sqlite import select_sqlite_pms_v4

class Task_configuration(object):
    """任务配置"""
    def __init__(self, s: requests.Session, base_url):
        self.s = s
        self.base_url = base_url

    def location_settings(self, ware_house_id, ware_house_name, station_id, group_id=None, relation_station_id_1=0, relation_station_id_2=0, relation_station_id_3=0):
        """新增库位接口"""
        api = self.base_url + "/api/Agv/AddWarehouse"
        body = {
            "WareHouseID": ware_house_id,
            "WarehouseName": ware_house_name,
            "GroupId": group_id,
            "RelationStationID1": relation_station_id_1,
            "RelationStationID2": relation_station_id_2,
            "RelationStationID3": relation_station_id_3,
            "StationID": station_id
        }
        r = self.s.post(api, json=body)
        return r

    """删除库位"""
    def delete_location(self, data):
        api = self.base_url + "/api/Agv/DeleteWarehouse"
        body = data
        header = {
            "token": get_token(),
            "Content-Type": "application/json"
        }
        r = self.s.post(api, json=body, headers=header)
        return r

    """修改库位"""
    def updata_location(self, ware_house_id, ware_house_name, station_id, group_id=None, relation_station_id_1=0, relation_station_id_2=0, relation_station_id_3=0):
        api = self.base_url + "/api/Agv/UpdateWarehouse"
        body = {
            "WareHouseID": ware_house_id,
            "WarehouseName": ware_house_name,
            "GroupId": group_id,
            "RelationStationID1": relation_station_id_1,
            "RelationStationID2": relation_station_id_2,
            "RelationStationID3": relation_station_id_3,
            "StationID": station_id
        }
        r = self.s.post(api, json=body)
        return r

    """添加库位组"""
    def add_warehouse_group(self, warehouse_type, remark, operation_name, param1, param2, param3):
        api1 = self.base_url + "/api/Agv/AddWarehouseGroup"
        api2 = self.base_url + "/api/Agv/AppendWarehouseGroupList"
        body1 = {
            "WarehouseType": warehouse_type,
            "Remark": remark
        }
        res = self.s.post(api1, body1)
        group_id = res.json().get("data").get("GroupId")
        body2 = [{
            "GroupId": group_id,
            "Remark": remark,
            "OperationName": operation_name,
            "Param1": param1,
            "Param2": param2,
            "Param3": param3,
            "WarehouseType": warehouse_type
        }]
        r = self.s.post(api2, json=body2)
        return r

    def execution_template(self, book_name, count, car_nums, agv_id):
        """
        任务模板执行接口
        bookName: 执行的任务名称
        count: 执行次数
        carNums: 未知
        agvId: 车辆编号
        """
        api = self.base_url + "/api/Agv/AGVExecuteBookTask"
        body = {
            "bookname": book_name,
            "count": count,
            "carNums": car_nums,
            "agvId": agv_id
        }
        headers = {"token": get_token()}
        r = self.s.post(api, json=body, headers=headers)
        return r

    def revise_template(self):
        """修改模板"""
        pass

    def update_group_by_id(self, group_id, warehouse_type, remark):
        """修改库位组名称
        "GroupId": "bdf20993-0c5b-46ee-acbb-c1347b40ae28",
        "WarehouseType": "5",
        "Remark": "5"
        """
        api = self.base_url + "/api/Agv/UpdateWarehouseGroupByGroupId"
        body = {
            "GroupId": group_id,
            "WarehouseType": warehouse_type,
            "Remark": remark
        }
        r = self.s.post(api, json=body)
        return r

    def delete_group_by_id(self, group_id):
        api = self.base_url + "/api/Agv/DeleteWarehouseGroupByType?GroupId={}".format(group_id)
        r = self.s.post(api)
        return r

    def find_task(self, task_id):
        api = self.base_url + "/api/Agv/GetHistoryTaskData?TaskID= s%ds" % task_id
        r = self.s.get(api)
        return r

    def add_operate(self, name, code, is_agv_behavior, remark, is_edit, is_delete):
        api = self.base_url + "/api/Agv/AddOperate"
        body = {
            "Name": name,
            "Code": code,
            "isAgvBehavior": is_agv_behavior,
            "Remark": remark,
            "isEdit": is_edit,
            "isDelete": is_delete
        }
        r = self.s.post(api, json=body)
        return r

    def delete_operate(self, name):
        api = self.base_url + "/api/Agv/DeleteOperate"
        body = select_sqlite_pms_v4("select ID from OperateInfo where Name = {}" .format(name))[0][0]
        headers = {
            "token": get_token(),
            "Content-Type": "application/json"
        }
        r = self.s.post(api, json=body, headers=headers)
        return r

    def updata_operate(self, name, code, is_agv_behavior, remark, is_edit, is_delete):
        api = self.base_url + "/api/Agv/UpdateOperate"
        body = {
            "ID": "SELECT ID FROM OperateInfo WHERE Name = '{}'".format(name)[0][0],
            "Name": name,
            "Code": code,
            "isAgvBehavior": is_agv_behavior,
            "Remark": remark,
            "isEdit": is_edit,
            "isDelete": is_delete
        }
        headers = {
            "token": get_token(),
            "Content-Type": "application/json"
        }
        r = self.s.post(api,json=body,headers=headers)
        return r

    def add_task_book(self, name, describe, remark, task_group=""):
        api = self.base_url + "/api/Agv/AddTaskBook"
        body = {
            "Name": name,
            "Describe": describe,
            "Remark": remark,
            "Taskgroup": task_group
        }
        headers = {
            "token": get_token()
        }
        r = requests.post(api, json=body, headers=headers)
        return r

    def add_task(self, task_id, template_name, agv_id, parameters):
        api = self.base_url + "/api/agv/TaskAdd"
        body = {
        "TaskID" : task_id,
        "TemplateName" : template_name,
        "Parameters" : r"{}".format(parameters),
        "AgvID" : agv_id
        }
        headers = {"token": get_token()}
        r = self.s.post(api, json=body, headers=headers)
        return r

    def change_agv(self, agv_id):
        """必须存在任务或者先通过模板接口先执行任务"""
        api = self.base_url + "/api/agv/TaskChangeAssignAGV"
        url = "http://localhost:9528/api/Agv/GetTaskDataList"
        r = requests.get(url)
        s1 = r.json().get("data")
        body = {
            "TaskID": s1[-1].get("TaskID"),    #保险取值直接拿最后一条数据取值ID"
            "AgvID": agv_id
        }
        r = self.s.post(api, json=body)
        return r

    def get_test_book(self):
        api = self.base_url + "/api/agv/GetTaskBookList"
        r = self.s.get(api)
        return   r

    def def_test_changge_rely(self, task_id, parent_task_id):
        api = self.base_url + "/api/agv/TaskChangeRely"
        body = {
            "TaskID": task_id,
            "ParentTaskID": parent_task_id
        }
        r = self.s.post(api, json=body)
        return r


# if __name__ == '__main__':
#     s = requests.session()
#     base_url = "http://localhost:9528"
