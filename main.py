#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import sys
import wx
from UI.noname import DF_CALCUL
from ExcelOperator import MyFrame
from ExcelOperator import save_all



#生成资源文件目录访问路径
# def resource_path(relative_path):
#     if getattr(sys, 'frozen', False): #是否Bundle Resource
#         base_path = sys._MEIPASS
#     else:
#         base_path = os.path.abspath(".")
#     return os.path.join(base_path, relative_path)

def main():

    app = wx.App()
    frame = MyFrame(None)
    frame.Show()
    #frame.ShowFullScreen(True)
    #wx.CallLater(5000, frame.ShowFullScreen, False)
    app.MainLoop()
    del app
    del frame
    save_all()

if __name__ == '__main__':
    main()
