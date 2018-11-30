import os
import time

def GetTestDataPath():
    ospath=os.path.dirname(os.path.abspath(__file__))
    return os.path.join(ospath,"TestData.xls")

def GetTestReport():
    now=time.strftime("%Y-%m-%d-%H-%M-%S-",time.localtime(time.time()))
    ospath=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(ospath,"apiauto1\\testreport",now+"TestReport.xlsx")

def GetTestLogPath():
    ospath=os.path.dirname(os.path.abspath(__file__))
    return os.path.join(ospath,'log.txt')

def GetTestConfig(configname):
    ospath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath,"config",configname)