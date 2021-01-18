#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

class BaseApi:
    headers = {
        "UserClientType": "102",
        "FakesubjectParentId": "0",
        "SubjectId": "44",
        "OpenId": "ouoD50BJyntZYO_P4nKD7zpK7pjA",
        "SubjectMergerId": "538",
        "SubjectParentId": "7",
        "PackageId": "1",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 wechatdevtools/1.04.2006192 MicroMessenger/7.0.4 Language/zh_CN webview/",
        "SubjectLevel": "0",
        "VersionReview": "180",
        "VersionNumber": "3630",
        "UserId": "6648816",
        "Token": "20210115135342-ec41f8dc0cd97c2822534678894671f4"
    }
    host = "https://weixin.566.com"
    def send_requests(self, req:dict):#对requests进行二次封装
        """
        req = {
        "method" : "get" or "post"
        "url" : "xxxxxx"
        "headers": ""
        "params" : "xxxxx"

        }
        :param req:
        :return:
        """
        return  requests.request(**req)

