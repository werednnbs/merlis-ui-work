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

		"x" : (SCREEN_WIDTH  - 180) /2,
		"y" : (SCREEN_HEIGHT - 325) /2,

		"width" : 180,
		"height" : 325,

		"children" :
		(
			{
				"name" : "board",
				"type" : "board",
				"style" : ("attach",),

				"x" : 0,
				"y" : 0,

				"width" : 180,
				"height" : 325,

				"children" :
				(

					## Title
					{
						"name" : "TitleBar",
						"type" : "titlebar",
						"style" : ("attach",),

						"x" : 6,
						"y" : 7,

						"width" : 166,
						"color" : "yellow",

						"children" :
						(
							{ "name":"TitleName", "type":"text", "x":0, "y":3, "text":uiScriptLocale.SYSTEM_TITLE, "text_horizontal_align":"center", "horizontal_align" : "center" },
						),
					},
					{
						"name" : "change_ch_button",
						"type" : "button",

						"x" : 0,
						"y" : 17 + 34,

						"text" : "Hýzlý Kanal",

						"default_image" : "%s/bottons/btn-big-detail-normal.tga" % PATCH_COMMON,
						"over_image" : "%s/bottons/btn-big-detail-hover.tga" % PATCH_COMMON,
						"down_image" : "%s/bottons/btn-big-detail-press.tga" % PATCH_COMMON,

						"horizontal_align" : "center",
					},
					{
						"name" : "mall_button",
						"type" : "button",

						"x" : 0,
						"y" : 57 + 34,

						"text" : uiScriptLocale.SYSTEM_MALL,
						"text_color" : 0xffF8BF24,

						"default_image" : "%s/bottons/btn-big-detail-normal.tga" % PATCH_COMMON,
						"over_image" : "%s/bottons/btn-big-detail-hover.tga" % PATCH_COMMON,
						"down_image" : "%s/bottons/btn-big-detail-press.tga" % PATCH_COMMON,

						"horizontal_align" : "center",
					},

					{
						"name" : "system_option_button",
						"type" : "button",

						"x" : 0,
						"y" : 87 + 34,

						"text" : uiScriptLocale.SYSTEMOPTION_TITLE,

						"default_image" : "%s/bottons/btn-big-detail-normal.tga" % PATCH_COMMON,
						"over_image" : "%s/bottons/btn-big-detail-hover.tga" % PATCH_COMMON,
						"down_image" : "%s/bottons/btn-big-detail-press.tga" % PATCH_COMMON,

						"horizontal_align" : "center",
					},
					{
						"name" : "game_option_button",
						"type" : "button",

						"x" : 0,
						"y" : 117 + 34,

						"text" : uiScriptLocale.GAMEOPTION_TITLE,

						"default_image" : "%s/bottons/btn-big-detail-normal.tga" % PATCH_COMMON,
						"over_image" : "%s/bottons/btn-big-detail-hover.tga" % PATCH_COMMON,
						"down_image" : "%s/bottons/btn-big-detail-press.tga" % PATCH_COMMON,

						"horizontal_align" : "center",
					},
					{
						"name" : "change_button",
						"type" : "button",

						"x" : 0,
						"y" : 147 + 34,

						"text" : uiScriptLocale.SYSTEM_CHANGE,

						"default_image" : "%s/bottons/btn-big-detail-normal.tga" % PATCH_COMMON,
						"over_image" : "%s/bottons/btn-big-detail-hover.tga" % PATCH_COMMON,
						"down_image" : "%s/bottons/btn-big-detail-press.tga" % PATCH_COMMON,

						"horizontal_align" : "center",
					},
					{
						"name" : "logout_button",
						"type" : "button",

						"x" : 0,
						"y" : 177 + 34,

						"text" : uiScriptLocale.SYSTEM_LOGOUT,

						"default_image" : "%s/bottons/btn-big-detail-normal.tga" % PATCH_COMMON,
						"over_image" : "%s/bottons/btn-big-detail-hover.tga" % PATCH_COMMON,
						"down_image" : "%s/bottons/btn-big-detail-press.tga" % PATCH_COMMON,

						"horizontal_align" : "center",
					},
					{
						"name" : "exit_button",
						"type" : "button",

						"x" : 0,
						"y" : 217 + 34,

						"text" : uiScriptLocale.SYSTEM_EXIT,

						"default_image" : "%s/bottons/btn-big-detail-normal.tga" % PATCH_COMMON,
						"over_image" : "%s/bottons/btn-big-detail-hover.tga" % PATCH_COMMON,
						"down_image" : "%s/bottons/btn-big-detail-press.tga" % PATCH_COMMON,

						"horizontal_align" : "center",
					},
					{
						"name" : "cancel_button",
						"type" : "button",

						"x" : 0,
						"y" : 247 + 34,

						"text" : uiScriptLocale.CANCEL,

						"default_image" : "%s/bottons/btn-big-detail-normal.tga" % PATCH_COMMON,
						"over_image" : "%s/bottons/btn-big-detail-hover.tga" % PATCH_COMMON,
						"down_image" : "%s/bottons/btn-big-detail-press.tga" % PATCH_COMMON,

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

		"x" : (SCREEN_WIDTH  - 200) /2,
		"y" : (SCREEN_HEIGHT - 288) /2,

		"width" : 200,
		"height" : 288,

		"children" :
		(
			{
				"name" : "board",
				"type" : "thinboard",

				"x" : 0,
				"y" : 0,

				"width" : 200,
				"height" : 288,

				"children" :
				(
					{
						"name" : "change_ch_button",
						"type" : "button",

						"x" : 10,
						"y" : 17,

						"text" : "Hýzlý Kanal",

						"default_image" : ROOT + "XLarge_Button_01.sub",
						"over_image" : ROOT + "XLarge_Button_02.sub",
						"down_image" : ROOT + "XLarge_Button_03.sub",
						"disable_image" : ROOT + "XLarge_Button_03.sub",
					},
					{
						"name" : "mall_button",
						"type" : "button",

						"x" : 10,
						"y" : 57,

						"text" : uiScriptLocale.SYSTEM_MALL,
						"text_color" : 0xffF8BF24,

						"default_image" : ROOT + "XLarge_Button_02.sub",
						"over_image" : ROOT + "XLarge_Button_02.sub",
						"down_image" : ROOT + "XLarge_Button_02.sub",
					},

					{
						"name" : "system_option_button",
						"type" : "button",

						"x" : 10,
						"y" : 87,

						"text" : uiScriptLocale.SYSTEMOPTION_TITLE,

						"default_image" : ROOT + "XLarge_Button_01.sub",
						"over_image" : ROOT + "XLarge_Button_02.sub",
						"down_image" : ROOT + "XLarge_Button_03.sub",
					},
					{
						"name" : "game_option_button",
						"type" : "button",

						"x" : 10,
						"y" : 117,

						"text" : uiScriptLocale.GAMEOPTION_TITLE,

						"default_image" : ROOT + "XLarge_Button_01.sub",
						"over_image" : ROOT + "XLarge_Button_02.sub",
						"down_image" : ROOT + "XLarge_Button_03.sub",
					},
					{
						"name" : "change_button",
						"type" : "button",

						"x" : 10,
						"y" : 147,

						"text" : uiScriptLocale.SYSTEM_CHANGE,

						"default_image" : ROOT + "XLarge_Button_01.sub",
						"over_image" : ROOT + "XLarge_Button_02.sub",
						"down_image" : ROOT + "XLarge_Button_03.sub",
					},
					{
						"name" : "logout_button",
						"type" : "button",

						"x" : 10,
						"y" : 177,

						"text" : uiScriptLocale.SYSTEM_LOGOUT,

						"default_image" : ROOT + "XLarge_Button_01.sub",
						"over_image" : ROOT + "XLarge_Button_02.sub",
						"down_image" : ROOT + "XLarge_Button_03.sub",
					},
					{
						"name" : "exit_button",
						"type" : "button",

						"x" : 10,
						"y" : 217,

						"text" : uiScriptLocale.SYSTEM_EXIT,

						"default_image" : ROOT + "XLarge_Button_01.sub",
						"over_image" : ROOT + "XLarge_Button_02.sub",
						"down_image" : ROOT + "XLarge_Button_03.sub",
					},
					{
						"name" : "cancel_button",
						"type" : "button",

						"x" : 10,
						"y" : 247,

						"text" : uiScriptLocale.CANCEL,

						"default_image" : ROOT + "XLarge_Button_01.sub",
						"over_image" : ROOT + "XLarge_Button_02.sub",
						"down_image" : ROOT + "XLarge_Button_03.sub",
					},
				),
			},
		),
	}
