#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from api.baseapi import BaseApi
import json
class Papers(BaseApi):
    def getpapaerlist(self):
        req = {
            "method": "get",
            "url": self.host + "/api/question/GetPapers?pageIndex=1",
            "headers": self.headers
        }
        self.r = self.send_requests(req)
        self.paperId =  self.r.json()["EntityList"][0]["PaperId"]
    def getpapers(self):
        self.getpapaerlist()
        req = {
            "method": "get",
            "url":self.host + f"/api/question/Paper?paperId={self.paperId}&userExamPaperId=0",
            "headers": self.headers
        }
        self.r = self.send_requests(req)
        r1 =  self.r.json()["PaperEntity"]["TKQuestionsBasicEntityList"][0]["QuestionsEntityList"]
        questionList = [];#定义一个空数组
        for q in r1:
            answers = q["QuestionContentKeyValue"]#生成选项列表
            totalCount = len(answers)#试题选项个数
            idx = random.randint(0, totalCount - 1)
            # print(idx)
            # print(totalCount)
            # print(answers[idx]);
            answerKey = answers[idx]["Key"]#随机取某个选项
            item = {"QuestionId": q["QuestionId"], "AnswerDuration": random.randint(0, 100), "Options": answerKey}
            questionList.append(item)
        self.data = {"Answers": questionList, "paperid": self.paperId, "IsCheckinRewards": False, "isSavePaper": 1}
    def savepaper(self):
        self.getpapers()
        req = {
            "method": "post",
            "url":self.host + "/API/report/SaveUserPaperWithQueue?",
            "json":self.data
        }
        self.r = self.send_requests(req)
        self.savepaperqid = self.r.json()["SavePaperQueueId"]
        print(self.r.json())
        print(self.savepaperqid)
    def getuserexampaperid(self):
        self.savepaper()
        req ={
            "method":"get",
            "url":self.host + f"/api/report/GetRealUserExamPaperId?SavePaperQueueId={self.savepaperqid}",
            "headers":self.headers,
        }
        r = self.send_requests(req)
        assert self.r.json()["Msg"] =="成功"
        self.userexampaperid = r.json()["UserExamPaperId"]
        print(self.userexampaperid)
    def getpaperReport(self):
        self.getuserexampaperid()
        req = {
            "method": "get",
            "url": self.host + f"/api/Report/GetPaperReport?UserExamPaperId={self.userexampaperid}",
            "headers": self.headers,
        }
        r = self.send_requests(req)
        print(r.json())
    def analysis(self):
        self.getuserexampaperid()
        req = {
            "method": "get",
            "url":self.host + f"/api/question/Paper?paperId={self.paperId}&userExamPaperId={self.userexampaperid}",
            "headers": self.headers
        }
        self.r = self.send_requests(req)
        print(self.r.json())