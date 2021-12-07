# -*- coding: utf-8 -*-
# @Time     : 2021-11-30 9:00
# @Author   : Mr.z
# @Software : PyCharm

import requests
import allure


class Login_manager(object):
    def __init__(self, s: requests.Session, base_url):
        self.s = s
        self.Base_url = base_url

    @allure.step("登录web")
    def login_cloud(self, user, paw):
        api = self.Base_url + "/api/Auth/Login"
        body = {
            "User": user,
            "Password": paw
        }
        res = requests.post(api, json=body)
        token = res.json()['data']['token']
        h = {
            "token": token}
        self.s.headers.update(h)
        return self.s, res


def get_token(user="casun",
              paw="rZgTTt8DESKpqMds/ghEZeigs8TBNS4MgLiSzTch5gEhs/qFbzUh+WJL05Ti5IG6vz3EO55eCqCAiy2oprn840R/B40aXWxfic/Q/gOsJiqNcqPO37r0/6u1pr1d0BMuWm63VGzJUVrtoiLW/j5M7uS8sY2imBnTZLvR+kPkzGU="):
    """从登陆的类中继续方法，返回token"""
    se = requests.Session()
    log = Login_manager(se, "http://localhost:9528")
    re = log.login_cloud(user, paw)
    return re[1].json().get("data").get("token")
