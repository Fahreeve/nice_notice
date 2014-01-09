# -*- coding: UTF-8 -*-
import vk_auth
import json
import urllib2
from urllib import urlencode

class vk:
    def __init__(self, email, password, permissions):
        #("mail@mail.com", "password", "messages,photos")
        self.email = email
        self.password = password
        self.token, self.user_id = vk_auth.auth(email, password, "2951857", permissions)
        
    def call_api(self, method, params):
        if isinstance(params, list):
            params_list = [kv for kv in params]
        elif isinstance(params, dict):
            params_list = params.items()
        else:
            params_list = [params]
        params_list.append(("access_token", self.token))
        print urlencode(params_list)
        url = "https://api.vk.com/method/%s?%s" % (method, urlencode(params_list)) 
        return json.loads(urllib2.urlopen(url).read())["response"]    

    def getDialogs(self, count = 7):
        if count <= 7:
            a = self.call_api("messages.getDialogs", ("count", count))
            return a[0], a[1:] 
        else:
            return
        
    def getHistory(self, typeid, id, count = 20):
        #chat_id or user_id
        a = self.call_api("messages.getHistory", {typeid: id, "count": count})
        return a[0], a[1:]        
        
    def get(self, users_id, fields=[]):
        if type(users_id) == int:
            users_id = [users_id]
        result = self.call_api("users.get", {"uid": ",".join(map(str, users_id)), "fields": ",".join(fields)})
        return result
        