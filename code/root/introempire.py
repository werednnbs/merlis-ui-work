import ui
import net
import wndMgr
import dbg
import app
import event
import _weakref
import localeInfo
import uiScriptLocale

LOCALE_PATH = "uiscript/"+uiScriptLocale.CODEPAGE+"_"

class SelectEmpireWindow(ui.ScriptWindow):

	class EmpireButton(ui.Window):
		def __init__(self, owner, arg):
			ui.Window.__init__(self)
			self.owner = owner
			self.arg = arg

	def __init__(self, stream):
		print "NEW EMPIRE WINDOW  ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_EMPIRE, self)

		self.stream=stream
		self.empireID=app.GetRandom(1, 3)
		self.empireArea = {}
		self.empireAreaButton = {}

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_EMPIRE, 0)
		print "---------------------------------------------------------------------------- DELETE EMPIRE WINDOW"

	def Close(self):
		print "---------------------------------------------------------------------------- CLOSE EMPIRE WINDOW"		

		self.ClearDictionary()
		self.selectButton = None
		self.empireArea = None
		self.empireAreaButton = None

		self.KillFocus()
		self.Hide()

		app.HideCursor()
		event.Destroy()

	def Open(self):
		print "OPEN EMPIRE WINDOW ----------------------------------------------------------------------------"

		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetWindowName("SelectEmpireWindow")
		self.Show()	

		if not self.__LoadScript(uiScriptLocale.LOCALE_UISCRIPT_PATH + "SelectEmpireWindow.py"):
			dbg.TraceError("SelectEmpireWindow.Open - __LoadScript Error")
			return

		self.__CreateButtons()
		app.ShowCursor()

	def __CreateButtons(self):
		for key, img in self.empireArea.items():

			# img.SetAlpha(0.0)

			(x, y) = img.GetGlobalPosition()
			btn = self.EmpireButton(_weakref.proxy(self), key)
			btn.SetParent(self)
			btn.SetPosition(x, y)
			btn.SetSize(img.GetWidth(), img.GetHeight())
			btn.Show()
			self.empireAreaButton[key] = btn
		
	def OnCreateFailure(self, type):
		if 0 == type:
			self.PopupMessage("Regatul selectat este Plin.")
		if 1 == type:
			self.stream.SetCreateCharacterPhase()

	def PopupMessage(self, msg, func=0):
		if not func:
			func=self.EmptyFunc

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, func, localeInfo.UI_OK)

	def __LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)	
		except:
			import exception
			exception.Abort("SelectEmpireWindow.__LoadScript.LoadObject")

		try:
			GetObject=self.GetChild
			self.selectButton	= GetObject("select_button")
			self.empireAreaA	= GetObject("EmpireArea_A")
			self.empireAreaB	= GetObject("EmpireArea_B")
			self.empireAreaC	= GetObject("EmpireArea_C")
		except:
			import exception
			exception.Abort("SelectEmpireWindow.__LoadScript.BindObject")					

		self.selectButton.SetEvent(ui.__mem_func__(self.ClickSelectButton))

		self.empireAreaA.SetEvent(ui.__mem_func__(self.ClickempireAreaA))
		self.empireAreaB.SetEvent(ui.__mem_func__(self.ClickempireAreaB))
		self.empireAreaC.SetEvent(ui.__mem_func__(self.ClickempireAreaC))

		return 1

	def ClickempireAreaA(self):
		self.empireAreaA.Down()
		self.empireAreaB.SetUp()
		self.empireAreaC.SetUp()
		self.empireID=1

	def ClickempireAreaB(self):
		self.empireAreaA.SetUp()
		self.empireAreaB.Down()
		self.empireAreaC.SetUp()
		self.empireID=2

	def ClickempireAreaC(self):
		self.empireAreaA.SetUp()
		self.empireAreaB.SetUp()
		self.empireAreaC.Down()
		self.empireID=3

	def ClickSelectButton(self):
		net.SendSelectEmpirePacket(self.empireID)
		self.stream.SetSelectCharacterPhase()

	def OnPressEscapeKey(self):
		self.ClickExitButton()
		return TRUE

class ReselectEmpireWindow(SelectEmpireWindow):
	def ClickSelectButton(self):
		net.SendSelectEmpirePacket(self.empireID)
		self.stream.SetCreateCharacterPhase()

	def ClickExitButton(self):
		self.stream.SetSelectCharacterPhase()
