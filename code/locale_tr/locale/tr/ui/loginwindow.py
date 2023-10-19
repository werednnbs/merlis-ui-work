import uiScriptLocale
import dates
import ui

#PATCHES
PATCH_LOGIN = uiScriptLocale.LOCALE_UISCRIPT_PATH + "loginwindow"
PATCH_COMMON = ui.PATCH_COMMON

#LOGIN Interface
SAVE_EMPTY = uiScriptLocale.LOGIN_INTERFACE_SAVE_EMPTY
TITLE_BOARD = uiScriptLocale.LOGIN_INTERFAE_TITLE_BOARD
COPYRIGHT = uiScriptLocale.LOGIN_INTERFACE_COPYRIGHT

#Colors
COLOR_NORMAL = dates.COLOR_NORMAL
COLOR_HOVER = dates.COLOR_HOVER

window = {
	"name" : "LoginWindow",
	"sytle" : ("movable",),

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "bg",
			"type" : "expanded_image",
			"x" : 0,
			"y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image": "%s/background.tga" % PATCH_LOGIN,
		},

		# bar-top
		{
			"name" : "BarTop",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 35,

			"rect" : (0.0, 0.0, float(SCREEN_WIDTH - 200) / 156.0, 0.0),

			"image": "%s/bar-top.tga" % PATCH_LOGIN,
		},

		{
			"name" : "TallismTop",
			"type" : "image",

			"x" : 20,
			"y" : 25,

			"width" : 25,
			"height" : 53,

			"image": "%s/tallism-top.tga" % PATCH_LOGIN,
		},

		# {
		# 	"name" : "DetailsTop",
		# 	"type" : "expanded_image",

		# 	"x" : 0,
		# 	"y" : 0,

		# 	"horizontal_align" : "center",

		# 	"image" : PATCH_LOGIN + "/bar-top-details.tga"
		# },

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
			"name" : "logotype",
			"type" : "expanded_image",

			"x" : SCREEN_WIDTH / 2 - 162,
			"y" : SCREEN_HEIGHT / 2 - 300,

			"image": "%s/logotype.tga" % PATCH_LOGIN,

			"width" : 325,
			"height" : 238,
		},

		{
			"name" : "bg-board",
			"type" : "expanded_image",
			
			"x" : SCREEN_WIDTH / 2 - 400,
			"y" : SCREEN_HEIGHT / 2 - 178,

			"image": "%s/bg-board.tga" % PATCH_LOGIN,

			"children" :
			(
				{
					"name" : "accountLog",
					# "type" : "expanded_image",
					"x" : 400,
					"y" : 239,

					"width" : 225,
					"height" : 88,

					# "image": "%s/option_board_3.tga" % PATCH_LOGIN,
					"children" :
					(
						{
							"name" : "bg_account_save_empty",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"image" : "%s/select-account-empty.tga" % PATCH_LOGIN,
						},
						{
							"name" : "bg_account_save_full_1",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"image" : "%s/select-account-full.tga" % PATCH_LOGIN,
						},
						{
							"name": "account_1",
							"type": "text",

							"x": 0+32,
							"y": 0+5,

							"color": COLOR_HOVER,
							"text": SAVE_EMPTY,
							"text_horizontal_align": "center",
						},
						{
							"name" : "bg_account_save_empty",
							"type" : "image",

							"x" : 71,
							"y" : 0,

							"image" : "%s/select-account-empty.tga" % PATCH_LOGIN,
						},
						{
							"name" : "bg_account_save_full_2",
							"type" : "image",

							"x" : 71,
							"y" : 0,

							"image" : "%s/select-account-full.tga" % PATCH_LOGIN,
						},
						{
							"name": "account_2",
							"type": "text",

							"x": 71+32,
							"y": 0+5,

							"color": COLOR_HOVER,
							"text": SAVE_EMPTY,
							"text_horizontal_align": "center",
						},
						{
							"name" : "bg_account_save_empty",
							"type" : "image",

							"x" : 142,
							"y" : 0,

							"image" : "%s/select-account-empty.tga" % PATCH_LOGIN,
						},
						{
							"name" : "bg_account_save_full_3",
							"type" : "image",

							"x" : 142,
							"y" : 0,

							"image" : "%s/select-account-full.tga" % PATCH_LOGIN,
						},
						{
							"name": "account_3",
							"type": "text",

							"x": 142+32,
							"y": 0+5,

							"color": COLOR_HOVER,
							"text": SAVE_EMPTY,
							"text_horizontal_align": "center",
						},
						{
							"name" : "bg_account_save_empty",
							"type" : "image",

							"x" : 0,
							"y" : 30,

							"image" : "%s/select-account-empty.tga" % PATCH_LOGIN,
						},
						{
							"name" : "bg_account_save_full_4",
							"type" : "image",

							"x" : 0,
							"y" : 30,

							"image" : "%s/select-account-full.tga" % PATCH_LOGIN,
						},
						{
							"name": "account_4",
							"type": "text",

							"x": 0+32,
							"y": 30+5,

							"color": COLOR_HOVER,
							"text": SAVE_EMPTY,
							"text_horizontal_align": "center",
						},
						{
							"name" : "bg_account_save_empty",
							"type" : "image",

							"x" : 71,
							"y" : 30,

							"image" : "%s/select-account-empty.tga" % PATCH_LOGIN,
						},
						{
							"name" : "bg_account_save_full_5",
							"type" : "image",

							"x" : 71,
							"y" : 30,

							"image" : "%s/select-account-full.tga" % PATCH_LOGIN,
						},
						{
							"name": "account_5",
							"type": "text",

							"x": 71+32,
							"y": 30+5,

							"color": COLOR_HOVER,
							"text": SAVE_EMPTY,
							"text_horizontal_align": "center",
						},
						{
							"name" : "bg_account_save_empty",
							"type" : "image",

							"x" : 142,
							"y" : 30,

							"image" : "%s/select-account-empty.tga" % PATCH_LOGIN,
						},
						{
							"name" : "bg_account_save_full_6",
							"type" : "image",

							"x" : 142,
							"y" : 30,

							"image" : "%s/select-account-full.tga" % PATCH_LOGIN,
						},
						{
							"name": "account_6",
							"type": "text",

							"x": 142+32,
							"y": 30+5,

							"color": COLOR_HOVER,
							"text": SAVE_EMPTY,
							"text_horizontal_align": "center",
						},
					),
				},

				{
					"name" : "channelBoard",

					"x" : 400,
					"y" : 163,

					"width" : 225,
					"height" : 88,
				},
				## Panel_Login
				{
					"name" : "LoginBoard",
					# "type" : "thinboard_login",

					"x" : 187,
					"y" : 157,

					"width" : 211,
					"height" : 171,

					"children" :
					(
						{
							"name": "id_editline_s",
							"type": "input",

							"x": 35,
							"y": 27,

							"width" : 155,
						},
						{
							"name": "pwd_editlines",
							"type": "input",

							"x": 35,
							"y": 60,

							"width" : 155,
						},
						{
							"name" : "LoginButton",
							"type" : "button",

							"x": 0,
							"y": 94,

							"text" : uiScriptLocale.LOGIN_INTERFACE_LOGIN,
							"text_color" : COLOR_HOVER,

							"text_horizontal_align" : "center",
							"horizontal_align" : "center",
			
							"default_image" : "%s/bottons/btn-gen-detail-normal.tga" % PATCH_COMMON,
							"over_image" 	: "%s/bottons/btn-gen-detail-hover.tga" % PATCH_COMMON,
							"down_image" 	: "%s/bottons/btn-gen-detail-press.tga" % PATCH_COMMON,
						},
						# {
						# 	"name" : "RegisterButton",
						# 	"type" : "button",

						# 	"x": 106,
						# 	"y": 165,

						# 	# "text" : uiScriptLocale.LOGIN_INTERFACE_LOGIN,
						# 	# "text_color" : COLOR_HOVER,

						# 	"default_image" : "%s/btn-register-normal.tga" % PATCH_LOGIN,
						# 	"over_image" : "%s/btn-register-over.tga" % PATCH_LOGIN,
						# 	"down_image" : "%s/btn-register-normal.tga" % PATCH_LOGIN,
						# },
					),
				},
				{
					"name" : "boardLang",

					"width" : 431,
					"height" : 32,

					"x" : 249,
					"y" : 325,
				},
			),
		},

		# # bar-top
		# {
		# 	"name" : "BarBottom",
		# 	"type" : "expanded_image",

		# 	"x" : 0,
		# 	"y" : SCREEN_HEIGHT-52,

		# 	"rect" : (0.0, 0.0, float(SCREEN_WIDTH - 800) / 156.0, 0.0),

		# 	"image" : PATCH_LOGIN + "/bar-bottom.tga"
		# },
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
