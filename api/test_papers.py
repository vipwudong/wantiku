#!/usr/bin/env python
# -*- coding: utf-8 -*-
from test_wanitku.api.baseapi import BaseApi
import random
from jsonpath import jsonpath
class Test_Papers(BaseApi):
    def test_getpapaerlist(self):
        req = {
            "method": "get",
            "url": self.host + "/api/question/GetPapers?pageIndex=1",
            "headers": self.headers
        }
        r = self.send_requests(req)
        assert r.json()["SubjectId"] == 44
        self.paperId = r.json()["EntityList"][0]["PaperId"]
        return (self.paperId)
    def test_getpapers(self):
        self.test_getpapaerlist()
        req = {
            "method": "get",
            "url":self.host + f"/api/question/Paper?paperId={self.paperId}&userExamPaperId=0",
            "headers": self.headers
        }
        r = self.send_requests(req)
        # print(r.json())
        assert r.json()["Msg"] == "成功"
        r1 = r.json()["PaperEntity"]["TKQuestionsBasicEntityList"][0]["QuestionsEntityList"]
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
        self.data = {"Answers": questionList, "paperid": self.paperId, "IsCheckinRewards": "false", "isSavePaper": 1}
        print(self.data)
    def test_savepaper(self):
        self.test_getpapers()
        req = {
            "method": "post",
            "url":self.host + "/API/report/SaveUserPaperWithQueue?",
            "json":self.data
        }
        r = self.send_requests(req)
        self.SavePaperQueueId = r.json()["SavePaperQueueId"]
        print(self.SavePaperQueueId)
    def test_getuserexampaperid(self):
        self.test_savepaper()
        req ={
            "method":"get",
            "url":self.host + f"/api/report/GetRealUserExamPaperId?SavePaperQueueId={self.SavePaperQueueId}",
            "headers":self.headers,
        }
        r = self.send_requests(req)
        assert r.json()["Msg"] =="成功"
        self.userexampaperid = r.json()["UserExamPaperId"]
        print(self.userexampaperid)
        print(r.json())
    def test_analysis(self):
        self.test_getuserexampaperid()
        req = {
            "method": "get",
            "url":self.host + f"/api/question/Paper?paperId={self.paperId}&userExamPaperId={self.userexampaperid}",
            "headers": self.headers
        }
        r = self.send_requests(req)
        print(r.json())