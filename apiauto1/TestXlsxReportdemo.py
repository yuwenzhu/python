# -*- coding:utf-8 -*-
import xlsxwriter
import time
import apiauto1.TestRequest
from apiauto1.testvote import *
#把GetTestReport方法自己写出来
# from apiauto.day9.TestAllRunner import *
from apiauto1.testdata.getpath import GetTestReport
from apiauto.day10.initdata import init_data
from apiauto1.sendmail import MyMail
from apiauto1.log import logger
from apiauto1.testdata.getpath import GetTestConfig
# from apiauto.day7.TestAllCase import *

# init_data()
# test_post_vote()
# get_polls()
# get_question()
# post_login()
zuoye_1()
zuoye_2()
zuoye_3()
# zuoye_4()
# tianqi_4()
# threads()
# demo2()
# demo1()

TestReport = apiauto1.TestRequest.hlist  # 调用测试结果

hpassnum = 0  # 定义一个变量，用来计算测试通过的用例数量


def get_format(wd, option={}):
    return wd.add_format(option)

# 设置居中
def get_format_center(wd, num=1):
    return wd.add_format({'align': 'center', 'valign': 'vcenter', 'border': num})

#设置边框
def set_border_(wd, num=1):
    return wd.add_format({}).set_border(num)

# 写数据
def _write_center(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd))

now=time.strftime("%Y-%m-%d-%H-%M-%S-",time.localtime(time.time()))
timenow=time.strftime("%Y/%m/%d %H:%M",time.localtime(time.time()))
ReportPath=GetTestReport()
workbook=xlsxwriter.Workbook(ReportPath)    #生成的报告路径
worksheet=workbook.add_worksheet("测试总结")
worksheet2=workbook.add_worksheet("用例详情")

def init(worksheet):
    # 设置列行的宽高
    worksheet.set_column("A:A", 15)
    worksheet.set_column("B:B", 20)
    worksheet.set_column("C:C", 20)
    worksheet.set_column("D:D", 20)
    worksheet.set_column("E:E", 20)
    worksheet.set_column("F:F", 20)

    worksheet.set_row(1, 30)
    worksheet.set_row(2, 30)
    worksheet.set_row(3, 30)
    worksheet.set_row(4, 30)
    worksheet.set_row(5, 30)
    # worksheet.set_row(0, 200)

    #用在接口自动化单元格
    define_format_H1 = get_format(workbook, {'bold': True, 'font_size': 18})
    define_format_H2 = get_format(workbook, {'bold': True, 'font_size': 14})
    define_format_H1.set_border(1)

    define_format_H2.set_border(1)
    define_format_H1.set_align("center")
    define_format_H2.set_align("center")
    define_format_H2.set_bg_color("blue")
    define_format_H2.set_color("#ffffff")
    # Create a new Chart object.

    worksheet.merge_range('A1:F1', '接口自动化测试报告', define_format_H1)
    worksheet.merge_range('A2:F2', '测试概括', define_format_H2)
    worksheet.merge_range('A3:A6', '炼数成金', get_format_center(workbook))
    # worksheet.insert_image('A1', GetLogoDataPath())

    _write_center(worksheet, "B3", '项目名称', workbook)
    _write_center(worksheet, "B4", '接口版本', workbook)
    _write_center(worksheet, "B5", '脚本语言', workbook)
    _write_center(worksheet, "B6", '测试地址', workbook)

    data = {"test_name": "炼数成金项目接口", "test_version": "v1.0.0",
            "test_pl": "Python3", "test_net": testurl}
    _write_center(worksheet, "C3", data['test_name'], workbook)
    _write_center(worksheet, "C4", data['test_version'], workbook)
    _write_center(worksheet, "C5", data['test_pl'], workbook)
    _write_center(worksheet, "C6", data['test_net'], workbook)

    _write_center(worksheet, "D3", "测试用例总数", workbook)
    _write_center(worksheet, "D4", "测试用例通过数", workbook)
    _write_center(worksheet, "D5", "测试用例失败数", workbook)
    _write_center(worksheet, "D6", "测试日期", workbook)

    data1 = {"test_sum": len(TestReport),
             "test_success": hpassnum,
             "test_failed": len(TestReport) - hpassnum,
             "test_date": timenow}
    _write_center(worksheet, "E3", data1['test_sum'], workbook)
    _write_center(worksheet, "E4", data1['test_success'], workbook)
    _write_center(worksheet, "E5", data1['test_failed'], workbook)
    _write_center(worksheet, "E6", data1['test_date'], workbook)

    _write_center(worksheet, "F3", "测试用例通过率", workbook)

    worksheet.merge_range('F4:F6', str(
        (round(hpassnum / len(TestReport), 4)) * 100) + '%', get_format_center(workbook))

    pie(workbook, worksheet)

