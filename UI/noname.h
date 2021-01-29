///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jul 11 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __NONAME_H__
#define __NONAME_H__

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/textctrl.h>
#include <wx/sizer.h>
#include <wx/scrolwin.h>
#include <wx/checkbox.h>
#include <wx/grid.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/button.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class DF_CALCUL
///////////////////////////////////////////////////////////////////////////////
class DF_CALCUL : public wxFrame 
{
	private:
	
	protected:
		wxStaticText* m_staticText15;
		wxScrolledWindow* m_scrolledWindow2;
		wxStaticText* m_Tpp;
		wxTextCtrl* m_pp;
		wxStaticText* m_Thz;
		wxTextCtrl* m_hz;
		wxStaticText* m_Tgonet;
		wxTextCtrl* m_GoNetPower;
		wxStaticText* m_TstPower;
		wxTextCtrl* m_StatorRePower;
		wxStaticText* m_staticText20;
		wxTextCtrl* m_RotorOpen;
		wxStaticText* m_staticText212;
		wxTextCtrl* m_XiaoLv;
		wxStaticText* m_staticText21;
		wxTextCtrl* m_GridVRMS;
		wxStaticText* m_Vdc211;
		wxTextCtrl* m_Vdc;
		wxStaticText* m_SetNetMaxI1;
		wxTextCtrl* m_SetNetCurMax;
		wxStaticText* m_SetGenMaxI11;
		wxTextCtrl* m_SetGenCurMax1;
		wxStaticText* m_SetSatMaxI1111;
		wxTextCtrl* m_SetSatMaxI;
		wxCheckBox* m_checkBox1;
		wxStaticText* m_staticText221;
		wxTextCtrl* m_Rs;
		wxStaticText* m_staticText2211;
		wxTextCtrl* m_Rr;
		wxStaticText* m_Lksss;
		wxTextCtrl* m_Lks;
		wxStaticText* m_Lkrrr;
		wxTextCtrl* m_Lkr;
		wxStaticText* m_staticText22;
		wxTextCtrl* m_Lm;
		wxStaticText* m_staticText1711;
		wxGrid* m_grid2;
		wxTextCtrl* m_textCtrlS;
		wxStaticText* m_staticText171;
		wxButton* m_button;
		wxButton* m_button2;
		wxStaticText* m_staticText201;
		wxStaticText* m_staticText251;
		wxStaticText* m_staticText2511;
		wxStaticText* m_staticText16;
		wxScrolledWindow* m_scrolledWindow1;
		wxStaticText* m_staticText311;
		wxTextCtrl* m_SynsSpeed;
		wxStaticText* m_staticText25;
		wxTextCtrl* m_ZhuanChaLv;
		wxStaticText* m_staticText26;
		wxTextCtrl* m_StatorAPower;
		wxStaticText* m_TRotorAPower;
		wxTextCtrl* m_RotorAPower;
		wxStaticText* m_staticText401;
		wxStaticText* m_staticText41;
		wxStaticText* m_staticText29;
		wxTextCtrl* m_GenId;
		wxStaticText* m_staticText3111;
		wxTextCtrl* m_GenIq;
		wxStaticText* m_staticText30;
		wxTextCtrl* m_GenIrmsGS;
		wxStaticText* m_staticText31;
		wxTextCtrl* m_GenIrmsSJ;
		wxStaticText* m_staticText421;
		wxStaticText* m_staticText422;
		wxStaticText* m_NetId;
		wxTextCtrl* m_NetId;
		wxStaticText* m_NetIq;
		wxTextCtrl* m_NetIq;
		wxStaticText* m_NetIrms1;
		wxTextCtrl* m_NetIrms;
		wxStaticText* m_staticText42;
		wxStaticText* m_staticText43;
		wxStaticText* m_staticText312;
		wxTextCtrl* m_StatorId;
		wxStaticText* m_staticText32;
		wxTextCtrl* m_StatorIq;
		wxStaticText* m_staticText33;
		wxTextCtrl* m_StatorIrms;
		wxStaticText* m_staticText44;
		wxStaticText* m_staticText45;
		wxStaticText* m_staticText35;
		wxTextCtrl* m_GenVd;
		wxStaticText* m_staticText36;
		wxTextCtrl* m_GenVq;
		wxStaticText* m_staticText37;
		wxTextCtrl* m_GenV;
		wxStaticText* m_staticText38;
		wxTextCtrl* m_GenVrms;
		wxStaticText* m_staticText40;
		wxTextCtrl* m_Torque;
		
		// Virtual event handlers, overide them in your derived class
		virtual void OnCheck( wxCommandEvent& event ) { event.Skip(); }
		virtual void m_buttonOnButtonClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void m_buttonOnButtonClick2( wxCommandEvent& event ) { event.Skip(); }
		
	
	public:
		
		DF_CALCUL( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("双馈风电机组电驱系统设计工具"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 1300,650 ), long style = wxCAPTION|wxCLOSE_BOX|wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		
		~DF_CALCUL();
	
};

#endif //__NONAME_H__
