import requests

url = "http://localhost:9528/api/agv/TaskChangeAssignAGV"
body = {
    "TaskID": 12071528492442,
    "AgvID": 1
}

r = requests.post(url, json=body)
print(r.json())

# url = "http://localhost:9528/api/Agv/GetTaskDataList"
# r = requests.get(url)
# s = r.json().get("data")
# print(s[-1].get("TaskID"))
