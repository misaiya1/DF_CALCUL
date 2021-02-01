#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import sys
import wx
from UI.noname import DF_CALCUL
from ExcelOperator import MyFrame

#生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


''' 复制ppt  '''


app = wx.App()
frame = MyFrame(None)
frame.Show()
#frame.ShowFullScreen(True)
#wx.CallLater(5000, frame.ShowFullScreen, False)
app.MainLoop()

