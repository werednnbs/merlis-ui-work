import chr
import grp
import os
import dbg
import app
import math
import wndMgr
import snd
import net
import systemSetting
import localeInfo
import ui
import uiScriptlocale
import networkModule
import musicInfo
import playerSettingModule
import uiCommon
import uiMapNameShower
import uiAffectShower
import uiCharacter
import uiTarget
import consoleModule
import interfaceModule
import uiTaskBar
import uiInventory
import player
import chat
import uiPlayerGauge
import uiScriptLocale

LEAVE_BUTTON_FOR_POTAL = False
NOT_NEED_DELETE_CODE = False
ENABLE_ENGNUM_DELETE_CODE = False
RESOURCE = uiScriptLocale.LOCALE_UISCRIPT_PATH + "selectcharacterwindow/"

if localeInfo.IsJAPAN():
	NOT_NEED_DELETE_CODE = True
elif localeInfo.IsHONGKONG():
	ENABLE_ENGNUM_DELETE_CODE = True
elif localeInfo.IsEUROPE():
	ENABLE_ENGNUM_DELETE_CODE = True

class SelectCharacterWindow(ui.Window):

	SLOT_COUNT = 4
	CHARACTER_TYPE_COUNT = 4

	EMPIRE_NAME = { 
		net.EMPIRE_A : localeInfo.EMPIRE_A, 
		net.EMPIRE_B : localeInfo.EMPIRE_B, 
		net.EMPIRE_C : localeInfo.EMPIRE_C 
	}

	class CharacterRenderer(ui.Window):
		def OnRender(self):
			grp.ClearDepthBuffer()

			grp.SetGameRenderState()
			grp.PushState()
			grp.SetOmniLight()

			screenWidth = wndMgr.GetScreenWidth()
			screenHeight = wndMgr.GetScreenHeight()
			newScreenWidth = float(screenWidth - 270)
			newScreenHeight = float(screenHeight)

			grp.SetViewport(250.0/screenWidth, 0.0, newScreenWidth/screenWidth, newScreenHeight/screenHeight)

			app.SetCenterPosition(-40.0, -80.0, -10.0)
			app.SetCamera(1920.0, 15.0, 180.0, 95.0)
			grp.SetPerspective(11.0, newScreenWidth/newScreenHeight, 1000.0, 3000.0)

			(x, y) = app.GetCursorPosition()
			grp.SetCursorPosition(x, y)

			chr.Deform()
			chr.Render()

			grp.RestoreViewport()
			grp.PopState()
			grp.SetInterfaceRenderState()

	def __init__(self, stream):
		ui.Window.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_SELECT, self)

		self.stream=stream
		self.slot = self.stream.GetCharacterSlot()

		self.openLoadingFlag = False
		self.startIndex = -1
		self.startReservingTime = 0

		self.flagDict = {}
		self.curRotation = []
		self.destRotation = []

		self.curNameAlpha = []
		self.destNameAlpha = []
		for i in xrange(self.CHARACTER_TYPE_COUNT):
			self.curNameAlpha.append(0.0)
			self.destNameAlpha.append(0.0)

		self.curGauge = [0.0, 0.0, 0.0, 0.0]
		self.destGauge = [0.0, 0.0, 0.0, 0.0]

		self.dlgBoard = 0
		self.changeNameFlag = False
		self.nameInputBoard = None
		self.sendedChangeNamePacket = False

		self.startIndex = -1
		self.isLoad = 0

	def __del__(self):
		ui.Window.__del__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_SELECT, 0)

	def Open(self):
		if not self.__LoadBoardDialog(uiScriptLocale.LOCALE_UISCRIPT_PATH + "selectcharacterwindow.py"):
			dbg.TraceError("SelectCharacterWindow.Open - __LoadScript Error")
			return

		if not self.__LoadQuestionDialog("uiscript/questiondialog.py"):
			return

		playerSettingModule.LoadGameData("INIT")

		self.InitCharacterBoard()

		self.btnStart.Enable()
		self.btnCreate.Enable()
		self.btnDelete.Enable()
		# self.btnExit.Enable()
		##self.btnMall.Enable()

		self.dlgBoard.Show()
		self.SetWindowName("SelectCharacterWindow")
		self.Show()

		if self.slot>=0:
			self.SelectSlot(self.slot)

		if musicInfo.selectMusic != "":
			snd.SetMusicVolume(systemSetting.GetMusicVolume())
			snd.FadeInMusic("BGM/"+musicInfo.selectMusic)

		app.SetCenterPosition(0.0, 0.0, 0.0)
		app.SetCamera(1550.0, 15.0, 180.0, 95.0)

		self.isLoad=1
		self.Refresh()

		if self.stream.isAutoSelect:
			chrSlot=self.stream.GetCharacterSlot()
			self.SelectSlot(chrSlot)
			self.StartGame()

		self.HideAllFlag()
		self.SetEmpire(net.GetEmpireID())

		app.ShowCursor()

	def Close(self):
		if musicInfo.selectMusic != "":
			snd.FadeOutMusic("BGM/"+musicInfo.selectMusic)

		self.stream.popupWindow.Close()

		if self.dlgBoard:
			self.dlgBoard.ClearDictionary()

		self.flagDict = {}
		self.dlgBoard = None
		self.btnStart = None
		self.btnCreate = None
		self.btnDelete = None
		# self.btnExit = None
		self.backGround = None
		self.logoType = None
		self.footerBg = None

		self.dlgQuestion.ClearDictionary()
		self.dlgQuestion = None
		self.dlgQuestionText = None
		self.dlgQuestionAcceptButton = None
		self.dlgQuestionCancelButton = None
		self.privateInputBoard = None
		self.nameInputBoard = None

		chr.DeleteInstance(0)
		chr.DeleteInstance(1)
		chr.DeleteInstance(2)
		chr.DeleteInstance(3)

		self.Hide()
		self.KillFocus()

		app.HideCursor()

	def SetEmpire(self, id):
		if self.flagDict.has_key(id):
			self.flagDict[id].Show()
		
	def HideAllFlag(self):
		for flag in self.flagDict.values():
			flag.Hide()

	def Refresh(self):
		if not self.isLoad:
			return

		indexArray = (3, 2, 1, 0)

		for index in indexArray:
			playTime=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_PLAYTIME)
			id=net.GetAccountCharacterSlotDataInteger(index, net.ACCOUNT_CHARACTER_SLOT_ID)
			race=net.GetAccountCharacterSlotDataInteger(index, net.ACCOUNT_CHARACTER_SLOT_RACE)
			form=net.GetAccountCharacterSlotDataInteger(index, net.ACCOUNT_CHARACTER_SLOT_FORM)
			name=net.GetAccountCharacterSlotDataString(index, net.ACCOUNT_CHARACTER_SLOT_NAME)
			level=net.GetAccountCharacterSlotDataInteger(index, net.ACCOUNT_CHARACTER_SLOT_LEVEL)
			hair=net.GetAccountCharacterSlotDataInteger(index, net.ACCOUNT_CHARACTER_SLOT_HAIR)
			valueHTH=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_HTH)
			valueINT=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_INT)
			valueSTR=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_STR)
			valueDEX=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_DEX)
			guildName=net.GetAccountCharacterSlotDataString(self.slot, net.ACCOUNT_CHARACTER_SLOT_GUILD_NAME)

			if id:
				self.MakeCharacter(index, id, name, race, form, hair)
				self.SelectSlot(index)

				if race == 0:
					race = "warrior-m"
				elif race == 4:
					race = "warrior-w"
				elif race == 1:
					race = "ninja-w"
				elif race == 5:
					race = "ninja-m"
				elif race == 2:
					race = "sura-m"
				elif race == 6:
					race = "sura-w"
				elif race == 3:
					race = "shamane-w"
				elif race == 7:
					race = "shamane-m"

				if index == 0:
					self.CharacterName01.SetText(uiScriptLocale.SELECT_CHARACTER_NAME_CHARACTER+": "+name)
					self.Characterlevel01.SetText(uiScriptLocale.SELECT_CHARACTER_LEVEL_CHARACTER+": "+str(level))
					self.CharacterRace01.SetPosition(5,-13)
					self.CharacterRace01.LoadImage(RESOURCE + "chars/icon-"+str(race)+".tga")
					self.CharacterRace01.Show()

					# Descriptions character section.
					self.CharacterNameDesc.SetText(str(name))
					self.CharacterLevelDesc.SetText(str(level))
					self.CharacterPlayTimeDesc.SetText(str(playTime)+"min")
					if guildName:
						self.CharacterGuildDesc.SetText(guildName)
					else:
						self.CharacterGuildDesc.SetText(localeInfo.SELECT_NOT_JOIN_GUILD)
					self.CharacterClassDesc.SetText(str(race))

				if index == 1:
					self.CharacterName02.SetText(uiScriptLocale.SELECT_CHARACTER_NAME_CHARACTER+": "+name)
					self.Characterlevel02.SetText(uiScriptLocale.SELECT_CHARACTER_LEVEL_CHARACTER+": "+str(level))
					self.CharacterRace02.SetPosition(5,-13)
					self.CharacterRace02.LoadImage(RESOURCE + "chars/icon-"+str(race)+".tga")
					self.CharacterRace02.Show()

					# Descriptions character section.
					self.CharacterNameDesc.SetText(str(name))
					self.CharacterLevelDesc.SetText(str(level))
					self.CharacterPlayTimeDesc.SetText(str(playTime)+"min")
					if guildName:
						self.CharacterGuildDesc.SetText(guildName)
					else:
						self.CharacterGuildDesc.SetText(localeInfo.SELECT_NOT_JOIN_GUILD)
					self.CharacterClassDesc.SetText(str(race))

				elif index == 2:
					self.CharacterName03.SetText(uiScriptLocale.SELECT_CHARACTER_NAME_CHARACTER+": "+name)
					self.Characterlevel03.SetText(uiScriptLocale.SELECT_CHARACTER_LEVEL_CHARACTER+": "+str(level))
					self.CharacterRace03.SetPosition(5,-13)
					self.CharacterRace03.LoadImage(RESOURCE + "chars/icon-"+str(race)+".tga")
					self.CharacterRace03.Show()

					# Descriptions character section.
					self.CharacterNameDesc.SetText(str(name))
					self.CharacterLevelDesc.SetText(str(level))
					self.CharacterPlayTimeDesc.SetText(str(playTime)+"min")
					if guildName:
						self.CharacterGuildDesc.SetText(guildName)
					else:
						self.CharacterGuildDesc.SetText(localeInfo.SELECT_NOT_JOIN_GUILD)
					self.CharacterClassDesc.SetText(str(race))

				elif index == 3:
					self.CharacterName04.SetText(uiScriptLocale.SELECT_CHARACTER_NAME_CHARACTER+": "+name)
					self.Characterlevel04.SetText(uiScriptLocale.SELECT_CHARACTER_LEVEL_CHARACTER+": "+str(level))
					self.CharacterRace04.SetPosition(5,-13)
					self.CharacterRace04.LoadImage(RESOURCE + "chars/icon-"+str(race)+".tga")
					self.CharacterRace04.Show()

					# Descriptions character section.
					self.CharacterNameDesc.SetText(str(name))
					self.CharacterLevelDesc.SetText(str(level))
					self.CharacterPlayTimeDesc.SetText(str(playTime)+"min")
					if guildName:
						self.CharacterGuildDesc.SetText(guildName)
					else:
						self.CharacterGuildDesc.SetText(localeInfo.SELECT_NOT_JOIN_GUILD)
					self.CharacterClassDesc.SetText(str(race))

		self.SelectSlot(self.slot)

	def GetCharacterSlotID(self, slotIndex):
		return net.GetAccountCharacterSlotDataInteger(slotIndex, net.ACCOUNT_CHARACTER_SLOT_ID)

	def __LoadQuestionDialog(self, fileName):
		self.dlgQuestion = ui.ScriptWindow()

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self.dlgQuestion, fileName)
		except:
			import exception
			exception.Abort("SelectCharacterWindow.LoadQuestionDialog.LoadScript")

		try:
			GetObject=self.dlgQuestion.GetChild
			self.dlgQuestionText=GetObject("message")
			self.dlgQuestionAcceptButton=GetObject("accept")
			self.dlgQuestionCancelButton=GetObject("cancel")
		except:
			import exception
			exception.Abort("SelectCharacterWindow.LoadQuestionDialog.BindObject")

		self.dlgQuestionText.SetText(localeInfo.SELECT_DO_YOU_DELETE_REALLY)
		self.dlgQuestionAcceptButton.SetEvent(ui.__mem_func__(self.RequestDeleteCharacter))
		self.dlgQuestionCancelButton.SetEvent(ui.__mem_func__(self.dlgQuestion.Hide))
		return 1

	def __LoadBoardDialog(self, fileName):
		self.dlgBoard = ui.ScriptWindow()

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self.dlgBoard, fileName)
		except:
			import exception
			exception.Abort("SelectCharacterWindow.LoadBoardDialog.LoadScript")

		try:
			GetObject=self.dlgBoard.GetChild

			self.btnStart		= GetObject("start_button")
			self.btnCreate		= GetObject("create_button")
			self.btnDelete		= GetObject("delete_button")
			# self.btnExit		= GetObject("exit_button")

			self.btnSlot01		= GetObject("slot_button_01")
			self.btnSlot02		= GetObject("slot_button_02")
			self.btnSlot03		= GetObject("slot_button_03")
			self.btnSlot04		= GetObject("slot_button_04")
			self.btnSlot01A		= GetObject("slot_button_01_active")
			self.btnSlot02A		= GetObject("slot_button_02_active")
			self.btnSlot03A		= GetObject("slot_button_03_active")
			self.btnSlot04A		= GetObject("slot_button_04_active")
			self.CharacterNameDesc		= GetObject("character_name_desc")
			self.CharacterLevelDesc		= GetObject("character_level_desc")
			self.CharacterPlayTimeDesc		= GetObject("character_playtime_desc")
			self.CharacterGuildDesc		= GetObject("character_guild_desc")
			self.CharacterClassDesc		= GetObject("character_class_desc")
			self.Characterlevel01		= GetObject("character_level_value_01")
			self.CharacterName01		= GetObject("character_name_value_01")
			self.CharacterRace01		= GetObject("character_raza_value_01")			
			self.Characterlevel02		= GetObject("character_level_value_02")
			self.CharacterName02		= GetObject("character_name_value_02")
			self.CharacterRace02		= GetObject("character_raza_value_02")
			self.Characterlevel03		= GetObject("character_level_value_03")
			self.CharacterName03		= GetObject("character_name_value_03")
			self.CharacterRace03		= GetObject("character_raza_value_03")
			self.Characterlevel04		= GetObject("character_level_value_04")
			self.CharacterName04		= GetObject("character_name_value_04")
			self.CharacterRace04		= GetObject("character_raza_value_04")
			self.Characterlevel01A		= GetObject("character_level_value_01_a")
			self.CharacterName01A		= GetObject("character_name_value_01_a")
			self.CharacterRace01A		= GetObject("character_raza_value_01_a")
			self.Characterlevel02A		= GetObject("character_level_value_02_a")
			self.CharacterName02A		= GetObject("character_name_value_02_a")
			self.CharacterRace02A		= GetObject("character_raza_value_02_a")
			self.Characterlevel03A		= GetObject("character_level_value_03_a")
			self.CharacterName03A		= GetObject("character_name_value_03_a")
			self.CharacterRace03A		= GetObject("character_raza_value_03_a")
			self.Characterlevel04A		= GetObject("character_level_value_04_a")
			self.CharacterName04A		= GetObject("character_name_value_04_a")
			self.CharacterRace04A		= GetObject("character_raza_value_04_a")

			self.GaugeList = []
			self.GaugeList.append(GetObject("gauge_hth"))
			self.GaugeList.append(GetObject("gauge_int"))
			self.GaugeList.append(GetObject("gauge_str"))
			self.GaugeList.append(GetObject("gauge_dex"))

			self.flagDict[net.EMPIRE_A] = GetObject("EmpireFlag_A")
			self.flagDict[net.EMPIRE_B] = GetObject("EmpireFlag_B")
			self.flagDict[net.EMPIRE_C] = GetObject("EmpireFlag_C")

			self.backGround = GetObject("BackGround")
			self.logoType = GetObject("logotype")
			# self.footerBg = GetObject("footer_bg")

		except:
			import exception
			exception.Abort("SelectCharacterWindow.LoadBoardDialog.BindObject")

		self.btnStart.SetEvent(ui.__mem_func__(self.StartGame))
		self.btnCreate.SetEvent(ui.__mem_func__(self.CreateCharacter))
		# self.btnExit.SetEvent(ui.__mem_func__(self.ExitSelect))
		self.btnSlot01.SetEvent(ui.__mem_func__(self.SelectSlot1))
		self.btnSlot02.SetEvent(ui.__mem_func__(self.SelectSlot2))
		self.btnSlot03.SetEvent(ui.__mem_func__(self.SelectSlot3))
		self.btnSlot04.SetEvent(ui.__mem_func__(self.SelectSlot4))

		self.btnSlot01.Show()
		self.btnSlot02.Show()
		self.btnSlot03.Show()
		self.btnSlot04.Show()
		self.btnSlot01A.Hide()
		self.btnSlot02A.Hide()
		self.btnSlot03A.Hide()
		self.btnSlot04A.Hide()

		if NOT_NEED_DELETE_CODE:
			self.btnDelete.SetEvent(ui.__mem_func__(self.PopupDeleteQuestion))
		else:
			self.btnDelete.SetEvent(ui.__mem_func__(self.InputPrivateCode))

		self.chrRenderer = self.CharacterRenderer()
		self.chrRenderer.SetParent(self.backGround)
		self.chrRenderer.Show()

		self.logotype = self.CharacterRenderer()
		self.logotype.SetParent(self.logoType)
		self.logotype.Show()

		# self.footerbg = self.CharacterRenderer()
		# self.footerbg.SetParent(self.footerBg)
		# self.footerbg.Show()

		return 1

	def MakeCharacter(self, index, id, name, race, form, hair):
		if 0 == id:
			return

		chr.CreateInstance(index)
		chr.SelectInstance(index)
		chr.SetVirtualID(index)
		chr.SetNameString(name)

		chr.SetRace(race)
		chr.SetArmor(form)
		chr.SetHair(hair)
		#if app.ENABLE_SASH_SYSTEM:
		#	chr.SetSash(sash)
		
		chr.Refresh()
		chr.SetMotionMode(chr.MOTION_MODE_GENERAL)
		chr.SetLoopMotion(chr.MOTION_INTRO_WAIT)

		chr.SetRotation(0.0)

	## Manage Slot
	def SelectSlot1(self):
		snd.PlaySound("sound/ui/click.wav")
		self.SelectSlot(0)

	def SelectSlot2(self):
		snd.PlaySound("sound/ui/click.wav")
		self.SelectSlot(1)

	def SelectSlot3(self):
		snd.PlaySound("sound/ui/click.wav")
		self.SelectSlot(2)

	def SelectSlot4(self):
		snd.PlaySound("sound/ui/click.wav")
		self.SelectSlot(3)

	## Manage Character
	def StartGame(self):

		if self.sendedChangeNamePacket:
			return

		if self.changeNameFlag:
			self.OpenChangeNameDialog()
			return

		if -1 != self.startIndex:
			return

		if musicInfo.selectMusic != "":
			snd.FadeLimitOutMusic("BGM/"+musicInfo.selectMusic, systemSetting.GetMusicVolume()*0.05)

		self.btnStart.SetUp()
		self.btnCreate.SetUp()
		self.btnDelete.SetUp()
		# self.btnExit.SetUp()

		self.btnStart.Disable()
		self.btnCreate.Disable()
		self.btnDelete.Disable()
		# self.btnExit.Disable()
		self.dlgQuestion.Hide()

		self.stream.SetCharacterSlot(self.slot)

		self.startIndex = self.slot
		self.startReservingTime = app.GetTime()

		for i in xrange(self.SLOT_COUNT):

			if False == chr.HasInstance(i):
				continue

			chr.SelectInstance(i)

			if i == self.slot:
				self.slot=self.slot
				chr.PushOnceMotion(chr.MOTION_INTRO_SELECTED, 0.1)
				continue

			chr.PushOnceMotion(chr.MOTION_INTRO_NOT_SELECTED, 0.1)

	def OpenChangeNameDialog(self):
		import uiCommon
		nameInputBoard = uiCommon.InputDialogWithDescription()
		nameInputBoard.SetTitle(localeInfo.SELECT_CHANGE_NAME_TITLE)
		nameInputBoard.SetAcceptEvent(ui.__mem_func__(self.AcceptInputName))
		nameInputBoard.SetCancelEvent(ui.__mem_func__(self.CancelInputName))
		nameInputBoard.SetMaxLength(chr.PLAYER_NAME_MAX_LEN)
		nameInputBoard.SetBoardWidth(200)
		nameInputBoard.SetDescription(localeInfo.SELECT_INPUT_CHANGING_NAME)
		nameInputBoard.Open()
		nameInputBoard.slot = self.slot
		self.nameInputBoard = nameInputBoard

	def OnChangeName(self, id, name):
		self.SelectSlot(id)
		self.sendedChangeNamePacket = False
		self.PopupMessage(localeInfo.SELECT_CHANGED_NAME)

	def AcceptInputName(self):
		changeName = self.nameInputBoard.GetText()
		if not changeName:
			return

		self.sendedChangeNamePacket = True
		net.SendChangeNamePacket(self.nameInputBoard.slot, changeName)
		return self.CancelInputName()

	def CancelInputName(self):
		self.nameInputBoard.Close()
		self.nameInputBoard = None
		return True

	def OnCreateFailure(self, type):
		self.sendedChangeNamePacket = False
		if 0 == type:
			self.PopupMessage(localeInfo.SELECT_CHANGE_FAILURE_STRANGE_NAME)
		elif 1 == type:
			self.PopupMessage(localeInfo.SELECT_CHANGE_FAILURE_ALREADY_EXIST_NAME)
		elif 100 == type:
			self.PopupMessage(localeInfo.SELECT_CHANGE_FAILURE_STRANGE_INDEX)

	def CreateCharacter(self):
		id = self.GetCharacterSlotID(self.slot)
		if 0==id:
			self.stream.SetCharacterSlot(self.slot)

			EMPIRE_MODE = 1

			if EMPIRE_MODE:
				if self.__AreAllSlotEmpty():
					self.stream.SetReselectEmpirePhase()
				else:
					self.stream.SetCreateCharacterPhase()

			else:
				self.stream.SetCreateCharacterPhase()

	def __AreAllSlotEmpty(self):
		for iSlot in xrange(self.SLOT_COUNT):
			if 0!=net.GetAccountCharacterSlotDataInteger(iSlot, net.ACCOUNT_CHARACTER_SLOT_ID):
				return 0
		return 1

	def PopupDeleteQuestion(self):
		id = self.GetCharacterSlotID(self.slot)
		if 0 == id:
			return

		self.dlgQuestion.Show()
		self.dlgQuestion.SetTop()

	def RequestDeleteCharacter(self):
		self.dlgQuestion.Hide()

		id = self.GetCharacterSlotID(self.slot)
		if 0 == id:
			self.PopupMessage(localeInfo.SELECT_EMPTY_SLOT)
			return

		net.SendDestroyCharacterPacket(self.slot, "1234567")
		self.PopupMessage(localeInfo.SELECT_DELEING)

	def InputPrivateCode(self):
		
		import uiCommon
		privateInputBoard = uiCommon.InputDialogWithDescription()
		privateInputBoard.SetTitle(localeInfo.INPUT_PRIVATE_CODE_DIALOG_TITLE)
		privateInputBoard.SetAcceptEvent(ui.__mem_func__(self.AcceptInputPrivateCode))
		privateInputBoard.SetCancelEvent(ui.__mem_func__(self.CancelInputPrivateCode))

		if ENABLE_ENGNUM_DELETE_CODE:
			pass
		else:
			privateInputBoard.SetNumberMode()

		privateInputBoard.SetSecretMode()
		privateInputBoard.SetMaxLength(7)
			
		privateInputBoard.SetBoardWidth(250)
		privateInputBoard.SetDescription(localeInfo.INPUT_PRIVATE_CODE_DIALOG_DESCRIPTION)
		privateInputBoard.Open()
		self.privateInputBoard = privateInputBoard

	def AcceptInputPrivateCode(self):
		privateCode = self.privateInputBoard.GetText()
		if not privateCode:
			return

		id = self.GetCharacterSlotID(self.slot)
		if 0 == id:
			self.PopupMessage(localeInfo.SELECT_EMPTY_SLOT)
			return

		net.SendDestroyCharacterPacket(self.slot, privateCode)
		self.PopupMessage(localeInfo.SELECT_DELEING)

		self.CancelInputPrivateCode()
		return True

	def CancelInputPrivateCode(self):
		self.privateInputBoard = None
		return True

	def OnDeleteSuccess(self, slot):
		self.PopupMessage(localeInfo.SELECT_DELETED)
		self.DeleteCharacter(slot)

	def OnDeleteFailure(self):
		self.PopupMessage(localeInfo.SELECT_CAN_NOT_DELETE)

	def DeleteCharacter(self, index):
		chr.DeleteInstance(index)
		self.SelectSlot(self.slot)
		if index == 0:
			self.Characterlevel01A.SetText("")
			self.CharacterName01A.SetText("")
			self.Characterlevel01.SetText("")
			self.CharacterName01.SetText("")
			self.CharacterRace01.Hide()
			self.CharacterRace01A.Hide()
		elif index == 1:
			self.Characterlevel02A.SetText("")
			self.CharacterName02A.SetText("")
			self.Characterlevel02.SetText("")
			self.CharacterName02.SetText("")
			self.CharacterRace02.Hide()
			self.CharacterRace02A.Hide()
		elif index == 2:
			self.Characterlevel03A.SetText("")
			self.CharacterName03A.SetText("")
			self.Characterlevel03.SetText("")
			self.CharacterName03.SetText("")
			self.CharacterRace03.Hide()
			self.CharacterRace03A.Hide()
		elif index == 3:
			self.Characterlevel04A.SetText("")
			self.CharacterName04A.SetText("")
			self.Characterlevel04.SetText("")
			self.CharacterName04.SetText("")
			self.CharacterRace04.Hide()
			self.CharacterRace04A.Hide()

	def ExitSelect(self):
		self.dlgQuestion.Hide()
	
		if LEAVE_BUTTON_FOR_POTAL:
			if app.loggined:
				self.stream.SetPhaseWindow(0)
			else:
				self.stream.setloginphase()
		else:
			self.stream.SetLoginPhase()

		self.Hide()

	def GetSlotIndex(self):
		return self.slot

	def DecreaseSlotIndex(self):
		slotIndex = (self.GetSlotIndex() - 1 + self.SLOT_COUNT) % self.SLOT_COUNT
		self.SelectSlot(slotIndex)

	def IncreaseSlotIndex(self):
		slotIndex = (self.GetSlotIndex() + 1) % self.SLOT_COUNT
		self.SelectSlot(slotIndex)

	def SelectSlot(self, index):

		if index < 0:
			return
		if index >= self.SLOT_COUNT:
			return

		chr.DeleteInstance(0)
		chr.DeleteInstance(1)
		chr.DeleteInstance(2)
		chr.DeleteInstance(3)

		self.slot = index

		chr.SelectInstance(self.slot)

		self.btnSlot01A.Hide()
		self.btnSlot02A.Hide()
		self.btnSlot03A.Hide()
		self.btnSlot04A.Hide()

		if self.slot == 0:
			self.btnSlot01A.Show()
		elif self.slot == 1:
			self.btnSlot02A.Show()
		elif self.slot == 2:
			self.btnSlot03A.Show()
		elif self.slot == 3:
			self.btnSlot04A.Show()

		id=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_ID)
		if 0 != id:

			self.btnStart.Show()
			self.btnDelete.Enable()
			self.btnCreate.Hide()
			self.CharacterNameDesc.Show()
			self.CharacterLevelDesc.Show()
			self.CharacterPlayTimeDesc.Show()
			self.CharacterGuildDesc.Show()
			self.CharacterClassDesc.Show()

			playTime=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_PLAYTIME)
			level=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_LEVEL)
			name=net.GetAccountCharacterSlotDataString(self.slot, net.ACCOUNT_CHARACTER_SLOT_NAME)
			race=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_RACE)
			form=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_FORM)
			hair=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_HAIR)
			valueHTH=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_HTH)
			valueINT=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_INT)
			valueSTR=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_STR)
			valueDEX=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_DEX)
			guildName=net.GetAccountCharacterSlotDataString(self.slot, net.ACCOUNT_CHARACTER_SLOT_GUILD_NAME)
			self.changeNameFlag=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_CHANGE_NAME_FLAG)

			job = chr.RaceToJob(race)
			if job >= 0 and job < self.CHARACTER_TYPE_COUNT:
				self.destNameAlpha[job] = 1.0

			if id:
				self.MakeCharacter(self.slot, id, name, race, form, hair)

			if race == 0:
				race = "warrior-m"
			elif race == 4:
				race = "warrior-w"
			elif race == 1:
				race = "ninja-w"
			elif race == 5:
				race = "ninja-m"
			elif race == 2:
				race = "sura-m"
			elif race == 6:
				race = "sura-w"
			elif race == 3:
				race = "shamane-w"
			elif race == 7:
				race = "shamane-m"

			if self.slot == 0:

				self.CharacterName01A.SetText(uiScriptLocale.SELECT_CHARACTER_NAME_CHARACTER+": "+name)
				self.Characterlevel01A.SetText(uiScriptLocale.SELECT_CHARACTER_LEVEL_CHARACTER+": "+str(level))
				self.CharacterRace01A.SetPosition(5,-13)
				self.CharacterRace01A.LoadImage(RESOURCE + "chars/icon-"+str(race)+".tga")
				self.CharacterRace01A.Show()

				# Descriptions character section.
				self.CharacterNameDesc.SetText(str(name))
				self.CharacterLevelDesc.SetText(str(level))
				self.CharacterPlayTimeDesc.SetText(str(playTime)+"min")
				if guildName:
					self.CharacterGuildDesc.SetText(guildName)
				else:
					self.CharacterGuildDesc.SetText(localeInfo.SELECT_NOT_JOIN_GUILD)
				self.CharacterClassDesc.SetText(str(race))

			if self.slot == 1:

				self.CharacterName02A.SetText(uiScriptLocale.SELECT_CHARACTER_NAME_CHARACTER+": "+name)
				self.Characterlevel02A.SetText(uiScriptLocale.SELECT_CHARACTER_LEVEL_CHARACTER+": "+str(level))
				self.CharacterRace02A.SetPosition(5,-13)
				self.CharacterRace02A.LoadImage(RESOURCE + "chars/icon-"+str(race)+".tga")
				self.CharacterRace02A.Show()

				# Descriptions character section.
				self.CharacterNameDesc.SetText(str(name))
				self.CharacterLevelDesc.SetText(str(level))
				self.CharacterPlayTimeDesc.SetText(str(playTime)+"min")
				if guildName:
					self.CharacterGuildDesc.SetText(guildName)
				else:
					self.CharacterGuildDesc.SetText(localeInfo.SELECT_NOT_JOIN_GUILD)
				self.CharacterClassDesc.SetText(str(race))

			elif self.slot == 2:

				self.CharacterName03A.SetText(uiScriptLocale.SELECT_CHARACTER_NAME_CHARACTER+": "+name)
				self.Characterlevel03A.SetText(uiScriptLocale.SELECT_CHARACTER_LEVEL_CHARACTER+": "+str(level))
				self.CharacterRace03A.SetPosition(5,-13)
				self.CharacterRace03A.LoadImage(RESOURCE + "chars/icon-"+str(race)+".tga")
				self.CharacterRace03A.Show()

				# Descriptions character section.
				self.CharacterNameDesc.SetText(str(name))
				self.CharacterLevelDesc.SetText(str(level))
				self.CharacterPlayTimeDesc.SetText(str(playTime)+"min")
				if guildName:
					self.CharacterGuildDesc.SetText(guildName)
				else:
					self.CharacterGuildDesc.SetText(localeInfo.SELECT_NOT_JOIN_GUILD)
				self.CharacterClassDesc.SetText(str(race))

			elif self.slot == 3:

				self.CharacterName04A.SetText(uiScriptLocale.SELECT_CHARACTER_LEVEL_CHARACTER+": "+name)
				self.Characterlevel04A.SetText(uiScriptLocale.SELECT_CHARACTER_SKILL_TOOLTIP_LEVEL+": "+str(level))
				self.CharacterRace04A.SetPosition(5,-13)
				self.CharacterRace04A.LoadImage(RESOURCE + "chars/icon-"+str(race)+".tga")
				self.CharacterRace04A.Show()

				# Descriptions character section.
				self.CharacterNameDesc.SetText(str(name))
				self.CharacterLevelDesc.SetText(str(level))
				self.CharacterPlayTimeDesc.SetText(str(playTime)+"min")
				if guildName:
					self.CharacterGuildDesc.SetText(guildName)
				else:
					self.CharacterGuildDesc.SetText(localeInfo.SELECT_NOT_JOIN_GUILD)
				self.CharacterClassDesc.SetText(str(race))

			statesSummary = float(valueHTH + valueINT + valueSTR + valueDEX)
			if statesSummary > 0.0:
				self.destGauge =	[
										float(valueHTH) / 90,
										float(valueINT) / 90,
										float(valueSTR) / 90,
										float(valueDEX) / 90,
									]

		else:
			
			self.InitCharacterBoard()

	def InitCharacterBoard(self):

		self.btnStart.Hide()
		self.btnDelete.Disable()
		self.btnCreate.Show()
		self.CharacterNameDesc.SetText(uiScriptLocale.SELECT_CHARACTER_NO_NAME_DESC)
		self.CharacterLevelDesc.SetText("0")
		self.CharacterPlayTimeDesc.SetText("0min")
		self.CharacterGuildDesc.SetText(uiScriptLocale.SELECT_CHARACTER_NO_GUILD_DESC)
		self.CharacterClassDesc.SetText(uiScriptLocale.SELECT_CHARACTER_NO_CLASS_DESC)

	## Event
	def OnKeyDown(self, key):

		if 1 == key:
			self.ExitSelect()
		if 2 == key:
			self.SelectSlot(0)
		if 3 == key:
			self.SelectSlot(1)
		if 4 == key:
			self.SelectSlot(2)

		if 28 == key:

			id = net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_ID)
			if 0 == id:
				self.CreateCharacter()

			else:
				self.StartGame()

		if 203 == key:
			self.slot = (self.GetSlotIndex() - 1 + self.SLOT_COUNT) % self.SLOT_COUNT
			self.SelectSlot(self.slot)
		if 205 == key:
			self.slot = (self.GetSlotIndex() + 1) % self.SLOT_COUNT
			self.SelectSlot(self.slot)

		return True

	def OnUpdate(self):
		chr.Update()

		for i in xrange(4):
			self.curGauge[i] += (self.destGauge[i] - self.curGauge[i]) / 10.0
			if abs(self.curGauge[i] - self.destGauge[i]) < 0.005:
				self.curGauge[i] = self.destGauge[i]
			self.GaugeList[i].SetPercentage(self.curGauge[i], 1.0)

		for i in xrange(self.SLOT_COUNT):

			if False == chr.HasInstance(i):
				continue

			chr.SelectInstance(i)

		if -1 != self.startIndex:

			if app.GetTime() - self.startReservingTime > 3.0:
				if False == self.openLoadingFlag:
					chrSlot=self.stream.GetCharacterSlot()
					net.DirectEnter(chrSlot)
					self.openLoadingFlag = True

					playTime=net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_PLAYTIME)

					import player
					player.SetPlayTime(playTime)
					import chat
					chat.Clear()

	def EmptyFunc(self):
		pass

	def PopupMessage(self, msg, func=0):
		if not func:
			func=self.EmptyFunc

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, func, localeInfo.UI_OK)

	def OnPressExitKey(self):
		self.ExitSelect()
		return True