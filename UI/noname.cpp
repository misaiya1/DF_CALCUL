///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jul 11 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

DF_CALCUL::DF_CALCUL( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxGridSizer* gSizer3;
	gSizer3 = new wxGridSizer( 0, 2, 0, 0 );
	
	wxBoxSizer* bSizer5;
	bSizer5 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText15 = new wxStaticText( this, wxID_ANY, wxT("输入参数"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticText15->Wrap( -1 );
	m_staticText15->SetFont( wxFont( 18, wxFONTFAMILY_DEFAULT, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, false, wxT("宋体") ) );
	
	bSizer5->Add( m_staticText15, 0, wxALL|wxEXPAND, 5 );
	
	wxBoxSizer* bSizer51;
	bSizer51 = new wxBoxSizer( wxVERTICAL );
	
	m_scrolledWindow2 = new wxScrolledWindow( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxHSCROLL|wxVSCROLL );
	m_scrolledWindow2->SetScrollRate( 5, 5 );
	wxFlexGridSizer* fgSizer3;
	fgSizer3 = new wxFlexGridSizer( 0, 4, 0, 0 );
	fgSizer3->SetFlexibleDirection( wxBOTH );
	fgSizer3->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );
	
	m_Tpp = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("极对数"), wxDefaultPosition, wxDefaultSize, 0 );
	m_Tpp->Wrap( -1 );
	fgSizer3->Add( m_Tpp, 0, wxALL, 5 );
	
	m_pp = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("2"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_pp, 0, wxALL, 5 );
	
	m_Thz = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("电网频率[Hz]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_Thz->Wrap( -1 );
	fgSizer3->Add( m_Thz, 0, wxALL, 5 );
	
	m_hz = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("50"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_hz, 0, wxALL, 5 );
	
	m_Tgonet = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("上网总功率[kW]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_Tgonet->Wrap( -1 );
	fgSizer3->Add( m_Tgonet, 0, wxALL, 5 );
	
	m_GoNetPower = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("3450"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_GoNetPower, 0, wxALL, 5 );
	
	m_TstPower = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("定子无功功率[kW]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_TstPower->Wrap( -1 );
	fgSizer3->Add( m_TstPower, 0, wxALL, 5 );
	
	m_StatorRePower = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("0"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_StatorRePower, 0, wxALL, 5 );
	
	m_staticText20 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("转子开口电压[V]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText20->Wrap( -1 );
	fgSizer3->Add( m_staticText20, 0, wxALL, 5 );
	
	m_RotorOpen = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("3512"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_RotorOpen, 0, wxALL, 5 );
	
	m_staticText212 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("变流器效率"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText212->Wrap( -1 );
	fgSizer3->Add( m_staticText212, 0, wxALL, 5 );
	
	m_XiaoLv = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("1"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_XiaoLv, 0, wxALL, 5 );
	
	m_staticText21 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("电网电压[V]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText21->Wrap( -1 );
	fgSizer3->Add( m_staticText21, 0, wxALL, 5 );
	
	m_GridVRMS = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("1140"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_GridVRMS, 0, wxALL, 5 );
	
	m_Vdc211 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("(选填)变流器直流母线电压[V]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_Vdc211->Wrap( -1 );
	fgSizer3->Add( m_Vdc211, 0, wxALL, 5 );
	
	m_Vdc = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("1800"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_Vdc, 0, wxALL, 5 );
	
	m_SetNetMaxI1 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("(选填)网侧变流器最大电流[A]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_SetNetMaxI1->Wrap( -1 );
	fgSizer3->Add( m_SetNetMaxI1, 0, wxALL, 5 );
	
	m_SetNetCurMax = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("400"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_SetNetCurMax, 0, wxALL, 5 );
	
	m_SetGenMaxI11 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("(选填)机侧变流器最大电流[A]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_SetGenMaxI11->Wrap( -1 );
	fgSizer3->Add( m_SetGenMaxI11, 0, wxALL, 5 );
	
	m_SetGenCurMax1 = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("400"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_SetGenCurMax1, 0, wxALL, 5 );
	
	m_SetSatMaxI1111 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("(选填)发电机定子最大电流[A]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_SetSatMaxI1111->Wrap( -1 );
	fgSizer3->Add( m_SetSatMaxI1111, 0, wxALL, 5 );
	
	m_SetSatMaxI = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("0"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_SetSatMaxI, 0, wxALL, 5 );
	
	
	m_scrolledWindow2->SetSizer( fgSizer3 );
	m_scrolledWindow2->Layout();
	fgSizer3->Fit( m_scrolledWindow2 );
	bSizer51->Add( m_scrolledWindow2, 1, wxEXPAND | wxALL, 5 );
	
	m_checkBox1 = new wxCheckBox( this, wxID_ANY, wxT("输入激磁电抗、定子漏抗、转子漏抗折算"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer51->Add( m_checkBox1, 0, wxALL, 5 );
	
	wxFlexGridSizer* fgSizer31;
	fgSizer31 = new wxFlexGridSizer( 0, 5, 0, 0 );
	fgSizer31->SetFlexibleDirection( wxBOTH );
	fgSizer31->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );
	
	wxBoxSizer* bSizer13;
	bSizer13 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText221 = new wxStaticText( this, wxID_ANY, wxT("定子电组[ohm]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText221->Wrap( -1 );
	bSizer13->Add( m_staticText221, 0, wxALL, 5 );
	
	m_Rs = new wxTextCtrl( this, wxID_ANY, wxT("0.0096"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer13->Add( m_Rs, 0, wxALL, 5 );
	
	
	fgSizer31->Add( bSizer13, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer131;
	bSizer131 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText2211 = new wxStaticText( this, wxID_ANY, wxT("转子电阻[ohm]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText2211->Wrap( -1 );
	bSizer131->Add( m_staticText2211, 0, wxALL, 5 );
	
	m_Rr = new wxTextCtrl( this, wxID_ANY, wxT("0.0085"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer131->Add( m_Rr, 0, wxALL, 5 );
	
	
	fgSizer31->Add( bSizer131, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer132;
	bSizer132 = new wxBoxSizer( wxVERTICAL );
	
	m_Lksss = new wxStaticText( this, wxID_ANY, wxT("定子漏感[H]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_Lksss->Wrap( -1 );
	bSizer132->Add( m_Lksss, 0, wxALL, 5 );
	
	m_Lks = new wxTextCtrl( this, wxID_ANY, wxT("1.9735e-4"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer132->Add( m_Lks, 0, wxALL, 5 );
	
	
	fgSizer31->Add( bSizer132, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer133;
	bSizer133 = new wxBoxSizer( wxVERTICAL );
	
	m_Lkrrr = new wxStaticText( this, wxID_ANY, wxT("转子漏感[H]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_Lkrrr->Wrap( -1 );
	bSizer133->Add( m_Lkrrr, 0, wxALL, 5 );
	
	m_Lkr = new wxTextCtrl( this, wxID_ANY, wxT("3.5619e-4"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer133->Add( m_Lkr, 0, wxALL, 5 );
	
	
	fgSizer31->Add( bSizer133, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer101;
	bSizer101 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText22 = new wxStaticText( this, wxID_ANY, wxT("电机互感[H]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText22->Wrap( -1 );
	bSizer101->Add( m_staticText22, 0, wxALL, 5 );
	
	m_Lm = new wxTextCtrl( this, wxID_ANY, wxT("0.01373"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer101->Add( m_Lm, 0, wxALL, 5 );
	
	
	fgSizer31->Add( bSizer101, 1, wxEXPAND, 5 );
	
	
	bSizer51->Add( fgSizer31, 0, 0, 5 );
	
	m_staticText1711 = new wxStaticText( this, wxID_ANY, wxT("功率曲线表"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticText1711->Wrap( -1 );
	bSizer51->Add( m_staticText1711, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_grid2 = new wxGrid( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
	
	// Grid
	m_grid2->CreateGrid( 2, 26 );
	m_grid2->EnableEditing( true );
	m_grid2->EnableGridLines( true );
	m_grid2->SetGridLineColour( wxSystemSettings::GetColour( wxSYS_COLOUR_APPWORKSPACE ) );
	m_grid2->EnableDragGridSize( false );
	m_grid2->SetMargins( 0, 0 );
	
	// Columns
	m_grid2->EnableDragColMove( false );
	m_grid2->EnableDragColSize( true );
	m_grid2->SetColLabelSize( 20 );
	m_grid2->SetColLabelAlignment( wxALIGN_CENTRE, wxALIGN_CENTRE );
	
	// Rows
	m_grid2->EnableDragRowSize( true );
	m_grid2->SetRowLabelSize( 80 );
	m_grid2->SetRowLabelAlignment( wxALIGN_CENTRE, wxALIGN_CENTRE );
	
	// Label Appearance
	
	// Cell Defaults
	m_grid2->SetDefaultCellAlignment( wxALIGN_LEFT, wxALIGN_TOP );
	bSizer51->Add( m_grid2, 1, wxALL|wxEXPAND, 5 );
	
	
	bSizer5->Add( bSizer51, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSlideButtZone;
	bSlideButtZone = new wxBoxSizer( wxVERTICAL );
	
	wxGridSizer* gSizer2;
	gSizer2 = new wxGridSizer( 0, 2, 0, 0 );
	
	wxBoxSizer* bSizer11;
	bSizer11 = new wxBoxSizer( wxVERTICAL );
	
	m_textCtrlS = new wxTextCtrl( this, wxID_ANY, wxT("1725"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer11->Add( m_textCtrlS, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_staticText171 = new wxStaticText( this, wxID_ANY, wxT("右侧计算使用的转速点[RPM]"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticText171->Wrap( -1 );
	bSizer11->Add( m_staticText171, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	gSizer2->Add( bSizer11, 0, wxEXPAND|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	wxBoxSizer* bSizer12;
	bSizer12 = new wxBoxSizer( wxVERTICAL );
	
	m_button = new wxButton( this, wxID_ANY, wxT("重新单点计算"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer12->Add( m_button, 0, wxALL|wxEXPAND, 5 );
	
	m_button2 = new wxButton( this, wxID_ANY, wxT("报告生成"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer12->Add( m_button2, 0, wxALL|wxEXPAND, 5 );
	
	
	gSizer2->Add( bSizer12, 0, wxEXPAND, 5 );
	
	
	bSlideButtZone->Add( gSizer2, 0, wxEXPAND, 5 );
	
	m_staticText201 = new wxStaticText( this, wxID_ANY, wxT("备注1：dq变换为等幅值形式；"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText201->Wrap( -1 );
	bSlideButtZone->Add( m_staticText201, 0, wxALL|wxEXPAND, 5 );
	
	m_staticText251 = new wxStaticText( this, wxID_ANY, wxT("备注2：“归算值”表示电机数学模型中将转子侧参数统一折算到定子侧，与Matlab仿真模型计算值相同； “实际值”表示反折算过程，与实际系统的测量值相同；"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText251->Wrap( -1 );
	bSlideButtZone->Add( m_staticText251, 0, wxALL|wxEXPAND, 5 );
	
	m_staticText2511 = new wxStaticText( this, wxID_ANY, wxT("备注3：Lm(互感)      = Xm(激磁电抗or磁化电抗) / (2pi*f)    其中 f为电网频率。定子漏感，转子漏感计算方式相同。"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText2511->Wrap( -1 );
	bSlideButtZone->Add( m_staticText2511, 0, wxALL|wxEXPAND, 5 );
	
	
	bSizer5->Add( bSlideButtZone, 0, wxEXPAND, 5 );
	
	
	gSizer3->Add( bSizer5, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer7;
	bSizer7 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText16 = new wxStaticText( this, wxID_ANY, wxT("计算结果(转速点)"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticText16->Wrap( -1 );
	m_staticText16->SetFont( wxFont( 18, wxFONTFAMILY_DEFAULT, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, false, wxT("宋体") ) );
	
	bSizer7->Add( m_staticText16, 0, wxALL|wxEXPAND, 5 );
	
	m_scrolledWindow1 = new wxScrolledWindow( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxHSCROLL|wxVSCROLL );
	m_scrolledWindow1->SetScrollRate( 5, 5 );
	wxBoxSizer* bSizer71;
	bSizer71 = new wxBoxSizer( wxVERTICAL );
	
	wxFlexGridSizer* fgSizer4;
	fgSizer4 = new wxFlexGridSizer( 0, 2, 0, 0 );
	fgSizer4->SetFlexibleDirection( wxBOTH );
	fgSizer4->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );
	
	m_staticText311 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("同步转速[RPM]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText311->Wrap( -1 );
	fgSizer4->Add( m_staticText311, 0, wxALL, 5 );
	
	m_SynsSpeed = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_SynsSpeed, 0, wxALL, 5 );
	
	m_staticText25 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("转差率"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText25->Wrap( -1 );
	fgSizer4->Add( m_staticText25, 0, wxALL, 5 );
	
	m_ZhuanChaLv = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_ZhuanChaLv, 0, wxALL, 5 );
	
	m_staticText26 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("定子有功功率[kW]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText26->Wrap( -1 );
	fgSizer4->Add( m_staticText26, 0, wxALL, 5 );
	
	m_StatorAPower = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_StatorAPower, 0, wxALL, 5 );
	
	m_TRotorAPower = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("转子有功功率[kW]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_TRotorAPower->Wrap( -1 );
	fgSizer4->Add( m_TRotorAPower, 0, wxALL, 5 );
	
	m_RotorAPower = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_RotorAPower, 0, wxALL, 5 );
	
	m_staticText401 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText401->Wrap( -1 );
	fgSizer4->Add( m_staticText401, 0, wxALL, 5 );
	
	m_staticText41 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText41->Wrap( -1 );
	fgSizer4->Add( m_staticText41, 0, wxALL, 5 );
	
	m_staticText29 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("机侧变流器（电机转子）d轴电流[A]（有功  负号表示流向电网）"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText29->Wrap( -1 );
	fgSizer4->Add( m_staticText29, 0, wxALL, 5 );
	
	m_GenId = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_GenId, 0, wxALL, 5 );
	
	m_staticText3111 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("机侧变流器（电机转子）q轴电流[A]（无功  负号表示流向电网）"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText3111->Wrap( -1 );
	fgSizer4->Add( m_staticText3111, 0, wxALL, 5 );
	
	m_GenIq = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_GenIq, 0, wxALL, 5 );
	
	m_staticText30 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("机侧变流器（电机转子）电流[A]（有效值 归算值）"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText30->Wrap( -1 );
	fgSizer4->Add( m_staticText30, 0, wxALL, 5 );
	
	m_GenIrmsGS = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_GenIrmsGS, 0, wxALL, 5 );
	
	m_staticText31 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("机侧变流器（电机转子）电流[A]（有效值 实际值）"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText31->Wrap( -1 );
	fgSizer4->Add( m_staticText31, 0, wxALL, 5 );
	
	m_GenIrmsSJ = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_GenIrmsSJ, 0, wxALL, 5 );
	
	m_staticText421 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText421->Wrap( -1 );
	fgSizer4->Add( m_staticText421, 0, wxALL, 5 );
	
	m_staticText422 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText422->Wrap( -1 );
	fgSizer4->Add( m_staticText422, 0, wxALL, 5 );
	
	m_NetId = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("网侧变流器d轴电流[A]（有功  负号表示流向电网）"), wxDefaultPosition, wxDefaultSize, 0 );
	m_NetId->Wrap( -1 );
	fgSizer4->Add( m_NetId, 0, wxALL, 5 );
	
	m_NetId = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_NetId, 0, wxALL, 5 );
	
	m_NetIq = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("网侧变流器q轴电流[A]（无功  负号表示流向电网）"), wxDefaultPosition, wxDefaultSize, 0 );
	m_NetIq->Wrap( -1 );
	fgSizer4->Add( m_NetIq, 0, wxALL, 5 );
	
	m_NetIq = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_NetIq, 0, wxALL, 5 );
	
	m_NetIrms1 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("网侧变流器电流[A]（有效值 负号表示流向电网）"), wxDefaultPosition, wxDefaultSize, 0 );
	m_NetIrms1->Wrap( -1 );
	fgSizer4->Add( m_NetIrms1, 0, wxALL, 5 );
	
	m_NetIrms = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_NetIrms, 0, wxALL, 5 );
	
	m_staticText42 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText42->Wrap( -1 );
	fgSizer4->Add( m_staticText42, 0, wxALL, 5 );
	
	m_staticText43 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText43->Wrap( -1 );
	fgSizer4->Add( m_staticText43, 0, wxALL, 5 );
	
	m_staticText312 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("电机定子d轴电流[A]（有功）"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText312->Wrap( -1 );
	fgSizer4->Add( m_staticText312, 0, wxALL, 5 );
	
	m_StatorId = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_StatorId, 0, wxALL, 5 );
	
	m_staticText32 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("电机定子q轴电流[A]（无功）"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText32->Wrap( -1 );
	fgSizer4->Add( m_staticText32, 0, wxALL, 5 );
	
	m_StatorIq = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_StatorIq, 0, wxALL, 5 );
	
	m_staticText33 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("电机定子电流[A]（有效值 实际值）"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText33->Wrap( -1 );
	fgSizer4->Add( m_staticText33, 0, wxALL, 5 );
	
	m_StatorIrms = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_StatorIrms, 0, wxALL, 5 );
	
	m_staticText44 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText44->Wrap( -1 );
	fgSizer4->Add( m_staticText44, 0, wxALL, 5 );
	
	m_staticText45 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText45->Wrap( -1 );
	fgSizer4->Add( m_staticText45, 0, wxALL, 5 );
	
	m_staticText35 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("机侧变流器（电机转子）d轴电压[V]（归算值）"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText35->Wrap( -1 );
	fgSizer4->Add( m_staticText35, 0, wxALL, 5 );
	
	m_GenVd = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_GenVd, 0, wxALL, 5 );
	
	m_staticText36 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("机侧变流器（电机转子）q轴电压[V]（归算值）"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText36->Wrap( -1 );
	fgSizer4->Add( m_staticText36, 0, wxALL, 5 );
	
	m_GenVq = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_GenVq, 0, wxALL, 5 );
	
	m_staticText37 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("机侧变流器（电机转子）相电压[V]（相峰值 归算值）"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText37->Wrap( -1 );
	fgSizer4->Add( m_staticText37, 0, wxALL, 5 );
	
	m_GenV = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_GenV, 0, wxALL, 5 );
	
	m_staticText38 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("机侧变流器（电机转子）线电压[V]（RMS 实际值）"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText38->Wrap( -1 );
	fgSizer4->Add( m_staticText38, 0, wxALL, 5 );
	
	m_GenVrms = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_GenVrms, 0, wxALL, 5 );
	
	m_staticText40 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("电磁扭矩[Nm]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText40->Wrap( -1 );
	fgSizer4->Add( m_staticText40, 0, wxALL, 5 );
	
	m_Torque = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_Torque, 0, wxALL, 5 );
	
	
	bSizer71->Add( fgSizer4, 1, wxEXPAND, 5 );
	
	
	m_scrolledWindow1->SetSizer( bSizer71 );
	m_scrolledWindow1->Layout();
	bSizer71->Fit( m_scrolledWindow1 );
	bSizer7->Add( m_scrolledWindow1, 1, wxEXPAND | wxALL, 5 );
	
	
	gSizer3->Add( bSizer7, 1, wxEXPAND, 5 );
	
	
	this->SetSizer( gSizer3 );
	this->Layout();
	
	this->Centre( wxBOTH );
	
	// Connect Events
	m_checkBox1->Connect( wxEVT_COMMAND_CHECKBOX_CLICKED, wxCommandEventHandler( DF_CALCUL::OnCheck ), NULL, this );
	m_button->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( DF_CALCUL::m_buttonOnButtonClick ), NULL, this );
	m_button2->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( DF_CALCUL::m_buttonOnButtonClick2 ), NULL, this );
}

DF_CALCUL::~DF_CALCUL()
{
	// Disconnect Events
	m_checkBox1->Disconnect( wxEVT_COMMAND_CHECKBOX_CLICKED, wxCommandEventHandler( DF_CALCUL::OnCheck ), NULL, this );
	m_button->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( DF_CALCUL::m_buttonOnButtonClick ), NULL, this );
	m_button2->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( DF_CALCUL::m_buttonOnButtonClick2 ), NULL, this );
	
}
