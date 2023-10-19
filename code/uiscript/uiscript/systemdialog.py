import uiScriptLocale
import app

if app.ENABLE_WEREDNNBS_UIGAME:
	import ui

ROOT = "d:/ymir work/ui/public/"
if app.ENABLE_WEREDNNBS_UIGAME:
	PATCH_COMMON = ui.PATCH_COMMON

if app.ENABLE_WEREDNNBS_UIGAME:
	window = {
		"name" : "SystemDialog",
		"style" : ("float",),

		"x" : SCREEN_WIDTH/2 - 100,
		"y" : SCREEN_HEIGHT/2 - 114,

		"width" : 200,
		"height" : 258,

		"children" :
		(
			{
				"name" : "board",
				"type" : "board",
				"style" : ("attach",),

				"x" : 0,
				"y" : 0,

				"width" : 200,
				"height" : 258,

				"children" :
				(

					## Title
					{
						"name" : "TitleBar",
						"type" : "titlebar",
						"style" : ("attach",),

						"x" : 8,
						"y" : 7,

						"width" : 185,
						"color" : "yellow",

						"children" :
						(
							{ "name":"TitleName", "type":"text", "x":77, "y":3, "text":uiScriptLocale.SYSTEM_TITLE, "text_horizontal_align":"center" },
						),
					},

					{
						"name" : "help_button",
						"type" : "button",

						"x" : 0,
						"y" : 17,

						"text" : uiScriptLocale.SYSTEM_HELP,

						"default_image" : "%s/btn-big-detail-normal.tga" % PATCH_COMMON,
						"over_image" : "%s/btn-big-detail-hover.tga" % PATCH_COMMON,
						"down_image" : "%s/btn-big-detail-press.tga" % PATCH_COMMON,

						"horizontal_align" : "center",
					},

					{
						"name" : "system_option_button",
						"type" : "button",

						"x" : 0,
						"y" : 57,

						"text" : uiScriptLocale.SYSTEMOPTION_TITLE,

						"default_image" : "%s/btn-big-detail-normal.tga" % PATCH_COMMON,
						"over_image" : "%s/btn-big-detail-hover.tga" % PATCH_COMMON,
						"down_image" : "%s/btn-big-detail-press.tga" % PATCH_COMMON,

						"horizontal_align" : "center",
					},
					{
						"name" : "game_option_button",
						"type" : "button",

						"x" : 0,
						"y" : 87,

						"text" : uiScriptLocale.GAMEOPTION_TITLE,

						"default_image" : "%s/btn-big-detail-normal.tga" % PATCH_COMMON,
						"over_image" : "%s/btn-big-detail-hover.tga" % PATCH_COMMON,
						"down_image" : "%s/btn-big-detail-press.tga" % PATCH_COMMON,

						"horizontal_align" : "center",
					},
					{
						"name" : "change_button",
						"type" : "button",

						"x" : 0,
						"y" : 117,

						"text" : uiScriptLocale.SYSTEM_CHANGE,

						"default_image" : "%s/btn-big-detail-normal.tga" % PATCH_COMMON,
						"over_image" : "%s/btn-big-detail-hover.tga" % PATCH_COMMON,
						"down_image" : "%s/btn-big-detail-press.tga" % PATCH_COMMON,

						"horizontal_align" : "center",
					},
					{
						"name" : "logout_button",
						"type" : "button",

						"x" : 0,
						"y" : 147,

						"text" : uiScriptLocale.SYSTEM_LOGOUT,

						"default_image" : "%s/btn-big-detail-normal.tga" % PATCH_COMMON,
						"over_image" : "%s/btn-big-detail-hover.tga" % PATCH_COMMON,
						"down_image" : "%s/btn-big-detail-press.tga" % PATCH_COMMON,

						"horizontal_align" : "center",
					},
					{
						"name" : "exit_button",
						"type" : "button",

						"x" : 0,
						"y" : 177,

						"text" : uiScriptLocale.SYSTEM_EXIT,

						"default_image" : "%s/btn-big-detail-normal.tga" % PATCH_COMMON,
						"over_image" : "%s/btn-big-detail-hover.tga" % PATCH_COMMON,
						"down_image" : "%s/btn-big-detail-press.tga" % PATCH_COMMON,

						"horizontal_align" : "center",
					},
					{
						"name" : "cancel_button",
						"type" : "button",

						"x" : 0,
						"y" : 217,

						"text" : uiScriptLocale.CANCEL,

						"default_image" : "%s/btn-big-detail-normal.tga" % PATCH_COMMON,
						"over_image" : "%s/btn-big-detail-hover.tga" % PATCH_COMMON,
						"down_image" : "%s/btn-big-detail-press.tga" % PATCH_COMMON,

						"horizontal_align" : "center",
					},
				),
			},
		),
	}
