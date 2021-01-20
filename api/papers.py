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
        self.paperId =self.r.json()["EntityList"][0]["PaperId"]
        return self.paperId
    def getpapers(self,paperId):
        req = {
            "method": "get",
            "url":self.host + f"/api/question/Paper?paperId={paperId}&userExamPaperId=0",
            "headers": self.headers
        }
        r = self.send_requests(req)
        return r.json()

    def savepaper(self, paper):
        paperId = paper["PaperEntity"]["PaperId"]
        r1 = paper["PaperEntity"]["TKQuestionsBasicEntityList"][0]["QuestionsEntityList"]
        questionList = [];  # 定义一个空数组
        for q in r1:
            answers = q["QuestionContentKeyValue"]  # 生成选项列表
            totalCount = len(answers)  # 试题选项个数
            idx = random.randint(0, totalCount - 1)
            # print(idx)
            # print(totalCount)
            # print(answers[idx]);
            answerKey = answers[idx]["Key"]  # 随机取某个选项
            item = {"QuestionId": q["QuestionId"], "AnswerDuration": random.randint(0, 100), "Options": answerKey}
            questionList.append(item)
        data = {"Answers": questionList, "paperid": paperId, "IsCheckinRewards": False, "isSavePaper": 1}
        req = {
            "method": "post",
            "url":self.host + "/API/report/SaveUserPaperWithQueue?",
            "json":data,
            "headers":self.headers

        }
        r = self.send_requests(req)
        self.savepaperqid = r.json()["SavePaperQueueId"]
        return self.savepaperqid
    def getuserexampaperid(self,savepaperqid):
        savepaperqid = self.savepaperqid
        req ={
            "method":"get",
            "url":self.host + f"/api/report/GetRealUserExamPaperId?SavePaperQueueId={savepaperqid}",
            "headers":self.headers,
        }
        r = self.send_requests(req)
        assert r.json()["Msg"] =="成功"
        print(r.json())
        self.realuserexampaperid = r.json()["UserExamPaperId"]
        return self.realuserexampaperid
    def getpaperReport(self,realuserexampaperid):
        req = {
            "method": "get",
            "url": self.host + f"/api/Report/GetPaperReport?UserExamPaperId={realuserexampaperid}",
            "headers": self.headers,
        }
        r = self.send_requests(req)
        print(r.json())
    def analysis(self,paperId,realuserexampaperid):
        req = {
            "method": "get",
            "url":self.host + f"/api/question/Paper?paperId={paperId}&userExamPaperId={realuserexampaperid}",
            "headers": self.headers
        }
        self.r = self.send_requests(req)
        print(self.r.json())
        print(req)
