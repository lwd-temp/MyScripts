# Shutdown.pyw
# 在22:01关闭计算机
# Author:lwd-temp
# 使用os.system实现
import os
import datetime
import sys
 
nowtime=datetime.datetime.now()
nowmon=nowtime.month
nowday=nowtime.day
nowye=nowtime.year
 
strthe=str(nowye)+"-"+str(nowmon)+"-"+str(nowday)+" "+str(22)+":"+str(1)+":"+"0.0"
thetime=datetime.datetime.strptime(strthe,"%Y-%m-%d %H:%M:%S.%f")
delta=(thetime-nowtime).seconds
 
if nowtime.weekday()==6:
    os.system("shutdown -s -t 300")
    sys.exit()
 
if delta<=600:
    delta=600
 
os.system("shutdown -s -t "+str(delta))
