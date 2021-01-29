#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import wx
from UI.noname import DF_CALCUL
from ExcelOperator import MyFrame

app = wx.App()
frame = MyFrame(None)
frame.Show()
#frame.ShowFullScreen(True)
#wx.CallLater(5000, frame.ShowFullScreen, False)
app.MainLoop()

