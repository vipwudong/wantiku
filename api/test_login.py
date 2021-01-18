#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

from test_wanitku.api.baseapi import BaseApi


class TestLogin(BaseApi):
    def test_data(self):
        req = {
            "method": "get",
            "url": self.host + "/api/login/EncryptMobile?",
            "params": {"mobile": "18600215696"},
            "headers": self.headers
        }
        r = self.send_requests(req)
        self.data = r.json()["Data"]
    def test_login(self):
        self.test_data()
        req = {
            "method": "post",
            "url": self.host + "/api/login/MobileLogin?",
            "data": self.data,
            "headers": self.headers}
        r = self.send_requests(req)
        assert r.json()["NickName"] == "刘全有"
        print(r.json())
