import uiScriptLocale
import dates
import ui

# ROOT_PATH = "d:/ymir work/ui/public/"
RESOURCE = uiScriptLocale.LOCALE_UISCRIPT_PATH + "selectempirewindow/"
PATCH_EMPIRE = uiScriptLocale.LOCALE_UISCRIPT_PATH + "selectempirewindow"
PATCH_COMMON = ui.PATCH_COMMON

#SELECT HARACTER
TITLE_BOARD = uiScriptLocale.SELECT_EMPIRE_TITLE
COPYRIGHT = uiScriptLocale.LOGIN_INTERFACE_COPYRIGHT

#Colors
COLOR_NORMAL = dates.COLOR_NORMAL
COLOR_HOVER = dates.COLOR_HOVER

window = {
	"name" : "SelectCharacterWindow",

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(

		## Board
		{
			"name" : "BackGround", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0, "y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image" : RESOURCE + "background.tga",
		},

		{
			"name" : "BarTop",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 35,

			"rect" : (0.0, 0.0, float(SCREEN_WIDTH - 200) / 156.0, 0.0),

			"image": "%s/bar-top.tga" % PATCH_EMPIRE,
		},

		{
			"name" : "TallismTop",
			"type" : "image",

			"x" : 20,
			"y" : 25,

			"width" : 25,
			"height" : 53,

			"image": "%s/tallism-top.tga" % PATCH_EMPIRE,
		},

		{
			"name" : "titleBoardTop",
			"type" : "text",

			"x" : 55,
			"y" : 44,

			"horizontal_align" : "left",
			"text_horizontal_align" : "left",
			
			"color": COLOR_HOVER,
			"text": TITLE_BOARD,

			"fontname" : "Tahoma:12",
		},
		{
			"name" : "board_A",
			"type" : "board",

			"width" : 210,
			"height" : 320,

			"x" : SCREEN_WIDTH/2 - 327,
			"y" : SCREEN_HEIGHT/2 - 160,

			"children" :
			(
				{
					"name" : "title_A",
					"type" : "text",

					"x" : 0,
					"y" : 22,

					"text" : "SHINSOO",
					"fontname" : "Arial:16",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",

					"color": 0xfffff5d4,
				},
				{
					"name" : "separator_medium",
					"type" : "image",

					"x" : 0,
					"y" : 45,

					"width" : 230,
					"height" : 13,

					"image": "%s/separator-medium.tga" % PATCH_COMMON,

					"horizontal_align" : "center",
				},
				{
					"name" : "flag_a",
					"type" : "image",

					"x" : 0,
					"y" : 75,

					"width" : 120,
					"height" : 60,

					"image": "%s/empire_flag/flag_a.tga" % PATCH_COMMON,

					"horizontal_align" : "center",
				},
				{
					"name" : "desc_a",
					"type" : "image",

					"x" : 0,
					"y" : 150,

					"width" : 120,
					"height" : 60,

					"image": "%s/description/desc_a.tga" % PATCH_EMPIRE,

					"horizontal_align" : "center",
				},
				{
					"name" : "EmpireArea_A",
					"type" : "radio_button",

					"x" : 0,
					"y" : 255,

					# "image" : RESOURCE + "bt-select-a-hover.tga",
					"default_image" : "%s/bottons/btn-gen-detail-normal.tga" % PATCH_COMMON,
					"over_image" 	: "%s/bottons/btn-gen-detail-hover.tga" % PATCH_COMMON,
					"down_image" 	: "%s/bottons/btn-gen-detail-hover.tga" % PATCH_COMMON,

					"horizontal_align" : "center",

					"text" : uiScriptLocale.EMPIRE_SELECT,
				},
			),
		},

		{
			"name" : "board_B",
			"type" : "board",

			"width" : 210,
			"height" : 320,

			"x" : SCREEN_WIDTH/2 - 104,
			"y" : SCREEN_HEIGHT/2 - 160,

			"children" :
			(
				{
					"name" : "title_B",
					"type" : "text",

					"x" : 0,
					"y" : 22,

					"text" : "CHUNJO",
					"fontname" : "Arial:16",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",

					"color": 0xfffff5d4,
				},
				{
					"name" : "separator_medium",
					"type" : "image",

					"x" : 0,
					"y" : 45,

					"width" : 230,
					"height" : 13,

					"image": "%s/separator-medium.tga" % PATCH_COMMON,

					"horizontal_align" : "center",
				},
				{
					"name" : "flag_b",
					"type" : "image",

					"x" : 0,
					"y" : 75,

					"width" : 120,
					"height" : 60,

					"image": "%s/empire_flag/flag_b.tga" % PATCH_COMMON,

					"horizontal_align" : "center",
				},
				{
					"name" : "desc_b",
					"type" : "image",

					"x" : 0,
					"y" : 150,

					"width" : 120,
					"height" : 60,

					"image": "%s/description/desc_b.tga" % PATCH_EMPIRE,

					"horizontal_align" : "center",
				},
				{
					"name" : "EmpireArea_B",
					"type" : "radio_button",

					"x" : 0,
					"y" : 255,

					"default_image" : "%s/bottons/btn-gen-detail-normal.tga" % PATCH_COMMON,
					"over_image" 	: "%s/bottons/btn-gen-detail-hover.tga" % PATCH_COMMON,
					"down_image" 	: "%s/bottons/btn-gen-detail-hover.tga" % PATCH_COMMON,

					"horizontal_align" : "center",

					"text" : uiScriptLocale.EMPIRE_SELECT,
				},
			),
		},

		{
			"name" : "board_C",
			"type" : "board",

			"width" : 210,
			"height" : 320,

			"x" : SCREEN_WIDTH/2 + 117,
			"y" : SCREEN_HEIGHT/2 - 160,

			"children" :
			(
				{
					"name" : "title_C",
					"type" : "text",

					"x" : 0,
					"y" : 22,

					"text" : "JINNO",
					"fontname" : "Arial:16",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",

					"color": 0xfffff5d4,
				},
				{
					"name" : "separator_medium",
					"type" : "image",

					"x" : 0,
					"y" : 45,

					"width" : 230,
					"height" : 13,

					"image": "%s/separator-medium.tga" % PATCH_COMMON,

					"horizontal_align" : "center",
				},
				{
					"name" : "flag_c",
					"type" : "image",

					"x" : 0,
					"y" : 75,

					"width" : 120,
					"height" : 60,

					"image": "%s/empire_flag/flag_c.tga" % PATCH_COMMON,

					"horizontal_align" : "center",
				},
				{
					"name" : "desc_c",
					"type" : "image",

					"x" : 0,
					"y" : 150,

					"width" : 120,
					"height" : 60,

					"image": "%s/description/desc_c.tga" % PATCH_EMPIRE,

					"horizontal_align" : "center",
				},
				{
					"name" : "EmpireArea_C",
					"type" : "radio_button",

					"x" : 0,
					"y" : 255,

					"horizontal_align" : "center",

					"default_image" : "%s/bottons/btn-gen-detail-normal.tga" % PATCH_COMMON,
					"over_image" 	: "%s/bottons/btn-gen-detail-hover.tga" % PATCH_COMMON,
					"down_image" 	: "%s/bottons/btn-gen-detail-hover.tga" % PATCH_COMMON,

					"text" : uiScriptLocale.EMPIRE_SELECT,
				},
			),
		},


		{
			"name" : "select_button",
			"type" : "button",

			"x" : 0,
			"y" : SCREEN_HEIGHT - 80,

			"default_image" : "%s/bottons/btn-gen-detail-normal.tga" % PATCH_COMMON,
			"over_image" 	: "%s/bottons/btn-gen-detail-hover.tga" % PATCH_COMMON,
			"down_image" 	: "%s/bottons/btn-gen-detail-press.tga" % PATCH_COMMON,

			"horizontal_align" : "center",

			"text" : uiScriptLocale.SELECT_SELECT,
		},
		{
			"name" : "titleBoardCopyright",
			"type" : "text",

			"x" : 0,
			"y" : SCREEN_HEIGHT - 30,

			"horizontal_align" : "center",
			"text_horizontal_align" : "center",
			
			"color": COLOR_NORMAL,
			"text": COPYRIGHT,

			"fontname" : "Tahoma:12",
		},
	),
}