else:
	window = {
		"name" : "SystemDialog",
		"style" : ("float",),

		"x" : SCREEN_WIDTH/2 - 100,
		"y" : SCREEN_HEIGHT/2 - 114,

		"width" : 200,
		"height" : 258,

		"children" :
		(
			{
				"name" : "board",
				"type" : "thinboard",

				"x" : 0,
				"y" : 0,

				"width" : 200,
				"height" : 258,

				"children" :
				(
					{
						"name" : "help_button",
						"type" : "button",

						"x" : 10,
						"y" : 17,

						"text" : uiScriptLocale.SYSTEM_HELP,

						"default_image" : ROOT + "XLarge_Button_01.sub",
						"over_image" : ROOT + "XLarge_Button_02.sub",
						"down_image" : ROOT + "XLarge_Button_03.sub",
					},

					{
						"name" : "system_option_button",
						"type" : "button",

						"x" : 10,
						"y" : 57,

						"text" : uiScriptLocale.SYSTEMOPTION_TITLE,

						"default_image" : ROOT + "XLarge_Button_01.sub",
						"over_image" : ROOT + "XLarge_Button_02.sub",
						"down_image" : ROOT + "XLarge_Button_03.sub",
					},
					{
						"name" : "game_option_button",
						"type" : "button",

						"x" : 10,
						"y" : 87,

						"text" : uiScriptLocale.GAMEOPTION_TITLE,

						"default_image" : ROOT + "XLarge_Button_01.sub",
						"over_image" : ROOT + "XLarge_Button_02.sub",
						"down_image" : ROOT + "XLarge_Button_03.sub",
					},
					{
						"name" : "change_button",
						"type" : "button",

						"x" : 10,
						"y" : 117,

						"text" : uiScriptLocale.SYSTEM_CHANGE,

						"default_image" : ROOT + "XLarge_Button_01.sub",
						"over_image" : ROOT + "XLarge_Button_02.sub",
						"down_image" : ROOT + "XLarge_Button_03.sub",
					},
					{
						"name" : "logout_button",
						"type" : "button",

						"x" : 10,
						"y" : 147,

						"text" : uiScriptLocale.SYSTEM_LOGOUT,

						"default_image" : ROOT + "XLarge_Button_01.sub",
						"over_image" : ROOT + "XLarge_Button_02.sub",
						"down_image" : ROOT + "XLarge_Button_03.sub",
					},
					{
						"name" : "exit_button",
						"type" : "button",

						"x" : 10,
						"y" : 177,

						"text" : uiScriptLocale.SYSTEM_EXIT,

						"default_image" : ROOT + "XLarge_Button_01.sub",
						"over_image" : ROOT + "XLarge_Button_02.sub",
						"down_image" : ROOT + "XLarge_Button_03.sub",
					},
					{
						"name" : "cancel_button",
						"type" : "button",

						"x" : 10,
						"y" : 217,

						"text" : uiScriptLocale.CANCEL,

						"default_image" : ROOT + "XLarge_Button_01.sub",
						"over_image" : ROOT + "XLarge_Button_02.sub",
						"down_image" : ROOT + "XLarge_Button_03.sub",
					},
				),
			},
		),
	}
