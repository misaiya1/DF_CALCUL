# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jul 11 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class DF_CALCUL
###########################################################################

class DF_CALCUL ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"双馈风电机组电驱系统设计工具", pos = wx.DefaultPosition, size = wx.Size( 1350,600 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"输入参数", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText15.Wrap( -1 )
		
		self.m_staticText15.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		
		bSizer5.Add( self.m_staticText15, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer51 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		fgSizer3 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_Tpp = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"极对数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Tpp.Wrap( -1 )
		
		fgSizer3.Add( self.m_Tpp, 0, wx.ALL, 5 )
		
		self.m_pp = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_pp, 0, wx.ALL, 5 )
		
		self.m_Thz = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"电网频率[Hz]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Thz.Wrap( -1 )
		
		fgSizer3.Add( self.m_Thz, 0, wx.ALL, 5 )
		
		self.m_hz = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"50", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_hz, 0, wx.ALL, 5 )
		
		self.m_TstPower = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"定子无功功率[kW]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_TstPower.Wrap( -1 )
		
		fgSizer3.Add( self.m_TstPower, 0, wx.ALL, 5 )
		
		self.m_StatorRePower = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_StatorRePower, 0, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"转子开口电压[V]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		
		fgSizer3.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.m_RotorOpen = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"3512", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_RotorOpen, 0, wx.ALL, 5 )
		
		self.m_staticText212 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"变流器效率", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )
		
		fgSizer3.Add( self.m_staticText212, 0, wx.ALL, 5 )
		
		self.m_XiaoLv = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_XiaoLv, 0, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"电网电压[V]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		
		fgSizer3.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.m_GridVRMS = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"1140", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_GridVRMS, 0, wx.ALL, 5 )
		
		self.m_Vdc211 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"(选填)变流器直流母线电压[V]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Vdc211.Wrap( -1 )
		
		fgSizer3.Add( self.m_Vdc211, 0, wx.ALL, 5 )
		
		self.m_Vdc = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"1800", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_Vdc, 0, wx.ALL, 5 )
		
		self.m_SetNetMaxI1 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"(选填)网侧变流器最大电流[A]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_SetNetMaxI1.Wrap( -1 )
		
		fgSizer3.Add( self.m_SetNetMaxI1, 0, wx.ALL, 5 )
		
		self.m_SetNetCurMax = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"501", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_SetNetCurMax, 0, wx.ALL, 5 )
		
		self.m_SetGenMaxI11 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"(选填)机侧变流器最大电流[A]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_SetGenMaxI11.Wrap( -1 )
		
		fgSizer3.Add( self.m_SetGenMaxI11, 0, wx.ALL, 5 )
		
		self.m_SetGenCurMax1 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"502", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_SetGenCurMax1, 0, wx.ALL, 5 )
		
		self.m_SetSatMaxI1111 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"(选填)发电机定子最大电流[A]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_SetSatMaxI1111.Wrap( -1 )
		
		fgSizer3.Add( self.m_SetSatMaxI1111, 0, wx.ALL, 5 )
		
		self.m_SetSatMaxI = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"1503", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_SetSatMaxI, 0, wx.ALL, 5 )
		
		self.m_Tgonet = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"(选填)变流器容量[kW]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Tgonet.Wrap( -1 )
		
		fgSizer3.Add( self.m_Tgonet, 0, wx.ALL, 5 )
		
		self.m_GoNetPower = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"3450", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_GoNetPower, 0, wx.ALL, 5 )
		
		
		self.m_scrolledWindow2.SetSizer( fgSizer3 )
		self.m_scrolledWindow2.Layout()
		fgSizer3.Fit( self.m_scrolledWindow2 )
		bSizer51.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"输入激磁电抗、定子漏抗、转子漏抗折算", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		fgSizer31 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer31.SetFlexibleDirection( wx.BOTH )
		fgSizer31.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText221 = wx.StaticText( self, wx.ID_ANY, u"定子电组[ohm]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )
		
		bSizer13.Add( self.m_staticText221, 0, wx.ALL, 5 )
		
		self.m_Rs = wx.TextCtrl( self, wx.ID_ANY, u"0.0081", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_Rs, 0, wx.ALL, 5 )
		
		
		fgSizer31.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		bSizer131 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2211 = wx.StaticText( self, wx.ID_ANY, u"转子电阻[ohm]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2211.Wrap( -1 )
		
		bSizer131.Add( self.m_staticText2211, 0, wx.ALL, 5 )
		
		self.m_Rr = wx.TextCtrl( self, wx.ID_ANY, u"0.0085", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer131.Add( self.m_Rr, 0, wx.ALL, 5 )
		
		
		fgSizer31.Add( bSizer131, 1, wx.EXPAND, 5 )
		
		bSizer132 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_Lksss = wx.StaticText( self, wx.ID_ANY, u"定子漏感[H]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Lksss.Wrap( -1 )
		
		bSizer132.Add( self.m_Lksss, 0, wx.ALL, 5 )
		
		self.m_Lks = wx.TextCtrl( self, wx.ID_ANY, u"0.00019958", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer132.Add( self.m_Lks, 0, wx.ALL, 5 )
		
		
		fgSizer31.Add( bSizer132, 1, wx.EXPAND, 5 )
		
		bSizer133 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_Lkrrr = wx.StaticText( self, wx.ID_ANY, u"转子漏感[H]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Lkrrr.Wrap( -1 )
		
		bSizer133.Add( self.m_Lkrrr, 0, wx.ALL, 5 )
		
		self.m_Lkr = wx.TextCtrl( self, wx.ID_ANY, u"0.0003721", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer133.Add( self.m_Lkr, 0, wx.ALL, 5 )
		
		
		fgSizer31.Add( bSizer133, 1, wx.EXPAND, 5 )
		
		bSizer101 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"电机互感[H]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		
		bSizer101.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.m_Lm = wx.TextCtrl( self, wx.ID_ANY, u"0.014721798", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer101.Add( self.m_Lm, 0, wx.ALL, 5 )
		
		
		fgSizer31.Add( bSizer101, 1, wx.EXPAND, 5 )
		
		
		bSizer51.Add( fgSizer31, 0, 0, 5 )
		
		self.m_staticText1711 = wx.StaticText( self, wx.ID_ANY, u"功率曲线表", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1711.Wrap( -1 )
		
		bSizer51.Add( self.m_staticText1711, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid2.CreateGrid( 2, 26 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 20 )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer51.Add( self.m_grid2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer51, 1, wx.EXPAND, 5 )
		
		bSlideButtZone = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 2, 0, 0, 0 )
		
		self.m_scrolledWindow3 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow3.SetScrollRate( 5, 5 )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer31 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.m_textPPP = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, u"1000", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_textPPP, 0, wx.ALL, 5 )
		
		self.m_textQQQUUU = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_textQQQUUU, 0, wx.ALL, 5 )
		
		self.m_textQQQDDD = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_textQQQDDD, 0, wx.ALL, 5 )
		
		self.m_staticText1712 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"输入P[kW]", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1712.Wrap( -1 )
		
		gSizer31.Add( self.m_staticText1712, 0, wx.ALL, 5 )
		
		self.m_staticText17122 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"定子无功上限", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText17122.Wrap( -1 )
		
		gSizer31.Add( self.m_staticText17122, 0, wx.ALL, 5 )
		
		self.m_staticText171221 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"定子无功下限", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText171221.Wrap( -1 )
		
		gSizer31.Add( self.m_staticText171221, 0, wx.ALL, 5 )
		
		self.m_textQQQ = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, u"1000", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_textQQQ, 0, wx.ALL, 5 )
		
		self.m_textPPPUUU = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_textPPPUUU, 0, wx.ALL, 5 )
		
		self.m_textPPPDDD = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_textPPPDDD, 0, wx.ALL, 5 )
		
		self.m_staticText17121 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"输入Q[kVar]", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText17121.Wrap( -1 )
		
		gSizer31.Add( self.m_staticText17121, 0, wx.ALL, 5 )
		
		self.m_staticText171211 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"定子有功上限", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText171211.Wrap( -1 )
		
		gSizer31.Add( self.m_staticText171211, 0, wx.ALL, 5 )
		
		self.m_staticText171212 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"定子有功下限", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText171212.Wrap( -1 )
		
		gSizer31.Add( self.m_staticText171212, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( gSizer31, 1, wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow3.SetSizer( bSizer14 )
		self.m_scrolledWindow3.Layout()
		bSizer14.Fit( self.m_scrolledWindow3 )
		gSizer2.Add( self.m_scrolledWindow3, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		gSizer5 = wx.GridSizer( 2, 2, 0, 0 )
		
		bSizer134 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrlS = wx.TextCtrl( self, wx.ID_ANY, u"1725", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer134.Add( self.m_textCtrlS, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText171 = wx.StaticText( self, wx.ID_ANY, u"右侧计算使用的转速点[RPM]", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText171.Wrap( -1 )
		
		bSizer134.Add( self.m_staticText171, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gSizer5.Add( bSizer134, 1, wx.EXPAND, 5 )
		
		self.m_button = wx.Button( self, wx.ID_ANY, u"重新单点计算", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"有无功能力边界计算", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"报告生成", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer11.Add( gSizer5, 1, wx.EXPAND, 5 )
		
		
		gSizer2.Add( bSizer11, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSlideButtZone.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSlideButtZone, 0, wx.EXPAND, 5 )
		
		
		gSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"计算结果(转速点)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText16.Wrap( -1 )
		
		self.m_staticText16.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		
		bSizer7.Add( self.m_staticText16, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer71 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText311 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"同步转速[RPM]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText311.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText311, 0, wx.ALL, 5 )
		
		self.m_SynsSpeed = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_SynsSpeed, 0, wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"转差率", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.m_ZhuanChaLv = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_ZhuanChaLv, 0, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"定子有功功率[kW]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		self.m_StatorAPower = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_StatorAPower, 0, wx.ALL, 5 )
		
		self.m_TRotorAPower = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"转子有功功率[kW]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_TRotorAPower.Wrap( -1 )
		
		fgSizer4.Add( self.m_TRotorAPower, 0, wx.ALL, 5 )
		
		self.m_RotorAPower = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_RotorAPower, 0, wx.ALL, 5 )
		
		self.m_staticText401 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText401.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText401, 0, wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		self.m_staticText29 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"机侧变流器（电机转子）d轴电流[A]（有功  负号表示流向电网）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText29, 0, wx.ALL, 5 )
		
		self.m_GenId = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_GenId, 0, wx.ALL, 5 )
		
		self.m_staticText3111 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"机侧变流器（电机转子）q轴电流[A]（无功  负号表示流向电网）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3111.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText3111, 0, wx.ALL, 5 )
		
		self.m_GenIq = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_GenIq, 0, wx.ALL, 5 )
		
		self.m_staticText30 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"机侧变流器（电机转子）电流[A]（有效值 归算值）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText30, 0, wx.ALL, 5 )
		
		self.m_GenIrmsGS = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_GenIrmsGS, 0, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"机侧变流器（电机转子）电流[A]（有效值 实际值）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		self.m_GenIrmsSJ = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_GenIrmsSJ, 0, wx.ALL, 5 )
		
		self.m_staticText421 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText421.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText421, 0, wx.ALL, 5 )
		
		self.m_staticText422 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText422.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText422, 0, wx.ALL, 5 )
		
		self.m_NetId = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"网侧变流器d轴电流[A]（有功  负号表示流向电网）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_NetId.Wrap( -1 )
		
		fgSizer4.Add( self.m_NetId, 0, wx.ALL, 5 )
		
		self.m_NetId = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_NetId, 0, wx.ALL, 5 )
		
		self.m_NetIq = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"网侧变流器q轴电流[A]（无功  负号表示流向电网）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_NetIq.Wrap( -1 )
		
		fgSizer4.Add( self.m_NetIq, 0, wx.ALL, 5 )
		
		self.m_NetIq = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_NetIq, 0, wx.ALL, 5 )
		
		self.m_NetIrms1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"网侧变流器电流[A]（有效值 负号表示流向电网）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_NetIrms1.Wrap( -1 )
		
		fgSizer4.Add( self.m_NetIrms1, 0, wx.ALL, 5 )
		
		self.m_NetIrms = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_NetIrms, 0, wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText42, 0, wx.ALL, 5 )
		
		self.m_staticText43 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText43, 0, wx.ALL, 5 )
		
		self.m_staticText312 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"电机定子d轴电流[A]（有功）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText312.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText312, 0, wx.ALL, 5 )
		
		self.m_StatorId = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_StatorId, 0, wx.ALL, 5 )
		
		self.m_staticText32 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"电机定子q轴电流[A]（无功）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		self.m_StatorIq = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_StatorIq, 0, wx.ALL, 5 )
		
		self.m_staticText33 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"电机定子电流[A]（有效值 实际值）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText33, 0, wx.ALL, 5 )
		
		self.m_StatorIrms = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_StatorIrms, 0, wx.ALL, 5 )
		
		self.m_staticText44 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText44, 0, wx.ALL, 5 )
		
		self.m_staticText45 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText45, 0, wx.ALL, 5 )
		
		self.m_staticText35 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"机侧变流器（电机转子）d轴电压[V]（归算值）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		self.m_GenVd = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_GenVd, 0, wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"机侧变流器（电机转子）q轴电压[V]（归算值）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		self.m_GenVq = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_GenVq, 0, wx.ALL, 5 )
		
		self.m_staticText37 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"机侧变流器（电机转子）相电压[V]（相峰值 归算值）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText37, 0, wx.ALL, 5 )
		
		self.m_GenV = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_GenV, 0, wx.ALL, 5 )
		
		self.m_staticText38 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"机侧变流器（电机转子）线电压[V]（RMS 实际值）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText38, 0, wx.ALL, 5 )
		
		self.m_GenVrms = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_GenVrms, 0, wx.ALL, 5 )
		
		self.m_staticText40 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"电磁扭矩[Nm]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText40, 0, wx.ALL, 5 )
		
		self.m_Torque = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_Torque, 0, wx.ALL, 5 )
		
		self.m_staticText441 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText441.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText441, 0, wx.ALL, 5 )
		
		self.m_staticText442 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText442.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText442, 0, wx.ALL, 5 )
		
		self.m_staticText402 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"网侧无功功率最大值[kVar]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText402.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText402, 0, wx.ALL, 5 )
		
		self.m_Var1 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_Var1, 0, wx.ALL, 5 )
		
		
		bSizer71.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( bSizer71 )
		self.m_scrolledWindow1.Layout()
		bSizer71.Fit( self.m_scrolledWindow1 )
		bSizer7.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		gSizer3.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer3 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu5 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"说明信息", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"版本信息", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem3 )
		
		self.m_menubar1.Append( self.m_menu5, u"说明" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.OnCheck )
		self.m_button.Bind( wx.EVT_BUTTON, self.m_buttonOnButtonClick )
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_buttonOnButtonClick3 )
		self.m_button2.Bind( wx.EVT_BUTTON, self.m_buttonOnButtonClick2 )
		self.Bind( wx.EVT_MENU, self.mOnMenuSelection2, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.mOnMenuSelection1, id = self.m_menuItem3.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCheck( self, event ):
		event.Skip()
	
	def m_buttonOnButtonClick( self, event ):
		event.Skip()
	
	def m_buttonOnButtonClick3( self, event ):
		event.Skip()
	
	def m_buttonOnButtonClick2( self, event ):
		event.Skip()
	
	def mOnMenuSelection2( self, event ):
		event.Skip()
	
	def mOnMenuSelection1( self, event ):
		event.Skip()
	

