#!/usr/bin/env python
# -*- coding: utf-8 -*-
from api.papers import Papers
import time
class Test_Papers(Papers):
    def test_getpapaerlist(self):
        self.getpapaerlist()
        assert self.r.json()["SubjectId"] == 44
    def test_getpapers(self):
        paperId = self.getpapaerlist()
        self.getpapers(paperId)
        assert self.r.json()["Msg"] == "成功"
        print(self.r.json())
    def test_savepaper(self):
        paperId = self.getpapaerlist()
        paper = self.getpapers(paperId)
        savepaperqid = self.savepaper(paper)
        assert savepaperqid > 0
    def test_getuserexampaperid(self):

        paperId = self.getpapaerlist()
        paper = self.getpapers(paperId)
        savepaperqid = self.savepaper(paper)
        print("result savepaperqid= ",savepaperqid)
        time.sleep(3)
        realuserexampaperid = self.getuserexampaperid(savepaperqid)
        print(realuserexampaperid)
        # assert  self.userexampaperid > 0
    def test_getpaperReport(self):
        paperId = self.getpapaerlist()
        paper = self.getpapers(paperId)
        savepaperqid = self.savepaper(paper)
        realuserexampaperid = self.getuserexampaperid(savepaperqid)
        self.getpaperReport(realuserexampaperid)
        assert self.r.json()["Msg"] =="成功"
    def test_analysis(self):
        paperId = self.getpapaerlist()
        paper = self.getpapers(paperId)
        savepaperqid = self.savepaper(paper)
        time.sleep(2)
        realuserexampaperid = self.getuserexampaperid(savepaperqid)
        self.analysis(paperId,realuserexampaperid)
        assert self.r.json()["Msg"] =="成功"

    def test_analysis2(self):
        self.analysis(372961934, 341305622)
        print(self.r.json()["UserExamPaperEntity"])
        assert self.r.json()["Msg"] == "成功"