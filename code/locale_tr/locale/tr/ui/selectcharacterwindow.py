import uiScriptLocale
import dates
import ui

PATCH_SELECT = uiScriptLocale.LOCALE_UISCRIPT_PATH + "selectcharacterwindow"
PATCH_SELECT_BTNS = uiScriptLocale.LOCALE_UISCRIPT_PATH + "selectcharacterwindow/buttons"
PATCH_COMMON = ui.PATCH_COMMON

#SELECT HARACTER
TITLE_BOARD = uiScriptLocale.CHARACTER_INFO_TITLE
COPYRIGHT = uiScriptLocale.LOGIN_INTERFACE_COPYRIGHT

#Colors
COLOR_NORMAL = dates.COLOR_NORMAL
COLOR_HOVER = dates.COLOR_HOVER

DIFF_BTNS = 90
X_SPACE_BTNS = 25 - 5
Y_SPACE_BTNS = 156

window = {
	"name" : "SelectCharacterWindow",
	"x" : 0,
	"y" : 0,
	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,
	"children" :(

		{
			"name" : "BackGround", 
			"type" : "expanded_image",
			"x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image": "%s/background.tga" % PATCH_SELECT,
		},

		# bar-top
		{
			"name" : "BarTop",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 35,

			"rect" : (0.0, 0.0, float(SCREEN_WIDTH - 200) / 156.0, 0.0),

			"image": "%s/bar-top.tga" % PATCH_SELECT,
		},

		{
			"name" : "TallismTop",
			"type" : "image",

			"x" : 20,
			"y" : 25,

			"width" : 25,
			"height" : 53,

			"image": "%s/tallism-top.tga" % PATCH_SELECT,
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

			"image": "%s/logotype.tga" % PATCH_SELECT,
		},

		{
			"name" : "right-sec",
			"type" : "board",

			"width" : 260,
			"height" : 408,

			"x" : SCREEN_WIDTH - 280,
			"y" : 176,

			# "image" : PATCH_SELECT + "board-right.tga",

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
					"name" : "character_name",
					"type" : "text",

					"x" : 25,
					"y" : 47,

					"text" : uiScriptLocale.SELECT_CHARACTER_NAME_CHARACTER,
					"fontname" : "Arial:15",
					"text_horizontal_align" : "left",

					"color": COLOR_NORMAL,
				},

				{
					"name" : "character_name_desc",
					"type" : "text",

					"x" : 235,
					"y" : 47,

					"text" : "",
					"fontname" : "Arial:15",
					"text_horizontal_align" : "right",

					"color": COLOR_HOVER,
				},

				{
					"name" : "separator_medium",
					"type" : "image",

					"x" : 0,
					"y" : 47+17,

					"width" : 230,
					"height" : 13,

					"image": "%s/separator-medium.tga" % PATCH_COMMON,

					"horizontal_align" : "center",
				},

				{
					"name" : "character_guild",
					"type" : "text",

					"x" : 25,
					"y" : 47+30,

					"text" : uiScriptLocale.SELECT_CHARACTER_GUILD_CHARACTER,
					"fontname" : "Arial:15",
					"text_horizontal_align" : "left",

					"color": COLOR_NORMAL,

					# "r" : 0.7, "g" : 0.7, "b" : 0.7, "a" : 1,
				},

				{
					"name" : "character_guild_desc",
					"type" : "text",

					"x" : 235,
					"y" : 47+30,

					"text" : "",
					"fontname" : "Arial:15",
					"text_horizontal_align" : "right",

					"color": COLOR_HOVER,

					# "r" : 1, "g" : 1, "b" : 1, "a" : 1,
				},

				{
					"name" : "separator_medium",
					"type" : "image",

					"x" : 0,
					"y" : 47+30+17,

					"width" : 230,
					"height" : 13,

					"image": "%s/separator-medium.tga" % PATCH_COMMON,

					"horizontal_align" : "center",
				},

				{
					"name" : "character_playtime",
					"type" : "text",

					"x" : 25,
					"y" : 47+30*2,

					"text" : uiScriptLocale.SELECT_CHARACTER_PLAYTIME_CHARACTER,
					"fontname" : "Arial:15",
					"text_horizontal_align" : "left",

					"color": COLOR_NORMAL,

					# "r" : 0.7, "g" : 0.7, "b" : 0.7, "a" : 1,
				},

				{
					"name" : "character_playtime_desc",
					"type" : "text",

					"x" : 235,
					"y" : 47+30*2,

					"text" : "",
					"fontname" : "Arial:15",
					"text_horizontal_align" : "right",

					"color": COLOR_HOVER,

					# "r" : 1, "g" : 1, "b" : 1, "a" : 1,
				},

				{
					"name" : "separator_medium",
					"type" : "image",

					"x" : 0,
					"y" : 47+30*2+17,

					"width" : 230,
					"height" : 13,

					"image": "%s/separator-medium.tga" % PATCH_COMMON,

					"horizontal_align" : "center",
				},

				{
					"name" : "character_level",
					"type" : "text",

					"x" : 25,
					"y" : 47+30*3,

					"text" : uiScriptLocale.SELECT_CHARACTER_LEVEL_CHARACTER,
					"fontname" : "Arial:15",
					"text_horizontal_align" : "left",

					"color": COLOR_NORMAL,

					# "r" : 0.7, "g" : 0.7, "b" : 0.7, "a" : 1,
				},

				{
					"name" : "character_level_desc",
					"type" : "text",

					"x" : 235,
					"y" : 47+30*3,

					"text" : "",
					"fontname" : "Arial:15",
					"text_horizontal_align" : "right",

					"color": COLOR_HOVER,

					# "r" : 1, "g" : 1, "b" : 1, "a" : 1,
				},

				{
					"name" : "separator_medium",
					"type" : "image",

					"x" : 0,
					"y" : 47+30*3+17,

					"width" : 230,
					"height" : 13,

					"image": "%s/separator-medium.tga" % PATCH_COMMON,

					"horizontal_align" : "center",
				},

				{
					"name" : "character_empire",
					"type" : "text",

					"x" : 25,
					"y" : 47+30*4,

					"text" : uiScriptLocale.SELECT_CHARACTER_EMPIRE_CHARACTER,
					"fontname" : "Arial:15",
					"text_horizontal_align" : "left",

					"color": COLOR_NORMAL,

					# "r" : 0.7, "g" : 0.7, "b" : 0.7, "a" : 1,
				},

				{
					"name" : "EmpireFlag_A",
					"type" : "text",

					"x" : 235,
					"y" : 47+30*4,

					"text" : "Shinsoo",
					"fontname" : "Arial:15",
					"text_horizontal_align" : "right",

					"r" : 0.9, "g" : 0.1, "b" : 0.1, "a" : 1,
				},

				{
					"name" : "EmpireFlag_B",
					"type" : "text",

					"x" : 235,
					"y" : 47+30*4,

					"text" : "Chunjo",
					"fontname" : "Arial:15",
					"text_horizontal_align" : "right",

					"r" : 1, "g" : 1, "b" : 0, "a" : 1,
				},

				{
					"name" : "EmpireFlag_C",
					"type" : "text",

					"x" : 235,
					"y" : 47+30*4,

					"text" : "Jinno",
					"fontname" : "Arial:15",
					"text_horizontal_align" : "right",

					"r" : 0, "g" : 0.1, "b" : 1, "a" : 1,
				},

				{
					"name" : "separator_medium",
					"type" : "image",

					"x" : 0,
					"y" : 47+30*4+17,

					"width" : 230,
					"height" : 13,

					"image": "%s/separator-medium.tga" % PATCH_COMMON,

					"horizontal_align" : "center",
				},

				{
					"name" : "character_class",
					"type" : "text",

					"x" : 25,
					"y" : 47+30*5,

					"text" : uiScriptLocale.SELECT_CHARACTER_CLASS_CHARACTER,
					"fontname" : "Arial:15",
					"text_horizontal_align" : "left",

					"color": COLOR_NORMAL,

					# "r" : 0.7, "g" : 0.7, "b" : 0.7, "a" : 1,
				},

				{
					"name" : "character_class_desc",
					"type" : "text",

					"x" : 235,
					"y" : 47+30*5,

					"text" : "",
					"fontname" : "Arial:15",
					"text_horizontal_align" : "right",

					"color": COLOR_HOVER,

					# "r" : 1, "g" : 1, "b" : 1, "a" : 1,
				},

				{
					"name" : "separator_medium",
					"type" : "image",

					"x" : 0,
					"y" : 47+30*5+17,

					"width" : 230,
					"height" : 13,

					"image": "%s/separator-medium.tga" % PATCH_COMMON,

					"horizontal_align" : "center",
				},

				{
					"name" : "character_hth",
					"type" : "text",

					"x" : 0,
					"y" : 102+135,

					"children" :
					(
						{
							"name" : "gauge_hth",
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
					"name" : "character_int",
					"type" : "text",

					"x" : 0,
					"y" : 128+135,

					"children" :
					(
						{
							"name" : "gauge_int",
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
					"name" : "character_str",
					"type" : "text",

					"x" : 0,
					"y" : 154+135,

					"children" :
					(
						{
							"name" : "gauge_str",
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
					"name" : "character_dex",
					"type" : "text",

					"x" : 0,
					"y" : 180+135,

					"children" :
					(
						{
							"name" : "gauge_dex",
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

				{
					"name" : "delete_button",
					"type" : "button",

					"x" : 0,
					"y" : 62+29*10,

					"default_image" : "%s/bottons/btn-gen-normal.tga" % PATCH_COMMON,
					"over_image" 	: "%s/bottons/btn-gen-hover.tga" % PATCH_COMMON,
					"down_image" 	: "%s/bottons/btn-gen-press.tga" % PATCH_COMMON,

					"horizontal_align" : "center",

					"text" : uiScriptLocale.SELECT_DELETE,
				},

			),
		},

		{
			"name" : "left-sec",

			"width" : 350,
			"height" : 650,

			"x" : 0,
			"y" : 0,

			"horizontal_align" : "left",

			"children" :
			(

				# {
				# 	"name" : "title-select",
				# 	"type" : "image",

				# 	"x" : 32,
				# 	"y" : 3*52,

				# 	"image" : PATCH_SELECT + "title-select.tga",
				# },
				{
					"name" : "slot_button_01",
					"type" : "button",

					"x" : X_SPACE_BTNS,
					"y" : Y_SPACE_BTNS,

					"default_image" : "%s/slot_normal.tga" % PATCH_SELECT_BTNS,
					"over_image" : "%s/slot_hover.tga" % PATCH_SELECT_BTNS,
					"down_image" : "%s/slot_hover.tga" % PATCH_SELECT_BTNS,

					"children" :
					(
						{
							"name" : "character_name_value_01",
							"type" : "text",

							"x" : 95,
							"y" : 28+3,

							"text" : "",
							"text_horizontal_align" : "left",
							"fontname" : "Arial:16",

							# "r" : 0.7, "g" : 0.8, "b" : 0.9, "a" : 1,
							"color" : COLOR_HOVER,
						},
						{
							"name" : "character_level_value_01",
							"type" : "text",

							"x" : 95,
							"y" : 41+3,

							"text" : "",
							"fontname" : "Arial:14",

							# "r" : 0.7, "g" : 0.8, "b" : 0.9, "a" : 1,
							"color" : COLOR_HOVER,
						},
						{
							"name" : "character_raza_value_01",
							"type" : "image",

							"x" : 0,
							"y" : 0,
						},
					),
				},
				{
					"name" : "slot_button_01_active",
					"type" : "button",

					"x" : X_SPACE_BTNS,
					"y" : Y_SPACE_BTNS,

					"default_image" : "%s/slot_hover.tga" % PATCH_SELECT_BTNS,
					"over_image" : "%s/slot_hover.tga" % PATCH_SELECT_BTNS,
					"down_image" : "%s/slot_normal.tga" % PATCH_SELECT_BTNS,

					"children" :
					(
						{
							"name" : "character_name_value_01_a",
							"type" : "text",

							"x" : 95,
							"y" : 28+3,

							"text" : "",
							"text_horizontal_align" : "left",
							"fontname" : "Arial:16",

							# "r" : 0.7, "g" : 0.8, "b" : 0.9, "a" : 1,
							"color" : COLOR_HOVER,
						},
						{
							"name" : "character_level_value_01_a",
							"type" : "text",

							"x" : 95,
							"y" : 41+3,

							"text" : "",
							"fontname" : "Arial:14",

							# "r" : 0.7, "g" : 0.8, "b" : 0.9, "a" : 1,
							"color" : COLOR_HOVER,
						},
						{
							"name" : "character_raza_value_01_a",
							"type" : "image",

							"x" : 0,
							"y" : 0,
						},
					),
				},
				{
					"name" : "slot_button_02",
					"type" : "button",

					'x' : X_SPACE_BTNS,
					'y' : Y_SPACE_BTNS + DIFF_BTNS,
					
					"default_image" : "%s/slot_normal.tga" % PATCH_SELECT_BTNS,
					"over_image" : "%s/slot_hover.tga" % PATCH_SELECT_BTNS,
					"down_image" : "%s/slot_hover.tga" % PATCH_SELECT_BTNS,

					"children" :
					(
						{
							"name" : "character_name_value_02",
							"type" : "text",

							"x" : 95,
							"y" : 28+3,

							"text" : "",
							"text_horizontal_align" : "left",
							"fontname" : "Arial:16",

							# "r" : 0.7, "g" : 0.8, "b" : 0.9, "a" : 1,
							"color" : COLOR_HOVER,
						},
						{
							"name" : "character_level_value_02",
							"type" : "text",

							"x" : 95,
							"y" : 41+3,

							"text" : "",
							"fontname" : "Arial:14",

							# "r" : 0.7, "g" : 0.8, "b" : 0.9, "a" : 1,
							"color" : COLOR_HOVER,
						},
						{
							"name" : "character_raza_value_02",
							"type" : "image",

							"x" : 0,
							"y" : 0,
						},
					),
				},
				{
					"name" : "slot_button_02_active",
					"type" : "button",

					'x' : X_SPACE_BTNS,
					'y' : Y_SPACE_BTNS + DIFF_BTNS,

					"default_image" : "%s/slot_hover.tga" % PATCH_SELECT_BTNS,
					"over_image" : "%s/slot_hover.tga" % PATCH_SELECT_BTNS,
					"down_image" : "%s/slot_normal.tga" % PATCH_SELECT_BTNS,

					"children" :
					(
						{
							"name" : "character_name_value_02_a",
							"type" : "text",

							"x" : 95,
							"y" : 28+3,

							"text" : "",
							"text_horizontal_align" : "left",
							"fontname" : "Arial:16",

							# "r" : 0.7, "g" : 0.8, "b" : 0.9, "a" : 1,

							"color" : COLOR_HOVER,
						},
						{
							"name" : "character_level_value_02_a",
							"type" : "text",

							"x" : 95,
							"y" : 41+3,

							"text" : "",
							"fontname" : "Arial:14",

							# "r" : 0.7, "g" : 0.8, "b" : 0.9, "a" : 1,

							"color" : COLOR_HOVER,
						},
						{
							"name" : "character_raza_value_02_a",
							"type" : "image",

							"x" : 0,
							"y" : 0,
						},
					),
				},
				{
					"name" : "slot_button_03",
					"type" : "button",

					'x' : X_SPACE_BTNS,
					'y' : Y_SPACE_BTNS + 2*DIFF_BTNS,

					"default_image" : "%s/slot_normal.tga" % PATCH_SELECT_BTNS,
					"over_image" : "%s/slot_hover.tga" % PATCH_SELECT_BTNS,
					"down_image" : "%s/slot_hover.tga" % PATCH_SELECT_BTNS,

					"children" :
					(
						{
							"name" : "character_name_value_03",
							"type" : "text",

							"x" : 95,
							"y" : 28+3,

							"text" : "",
							"text_horizontal_align" : "left",
							"fontname" : "Arial:16",

							# "r" : 0.7, "g" : 0.8, "b" : 0.9, "a" : 1,
							"color" : COLOR_HOVER,
						},
						{
							"name" : "character_level_value_03",
							"type" : "text",

							"x" : 95,
							"y" : 41+3,

							"text" : "",
							"fontname" : "Arial:14",

							# "r" : 0.7, "g" : 0.8, "b" : 0.9, "a" : 1,
							"color" : COLOR_HOVER,
						},
						{
							"name" : "character_raza_value_03",
							"type" : "image",

							"x" : 0,
							"y" : 0,
						},
					),
				},
				{
					"name" : "slot_button_03_active",
					"type" : "button",

					'x' : X_SPACE_BTNS,
					'y' : Y_SPACE_BTNS + 2*DIFF_BTNS,

					"default_image" : "%s/slot_hover.tga" % PATCH_SELECT_BTNS,
					"over_image" : "%s/slot_hover.tga" % PATCH_SELECT_BTNS,
					"down_image" : "%s/slot_normal.tga" % PATCH_SELECT_BTNS,

					"children" :
					(
						{
							"name" : "character_name_value_03_a",
							"type" : "text",

							"x" : 95,
							"y" : 28+3,

							"text" : "",
							"text_horizontal_align" : "left",
							"fontname" : "Arial:16",

							# "r" : 0.7, "g" : 0.8, "b" : 0.9, "a" : 1,
							"color" : COLOR_HOVER,
						},
						{
							"name" : "character_level_value_03_a",
							"type" : "text",

							"x" : 95,
							"y" : 41+3,

							"text" : "",
							"fontname" : "Arial:14",

							# "r" : 0.7, "g" : 0.8, "b" : 0.9, "a" : 1,
							"color" : COLOR_HOVER,
						},
						{
							"name" : "character_raza_value_03_a",
							"type" : "image",

							"x" : 0,
							"y" : 0,
						},
					),
				},
				{
					"name" : "slot_button_04",
					"type" : "button",
					
					'x' : X_SPACE_BTNS,
					'y' : Y_SPACE_BTNS + 3*DIFF_BTNS,
					
					"default_image" : "%s/slot_normal.tga" % PATCH_SELECT_BTNS,
					"over_image" : "%s/slot_hover.tga" % PATCH_SELECT_BTNS,
					"down_image" : "%s/slot_hover.tga" % PATCH_SELECT_BTNS,

					"children" :
					(
						{
							"name" : "character_name_value_04",
							"type" : "text",

							"x" : 95,
							"y" : 28+3,

							"text" : "",
							"text_horizontal_align" : "left",
							"fontname" : "Arial:16",

							# "r" : 0.7, "g" : 0.8, "b" : 0.9, "a" : 1,
							"color" : COLOR_HOVER,
						},
						{
							"name" : "character_level_value_04",
							"type" : "text",

							"x" : 95,
							"y" : 41+3,

							"text" : "",
							"fontname" : "Arial:14",

							# "r" : 0.7, "g" : 0.8, "b" : 0.9, "a" : 1,
							"color" : COLOR_HOVER,
						},
						{
							"name" : "character_raza_value_04",
							"type" : "image",

							"x" : 0,
							"y" : 0,
						},
					),
				},
				{
					"name" : "slot_button_04_active",
					"type" : "button",

					'x' : X_SPACE_BTNS,
					'y' : Y_SPACE_BTNS + 3*DIFF_BTNS,
					
					"default_image" : "%s/slot_hover.tga" % PATCH_SELECT_BTNS,
					"over_image" : "%s/slot_hover.tga" % PATCH_SELECT_BTNS,
					"down_image" : "%s/slot_normal.tga" % PATCH_SELECT_BTNS,

					"children" :
					(
						{
							"name" : "character_name_value_04_a",
							"type" : "text",

							"x" : 95,
							"y" : 28+3,

							"text" : "",
							"text_horizontal_align" : "left",
							"fontname" : "Arial:16",

							# "r" : 0.7, "g" : 0.8, "b" : 0.9, "a" : 1,
							"color" : COLOR_HOVER,
						},
						{
							"name" : "character_level_value_04_a",
							"type" : "text",

							"x" : 95,
							"y" : 41+3,

							"text" : "",
							"fontname" : "Arial:14",

							# "r" : 0.7, "g" : 0.8, "b" : 0.9, "a" : 1,
							"color" : COLOR_HOVER,
						},
						{
							"name" : "character_raza_value_04_a",
							"type" : "image",

							"x" : 0,
							"y" : 0,
						},
					),
				},

			),

		},
		# {
		# 	"name" : "exit_button",
		# 	"type" : "button",

		# 	"x" : 72,
		# 	"y" : SCREEN_HEIGHT - 68,

		# 	"default_image" : "%s/bottons/btn-gen-normal.tga" % PATCH_COMMON,
		# 	"over_image" 	: "%s/bottons/btn-gen-hover.tga" % PATCH_COMMON,
		# 	"down_image" 	: "%s/bottons/btn-gen-press.tga" % PATCH_COMMON,

		# 	"horizontal_align" : "center",

		# 	"text" : uiScriptLocale.SELECT_DELETE,
		# },
		{
			"name" : "start_button",
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