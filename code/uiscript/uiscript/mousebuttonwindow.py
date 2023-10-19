import uiScriptLocale
import app

ROOT = "d:/ymir work/ui/game/taskbar/"
if app.ENABLE_WEREDNNBS_UIGAME:
	RESOURCE = "d:/ymir work/ui/gui/TaskBar/bottons/"

if app.ENABLE_WEREDNNBS_UIGAME:
	window = {
		"name" : "ButtonWindow",

		"x" : 0,
		"y" : 0,

		"width" : 14,
		"height" : 14 * 3,

		"children" :
		(
			{
				"name" : "button_move_and_attack",
				"type" : "button",

				"x" : 0,
				"y" : 0,

				"tooltip_text" : uiScriptLocale.MOUSEBUTTON_ATTACK,
				"tooltip_x" : -25,
				"tooltip_y" : 0,

				"default_image" : RESOURCE + "Mouse_Button_Attack_01.tga",
				"over_image" : RESOURCE + "Mouse_Button_Attack_02.tga",
				"down_image" : RESOURCE + "Mouse_Button_Attack_03.tga",
			},
			{
				"name" : "button_auto_attack",
				"type" : "button",

				"x" : 0,
				"y" : 14,

				"tooltip_text" : uiScriptLocale.MOUSEBUTTON_AUTO_ATTACK,
				"tooltip_x" : -25,
				"tooltip_y" : 0,

				"default_image" : RESOURCE + "Mouse_Button_Auto_Attack_01.tga",
				"over_image" : RESOURCE + "Mouse_Button_Auto_Attack_02.tga",
				"down_image" : RESOURCE + "Mouse_Button_Auto_Attack_03.tga",
			},
			{
				"name" : "button_camera",
				"type" : "button",

				"x" : 0,
				"y" : 14,

				"tooltip_text" : uiScriptLocale.MOUSEBUTTON_CAMERA,
				"tooltip_x" : -25,
				"tooltip_y" : 0,

				"default_image" : RESOURCE + "Mouse_Button_Camera_01.tga",
				"over_image" : RESOURCE + "Mouse_Button_Camera_02.tga",
				"down_image" : RESOURCE + "Mouse_Button_Camera_03.tga",
			},
		),
	}
else:
	window = {
		"name" : "ButtonWindow",

		"x" : 0,
		"y" : 0,

		"width" : 32,
		"height" : 32 * 3,

		"children" :
		(
			{
				"name" : "button_move_and_attack",
				"type" : "button",

				"x" : 0,
				"y" : 0,

				"tooltip_text" : uiScriptLocale.MOUSEBUTTON_ATTACK,
				"tooltip_x" : -40,
				"tooltip_y" : 9,

				"default_image" : ROOT + "Mouse_Button_Attack_01.sub",
				"over_image" : ROOT + "Mouse_Button_Attack_02.sub",
				"down_image" : ROOT + "Mouse_Button_Attack_03.sub",
			},
			{
				"name" : "button_auto_attack",
				"type" : "button",

				"x" : 0,
				"y" : 32,

				"tooltip_text" : uiScriptLocale.MOUSEBUTTON_AUTO_ATTACK,
				"tooltip_x" : -40,
				"tooltip_y" : 9,

				"default_image" : ROOT + "Mouse_Button_Auto_Attack_01.sub",
				"over_image" : ROOT + "Mouse_Button_Auto_Attack_02.sub",
				"down_image" : ROOT + "Mouse_Button_Auto_Attack_03.sub",
			},
			{
				"name" : "button_camera",
				"type" : "button",

				"x" : 0,
				"y" : 64,

				"tooltip_text" : uiScriptLocale.MOUSEBUTTON_CAMERA,
				"tooltip_x" : -40,
				"tooltip_y" : 9,

				"default_image" : ROOT + "Mouse_Button_Camera_01.sub",
				"over_image" : ROOT + "Mouse_Button_Camera_02.sub",
				"down_image" : ROOT + "Mouse_Button_Camera_03.sub",
			},
		),
	}