#设置用例详情的格式
def test_detail(worksheet):
    # 设置列宽高
    worksheet.set_column("A:A", 15)
    worksheet.set_column("B:B", 20)
    worksheet.set_column("C:C", 20)
    worksheet.set_column("D:D", 20)
    worksheet.set_column("E:E", 20)
    worksheet.set_column("F:F", 20)
    worksheet.set_column("G:G", 20)
    worksheet.set_column("H:H", 20)

    # 设置行的宽高
    for hrow in range(len(TestReport) + 2):
        worksheet.set_row(hrow, 20)

    worksheet.merge_range('A1:H1', '测试详情', get_format(workbook, {'bold': True,
                                                                 'font_size': 18,
                                                                 'align': 'center',
                                                                 'valign': 'vcenter',
                                                                 'bg_color': 'blue',
                                                                 'font_color': '#ffffff'}))
    _write_center(worksheet, "A2", '用例ID', workbook)
    _write_center(worksheet, "B2", '接口名称', workbook)
    _write_center(worksheet, "C2", '接口协议', workbook)
    _write_center(worksheet, "D2", 'URL', workbook)
    _write_center(worksheet, "E2", '参数', workbook)
    _write_center(worksheet, "F2", '预期值', workbook)
    _write_center(worksheet, "G2", '实际值', workbook)
    _write_center(worksheet, "H2", '测试结果', workbook)

    data = {"info": TestReport}  # 获取测试结果被添加到测试报告里

    temp = len(TestReport) + 2
    global hpassnum
    for item in data["info"]:
        if item["t_result"] == "通过":
            hpassnum += 1
        else:
            pass
        _write_center(worksheet, "A" + str(temp), item["t_id"], workbook)
        _write_center(worksheet, "B" + str(temp), item["t_name"], workbook)
        _write_center(worksheet, "C" + str(temp), item["t_method"], workbook)
        _write_center(worksheet, "D" + str(temp), item["t_url"], workbook)
        _write_center(worksheet, "E" + str(temp), item["t_param"], workbook)
        _write_center(worksheet, "F" + str(temp), item["t_hope"], workbook)
        _write_center(worksheet, "G" + str(temp), item["t_actual"], workbook)
        _write_center(worksheet, "H" + str(temp), item["t_result"], workbook)
        temp = temp - 1

# 生成饼形图
def pie(workbook, worksheet):
    chart1 = workbook.add_chart({'type': 'pie'})
    chart1.add_series({
        'name':       '接口测试统计',
        'categories': '=测试总结!$D$4:$D$5',
        'values':    '=测试总结!$E$4:$E$5',
        'points': [
        {'fill': {'color': '#00CD00'}},
        {'fill': {'color': 'red'}},
    ],
    })
    chart1.set_title({'name': '接口测试统计'})
    chart1.set_style(10)
    worksheet.insert_chart('A9', chart1, {'x_offset': 25, 'y_offset': 10})
    # pie(workbook, worksheet)

test_detail(worksheet2)
init(worksheet)

workbook.close()
#
# msg='''
# <table width='800' border='0' cellspacing='0' cellpadding='4'>
#     <tr>
#         <td bgcolor="#CECFAD" height='20' style='font-size:20px'>接口自动化测试报告<a href="http://101.37.15.193:8081/view/接口自动化测试/">更多内容>></a>
#     </tr>
#     <tr>
#         <td bgcolor="#EFEBDE" height='100' style='font-size:13px'>
#         1）测试用例总数：<font color=red>%(yonglizongshu)s</font><br><br>
#         2）通过用例总数：<font color=red>%(tongguoyongli)s</font><br><br>
#         3）失败总数：<font color=red>%(shibaiyongli)s</font><br><br>
#         4）通过率：<font color=red>%(tongguolv)s</font><br><br>
#         5）接口请求地址：<font color=red>%(test_net)s</font><br><br>
#         6）测试时间：<font color=red>%(timenow)s</font><br><br>
#                             详细内容请看附件：<font color=red>%(neirong)s</font>
#     </td>
#     </tr>
# '''
#
# try:
#     logger.info('生成测试报告成功')
#     mymail = MyMail(GetTestConfig('mail.conf'))
#     mymail.connect()
#     mymail.login()
#     mail_content = msg%dict(yonglizongshu=str(len(TestReport)),tongguoyongli=str(hpassnum),shibaiyongli=str(
#         len(TestReport)-hpassnum),tongguolv=str(round(hpassnum/len(TestReport),2)*100),test_net=test_net,timenow=timenow,neirong="【"+(now+'report.xlsx')+"】"
#     )
#     mail_title = '【接口自动化测试报告】'
#
#     attachments = set(
#         [ReportPath]
#     )
#
#     logger.info('正在发送测试报告邮件...')
#     mymail.send_mail(mail_title, mail_content, attachments)
# except Exception as e:
#     logger.info('邮件发送失败：'+str(e))
#     mymail.quit()
# else:
#     mymail.quit()
#     logger.info('发送邮件成功')