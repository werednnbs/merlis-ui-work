import uiScriptLocale
import dates
import ui

PATCH_CREATE = uiScriptLocale.LOCALE_UISCRIPT_PATH + "createcharacterwindow"
PATCH_CREATE_BTNS = uiScriptLocale.LOCALE_UISCRIPT_PATH + "createcharacterwindow/buttons"
PATCH_COMMON = ui.PATCH_COMMON

#SELECT HARACTER
TITLE_BOARD = uiScriptLocale.CHARACTER_INFO_TITLE
COPYRIGHT = uiScriptLocale.LOGIN_INTERFACE_COPYRIGHT

#Colors
COLOR_NORMAL = dates.COLOR_NORMAL
COLOR_HOVER = dates.COLOR_HOVER

# POSITIONS
DIFF_BTNS = 90
DIFF_BTNS_2 = 67
X_SPACE_BTNS = 64
Y_SPACE_BTNS = 73+35
X_SPACE_BTNS_2 = 73+93
Y_SPACE_BTNS_2 = 73+43

window = {
	"name" : "CreateCharacterWindow",

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(

		{
			"name" : "BackGround", 
			"type" : "expanded_image",
			"x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image": "%s/background.tga" % PATCH_CREATE,
			# "image" : RESOURCE + "background.tga",
		},

		{
			"name" : "BarTop",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 35,

			"rect" : (0.0, 0.0, float(SCREEN_WIDTH - 200) / 156.0, 0.0),

			"image": "%s/bar-top.tga" % PATCH_CREATE,
		},

		{
			"name" : "TallismTop",
			"type" : "image",

			"x" : 20,
			"y" : 25,

			"width" : 25,
			"height" : 53,

			"image": "%s/tallism-top.tga" % PATCH_CREATE,
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

		# {
		# 	"name" : "footer_bg",
		# 	"type" : "image",

		# 	"x" : SCREEN_WIDTH/2-266,
		# 	"y" : SCREEN_HEIGHT * (430) / 600,

		# 	"image": "%s/footer-bg.tga" % PATCH_SELECT,
		# },

		{
			"name" : "logotype",
			"type" : "image",

			"x" : SCREEN_WIDTH - 230,
			"y" : 50,

			"image": "%s/logotype.tga" % PATCH_CREATE,
		},

		{
			"name" : "right-sec",
			"type" : "board",

			"width" : 260,
			"height" : 368,

			"x" : SCREEN_WIDTH - 280,
			"y" : 176,

			# "image" : RESOURCE + "board-right.tga",

			"children" :
			(

				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : 245,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":3, "text":TITLE_BOARD, "text_horizontal_align":"center", "horizontal_align" : "center", },
					),
				},

				{
					"name" : "warrior-board",
					"type" : "image",

					"x" : 0,
					"y" : 38,
					"horizontal_align" : "center",

					"image": "%s/desc/warrior-board.tga" % PATCH_CREATE,
				},
				{
					"name" : "ninja-board",
					"type" : "image",

					"x" : 0,
					"y" : 38,

					"image": "%s/desc/ninja-board.tga" % PATCH_CREATE,

					"horizontal_align" : "center",
				},
				{
					"name" : "sura-board",
					"type" : "image",

					"x" : 0,
					"y" : 38,

					"image": "%s/desc/sura-board.tga" % PATCH_CREATE,

					"horizontal_align" : "center",
				},
				{
					"name" : "shamane-board",
					"type" : "image",

					"x" : 0,
					"y" : 38,

					"image": "%s/desc/shamane-board.tga" % PATCH_CREATE,
					"horizontal_align" : "center",
				},
				{
					"name" : "separator_medium",
					"type" : "image",

					"x" : 0,
					"y" : 102+115,

					"width" : 230,
					"height" : 13,

					"image": "%s/separator-medium.tga" % PATCH_COMMON,

					"horizontal_align" : "center",
				},
				{
					"name" : "hth",
					"type" : "text",

					"x" : 0,
					"y" : 102+135,

					"text" : "",

					"children" :
					(
						{
							"name" : "hth_gauge",
							"type" : "newgauge",

							"x" : 48,
							"y" : 4,

							"width" : 195,
							"color" : "red",
						},
						{
							"name" : "character_hth_value",
							"type" : "text",

							"x" : 25,
							"y" : 4,

							"text" : "VIT",
							"fontname" : "Arial:15",

							"text_horizontal_align" : "left",
						},
					),
				},
				{
					"name" : "int",
					"type" : "text",

					"x" : 0,
					"y" : 128+135,

					"text" : "",

					"children" :
					(
						{
							"name" : "int_gauge",
							"type" : "newgauge",

							"x" : 48,
							"y" : 4,

							"width" : 195,
							"color" : "red",
						},
						{
							"name" : "character_int_value",
							"type" : "text",

							"x" : 25,
							"y" : 4,

							"text" : "INT",
							"fontname" : "Arial:15",

							"text_horizontal_align" : "left",
						},
					),
				},
				{
					"name" : "str",
					"type" : "text",

					"x" : 0,
					"y" : 154+135,

					"text" : "",

					"children" :
					(
						{
							"name" : "str_gauge",
							"type" : "newgauge",

							"x" : 48,
							"y" : 4,

							"width" : 195,
							"color" : "red",
						},
						{
							"name" : "character_str_value",
							"type" : "text",

							"x" : 25,
							"y" : 4,

							"text" : "STR",
							"fontname" : "Arial:15",

							"text_horizontal_align" : "left",
						},
					),
				},
				{
					"name" : "dex",
					"type" : "text",

					"x" : 0,
					"y" : 180+135,

					"text" : "",

					"children" :
					(
						{
							"name" : "dex_gauge",
							"type" : "newgauge",

							"x" : 48,
							"y" : 4,

							"width" : 195,
							"color" : "red",
						},
						{
							"name" : "character_dex_value",
							"type" : "text",

							"x" : 25,
							"y" : 4,

							"text" : "DEX",
							"fontname" : "Arial:15",

							"text_horizontal_align" : "left",
						},
					),
				},
			),
		},
		{
			"name" : "left-sec",
			"type" : "image",

			"x" : 30,
			"y" : 100,

			"width" : 197,
			"height" : 424,

			"horizontal_align" : "left",

			# "image" : RESOURCE + "bg-left.tga",
			"image": "%s/bg-left.tga" % PATCH_CREATE,

			"children" :
			(

				{
					"name" : "character_name_value",
					"type" : "editline",

					"x" : 18,
					"y" : 13,

					"input_limit" : 16,

					"width" : 90,
					"height" : 20,
				},
				{
					"name" : "slot_01",
					"type" : "radio_button",

					'x' : X_SPACE_BTNS,
					'y' : Y_SPACE_BTNS,

					"text" : "",

					"default_image" : "%s/select-big-empty.tga" % PATCH_COMMON,
					"over_image"	: "%s/select-big-full.tga" % PATCH_COMMON,
					"down_image"	: "%s/select-big-full.tga" % PATCH_COMMON,
				},
				{
					"name" : "slot_02",
					"type" : "radio_button",

					'x' : X_SPACE_BTNS,
					'y' : Y_SPACE_BTNS + DIFF_BTNS,

					"text" : "",

					"default_image" : "%s/select-big-empty.tga" % PATCH_COMMON,
					"over_image"	: "%s/select-big-full.tga" % PATCH_COMMON,
					"down_image"	: "%s/select-big-full.tga" % PATCH_COMMON,
				},
				{
					"name" : "slot_03",
					"type" : "radio_button",

					'x' : X_SPACE_BTNS,
					'y' : Y_SPACE_BTNS + 2*DIFF_BTNS,

					"text" : "",

					"default_image" : "%s/select-big-empty.tga" % PATCH_COMMON,
					"over_image"	: "%s/select-big-full.tga" % PATCH_COMMON,
					"down_image"	: "%s/select-big-full.tga" % PATCH_COMMON,
				},
				{
					"name" : "slot_04",
					"type" : "radio_button",

					'x' : X_SPACE_BTNS,
					'y' : Y_SPACE_BTNS + 3*DIFF_BTNS,

					"text" : "",

					"default_image" : "%s/select-big-empty.tga" % PATCH_COMMON,
					"over_image"	: "%s/select-big-full.tga" % PATCH_COMMON,
					"down_image"	: "%s/select-big-full.tga" % PATCH_COMMON,
				},

				{
					"name" : "shape_button_01",
					"type" : "radio_button",

					'x' : X_SPACE_BTNS_2,
					'y' : Y_SPACE_BTNS_2 + 160,

					"text" : "",

					"default_image" : "%s/select-small-empty.tga" % PATCH_COMMON,
					"over_image"	: "%s/select-small-full.tga" % PATCH_COMMON,
					"down_image"	: "%s/select-small-full.tga" % PATCH_COMMON,
				},
				{
					"name" : "shape_button_02",
					"type" : "radio_button",

					'x' : X_SPACE_BTNS_2,
					'y' : Y_SPACE_BTNS_2 + DIFF_BTNS_2 + 160,

					"text" : "",

					"default_image" : "%s/select-small-empty.tga" % PATCH_COMMON,
					"over_image"	: "%s/select-small-full.tga" % PATCH_COMMON,
					"down_image"	: "%s/select-small-full.tga" % PATCH_COMMON,
				},
				{
					"name" : "gender_button_01",
					"type" : "radio_button",

					'x' : X_SPACE_BTNS_2,
					'y' : Y_SPACE_BTNS_2,

					"text" : "",

					"default_image" : "%s/select-small-empty.tga" % PATCH_COMMON,
					"over_image"	: "%s/select-small-full.tga" % PATCH_COMMON,
					"down_image"	: "%s/select-small-full.tga" % PATCH_COMMON,
				},
				{
					"name" : "gender_button_02",
					"type" : "radio_button",

					'x' : X_SPACE_BTNS_2,
					'y' : Y_SPACE_BTNS_2 + DIFF_BTNS_2,

					"text" : "",

					"default_image" : "%s/select-small-empty.tga" % PATCH_COMMON,
					"over_image"	: "%s/select-small-full.tga" % PATCH_COMMON,
					"down_image"	: "%s/select-small-full.tga" % PATCH_COMMON,
				},
			),
		},
		# {
		# 	"name" : "cancel_button",
		# 	"type" : "button",

		# 	"x" : 72,
		# 	"y" : SCREEN_HEIGHT - 68,

		# 	"default_image" : RESOURCE_BTNS + "bt-exit-normal.tga",
		# 	"over_image" 	: RESOURCE_BTNS + "bt-exit-hover.tga",
		# 	"down_image" 	: RESOURCE_BTNS + "bt-exit-normal.tga",

		# 	"horizontal_align" : "center",
		# },

		{
			"name" : "create_button",
			"type" : "button",

			"x" : 0,
			"y" : SCREEN_HEIGHT - 80,

			"default_image" : "%s/bottons/btn-gen-detail-normal.tga" % PATCH_COMMON,
			"over_image" 	: "%s/bottons/btn-gen-detail-hover.tga" % PATCH_COMMON,
			"down_image" 	: "%s/bottons/btn-gen-detail-press.tga" % PATCH_COMMON,

			"horizontal_align" : "center",

			"text" : uiScriptLocale.SELECT_CREATE,
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
