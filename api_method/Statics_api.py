import requests
from api_method.AGVS_login import get_token


class Statics_module(object):

    def __init__(self, s: requests.Session, base_url):
        self.s = s
        self.base_url = base_url

    def statics_find(self, start_time, end_time):
        api = self.base_url + "/api/Statics/GetAllCarrierStaticsInfo?startTime={}&endTime={}".format(start_time, end_time)
        headers = {
            "token": get_token()
        }
        res = self.s.get(api, headers=headers)
        return res
