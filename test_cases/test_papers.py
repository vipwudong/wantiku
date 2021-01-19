#!/usr/bin/env python
# -*- coding: utf-8 -*-
from api.papers import Papers


class Test_Papers(Papers):
    def test_getpapaerlist(self):
        self.getpapaerlist()
        assert self.r.json()["SubjectId"] == 44
    def test_getpapers(self):
        self.getpapers()
        assert self.r.json()["Msg"] == "成功"
    def test_savepaper(self):
        self.savepaper()
        assert self.savepaperqid > 0
    def test_getuserexampaperid(self):
        self.getuserexampaperid()
        print(self.userexampaperid)
        assert  self.userexampaperid > 0
    def test_getpaperReport(self):
        self.getpaperReport()
        assert self.r.json()["Msg"] =="成功"
    def test_analysis(self):
        self.analysis()
        assert self.r.json()["Msg"] =="成功"