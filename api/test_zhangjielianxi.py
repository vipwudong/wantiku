#!/usr/bin/env python
# -*- coding: utf-8 -*-
from jsonpath import jsonpath

import random
from test_wanitku.api.baseapi import BaseApi

class TestZhangjielianxi(BaseApi):
    def test_GetSpecialIntelligenceTree(self):
        req = {
            "method": "get",
            "url": self.host + "/api/question/GetSpecialIntelligenceTree?",
            "headers": {"SubjectId": "436",
                        "UserId": "6648816",
                        "SubjectParentId": "435",
                        "PackageId": "1",
                        "Token": "20210115135342-ec41f8dc0cd97c2822534678894671f4"
                        }
        }
        r = self.send_requests(req)
        print(r.json())
        self.ExamSiteId = r.json()["SiteQuestionUserList"][0]["ExamSiteId"]
        print(self.ExamSiteId)
    def test_SpecialExercisePaper(self):
        self.test_GetSpecialIntelligenceTree()
        req = {
            "method": "get",
            "url": self.host + f"//api/question/SpecialExercisePaper?examSiteId={self.ExamSiteId}",
            "headers": {"SubjectId": "436",
                        "UserId": "6648816",
                        "SubjectParentId": "435",
                        "PackageId": "1",
                        "Token": "20210115135342-ec41f8dc0cd97c2822534678894671f4"
                        }
        }
        r = self.send_requests(req)
        self.paperid = r.json()["PaperEntity"]["PaperId"]
        r1 = r.json()["PaperEntity"]["TKQuestionsBasicEntityList"][0]["QuestionsEntityList"]
        questionList = [];
        for q in r1:
            answers = q["QuestionContentKeyValue"]
            totalCount =  len(answers)
            idx = random.randint(0, totalCount-1);
            # print(idx)
            # print(totalCount)
            # print(answers[idx]);
            answerKey =answers[idx]["Key"]
            item = {"QuestionId": q["QuestionId"], "AnswerDuration": random.randint(0, 10000), "Options": answerKey}
            questionList.append(item)

        self.data = {"Answers": questionList, "paperid":self.paperid,"IsCheckinRewards":"false","isSavePaper":1}
        print(self.data)
    def test_SaveUserPaperWithQueue(self):
         self.test_SpecialExercisePaper()
         req = {
             "method": "post",
             "url": self.host + "/API/report/SaveUserPaperWithQueue",
             "json": self.data
         }
         r = self.send_requests(req)
         print(r.json())
         self.SavePaperQueueId = r.json()["SavePaperQueueId"]
         print(self.SavePaperQueueId)
         #