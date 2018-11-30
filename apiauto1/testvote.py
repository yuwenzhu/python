import xlrd
from apiauto1.TestRequest import *
from apiauto1.testdata.getpath import *

testdata=xlrd.open_workbook(GetTestDataPath())

testurl='http://127.0.0.1:8000'
testurl1='http://api.apiopen.top'
testurl2='https://api.apiopen.top'
def test_post_vote():
    try:
        table=testdata.sheets()[1]
        for i in range(3,5):
            choice= table.cell(i, 0).value
            status=table.cell(i,1).value
            qiwang=table.cell(i,2).value
            hdata={
                'choice':int(choice)
            }
            header={
                'content-type': "application/x-www-form-urlencoded"
            }
            testcaseid='1-1'
            testname='投票接口'+testcaseid
            testhope=str(int(status))
            fanhuitesthope=qiwang
            r=TestPostRequest(testurl+'/polls/1/vote/',hdata,header,testcaseid,testname,testhope,fanhuitesthope)
            # print (r)
    except Exception as e:
        print(e)

def get_polls():
    try:
        table=testdata.sheets()[1]
        for i in range(13,14):
            status= table.cell(i, 0).value
            hdata=''
            header={
                'content-type': "application/x-www-form-urlencoded"
            }
            testcaseid='1-2'
            testname='获取选项接口'+testcaseid
            testhope=str(int(status))
            fanhuitesthope='success'
            r=TestGetRequest(testurl+'/polls/1/',hdata,header,testcaseid,testname,testhope,fanhuitesthope)
    except Exception as e:
        print(e)

def get_question():
    try:
        hdata=''
        header={
            'content-type': "application/x-www-form-urlencoded"
        }
        testcaseid='1-3'
        testname='获取问题接口'+testcaseid
        testhope='200'
        fanhuitesthope='success'
        r=TestGetRequest(testurl+'/polls/',hdata,header,testcaseid,testname,testhope,fanhuitesthope)
        # print(r)
    except Exception as e:
        print(e)

def post_login():
    try:
        table=testdata.sheets()[3]
        for i in range(3,5):
            username= table.cell(i, 0).value
            password=table.cell(i,1).value
            status=table.cell(i,2).value
            qiwang=table.cell(i,3).value
            hdata={
                'username':str(int(username)),
                'password':str(int(password))
            }
            header={
                'content-type': "application/x-www-form-urlencoded"
            }
            testcaseid='1-1'
            testname='登录接口 '+testcaseid
            testhope=str(int(status))
            fanhuitesthope=qiwang
            r=TestPostRequest(testurl+'/polls/login/',hdata,header,testcaseid,testname,testhope,fanhuitesthope)
            # print (r)
    except Exception as e:
        print(e)

def zuoye_1():
    try:
        table=testdata.sheets()[4]
        for i in range(2,3):
            name= table.cell(i, 0).value
            status=table.cell(i,1).value
            qiwang=table.cell(i,2).value
            hdata={
                'name':name
            }
            header={
                'content-type': "application/x-www-form-urlencoded"
            }
            testcaseid='1-2'
            testname='搜索古诗词作者 '+testcaseid
            testhope=str(int(status))
            fanhuitesthope=qiwang
            r=TestGetRequest1(testurl1+'/likePoetry/',hdata,header,testcaseid,testname,testhope,fanhuitesthope)
            # print (r)
    except Exception as e:
        print(e)

def zuoye_2():
    try:
        table=testdata.sheets()[5]
        for i in range(1,2):
            status= table.cell(i, 0).value
            qiwang=table.cell(i,1).value
            hdata=''
            header={
                'content-type': "application/x-www-form-urlencoded"
            }
            testcaseid='1-3'
            testname='音乐排行榜 '+testcaseid
            testhope=str(int(status))
            fanhuitesthope=qiwang
            r=TestGetRequest1(testurl1+'/musicRankings/',hdata,header,testcaseid,testname,testhope,fanhuitesthope)
    except Exception as e:
        print(e)

def zuoye_3():
    try:
        table=testdata.sheets()[6]
        for i in range(1,2):
            status= table.cell(i, 0).value
            qiwang=table.cell(i,1).value
            hdata=''
            header={
                'content-type': "application/x-www-form-urlencoded"
            }
            testcaseid='1-4'
            testname='随机单句诗词 '+testcaseid
            testhope=str(int(status))
            fanhuitesthope=qiwang
            r=TestGetRequest1(testurl1+'/singlePoetry/',hdata,header,testcaseid,testname,testhope,fanhuitesthope)
    except Exception as e:
        print(e)

def zuoye_4():
    '''
    https的有问题，不会解决
    :return:
    '''
    try:
        table=testdata.sheets()[7]
        for i in range(2,3):
            name= table.cell(i, 0).value
            status=table.cell(i,1).value
            qiwang=table.cell(i,2).value
            hdata={
                'city':name
            }
            header={
                'content-type': "application/x-www-form-urlencoded",
                'Connection': 'close'
            }
            testcaseid='1-3'
            testname='天气获取接口 '+testcaseid
            testhope=str(int(status))
            fanhuitesthope=qiwang
            r=TestPostRequest1(testurl2+'/weatherApi/',hdata,header,testcaseid,testname,testhope,fanhuitesthope)
            # print (r)
    except Exception as e:
        print(e)

# test_post_vote()
# get_polls()
# get_question()
# post_login()
# zuoye_1()
# zuoye_2()
# zuoye_3()
# zuoye_4()