import json
import requests
import urllib3
urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()
from apiauto1.log import logger
#添加一个数组，用来装测试结果
hlist=[]
#公共的头文件设置
header={
    'content-type': "application/json;charset=UTF-8"
    }

def TestPostRequest(hurl,hdata,headers,htestcaseid,htestcasename,htesthope,fanhuitesthope):
    hr=requests.post(hurl,data=hdata,headers=headers)
    hresult=json.loads(hr.text)
    hstatus=hresult['status']
    if hstatus==htesthope and fanhuitesthope in str(hresult):
        hhhdata={'t_id':htestcaseid,
                 't_name':htestcasename,
                 't_method':'POST',
                 't_url':hurl,
                 't_param':'测试数据：'+str(hdata),
                 't_hope':'status:'+htesthope+',期望结果:'+fanhuitesthope,
                 't_actual': 'status:' + hstatus + ',实际返回结果:' + str(hresult),
                 't_result':'通过'
                 }
        hlist.append(hhhdata)
        logger.info(htestcasename)
        logger.info("通过")
    else:
        hhhdata = {'t_id': htestcaseid,
                    't_name': htestcasename,
                    't_method': 'POST',
                    't_url': hurl,
                    't_param': '测试数据：' + str(hdata),
                    't_hope': 'status:' + htesthope + ',期望结果:' + fanhuitesthope,
                    't_actual': 'status:' + hstatus + ',实际返回结果:' + str(hresult),
                    't_result': '失败'
                    }
        hlist.append(hhhdata)
        logger.error(htestcasename)
        logger.error("失败")
    # print(hlist)

def TestGetRequest(hurl,hdata,headers,htestcaseid,htestcasename,htesthope,fanhuitesthope):
    if hdata=='':
        hr=requests.get(hurl,headers=headers)
    else:
        hr=requests.get(hurl,params=hdata,headers=headers)
    hresult=json.loads(hr.text)
    hstatus=hresult['status']
    if hstatus==htesthope and fanhuitesthope in str(hresult):
        hhhdata={'t_id':htestcaseid,
                 't_name':htestcasename,
                 't_method':'POST',
                 't_url':hurl,
                 't_param':'测试数据：'+str(hdata),
                 't_hope':'status:'+htesthope+'期望结果:'+fanhuitesthope,
                 't_actual': 'status:' + hstatus + '实际返回结果:' + str(hresult),
                 't_result':'通过'
                 }
        hlist.append(hhhdata)
        logger.info(htestcasename)
        logger.info("通过")
    else:
        hhhdata = {'t_id': htestcaseid,
                    't_name': htestcasename,
                    't_method': 'POST',
                    't_url': hurl,
                    't_param': '测试数据：' + str(hdata),
                    't_hope': 'status:' + htesthope + '期望结果:' + fanhuitesthope,
                    't_actual': 'status:' + hstatus + '实际返回结果:' + str(hresult),
                    't_result': '失败'
                    }
        hlist.append(hhhdata)
        logger.info(htestcasename)
        logger.info("失败")
    # print(hlist)

def TestPostRequest1(hurl,hdata,headers,htestcaseid,htestcasename,htesthope,fanhuitesthope):
    hr=requests.post(hurl,data=hdata,headers=headers)
    hresult=json.loads(hr.text)
    hstatus=str(hresult['code'])
    if hstatus==htesthope and fanhuitesthope in str(hresult):
        hhhdata={'t_id':htestcaseid,
                 't_name':htestcasename,
                 't_method':'POST',
                 't_url':hurl,
                 't_param':'测试数据：'+str(hdata),
                 't_hope':'code:'+htesthope+',期望结果:'+fanhuitesthope,
                 't_actual': 'code:' + hstatus + ',实际返回结果:' + str(hresult),
                 't_result':'通过'
                 }
        hlist.append(hhhdata)
        logger.info(htestcasename)
        logger.info("通过")
    else:
        hhhdata = {'t_id': htestcaseid,
                    't_name': htestcasename,
                    't_method': 'POST',
                    't_url': hurl,
                    't_param': '测试数据：' + str(hdata),
                    't_hope': 'code:' + htesthope + ',期望结果:' + fanhuitesthope,
                    't_actual': 'code:' + hstatus + ',实际返回结果:' + str(hresult),
                    't_result': '失败'
                    }
        hlist.append(hhhdata)
        logger.info(htestcasename)
        logger.info("失败")
    # print(hlist)

def TestGetRequest1(hurl,hdata,headers,htestcaseid,htestcasename,htesthope,fanhuitesthope):
    if hdata=='':
        hr=requests.get(hurl,headers=headers)
    else:
        hr=requests.get(hurl,params=hdata,headers=headers)
    hresult=json.loads(hr.text)
    hstatus=str(hresult['code'])
    if hstatus==htesthope and fanhuitesthope in str(hresult):
        hhhdata={'t_id':htestcaseid,
                 't_name':htestcasename,
                 't_method':'POST',
                 't_url':hurl,
                 't_param':'测试数据：'+str(hdata),
                 't_hope':'code:'+htesthope+',期望结果:'+fanhuitesthope,
                 't_actual': 'code:' + hstatus + ',实际返回结果:' + str(hresult),
                 't_result':'通过'
                 }
        hlist.append(hhhdata)
        logger.info(htestcasename)
        logger.info("通过")
    else:
        hhhdata = {'t_id': htestcaseid,
                    't_name': htestcasename,
                    't_method': 'POST',
                    't_url': hurl,
                    't_param': '测试数据：' + str(hdata),
                    't_hope': 'code:' + htesthope + ',期望结果:' + fanhuitesthope,
                    't_actual': 'code:' + hstatus + ',实际返回结果:' + str(hresult),
                    't_result': '失败'
                    }
        hlist.append(hhhdata)
        logger.info(htestcasename)
        logger.info("失败")
    # print(hlist)