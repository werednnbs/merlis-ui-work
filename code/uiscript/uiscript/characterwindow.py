import uiScriptLocale
import app
if app.ENABLE_WEREDNNBS_UIGAME:
	import ui

QUEST_ICON_BACKGROUND = 'd:/ymir work/ui/game/quest/slot_base.sub'

SMALL_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_00.sub"
MIDDLE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_01.sub"
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_03.sub"
ICON_SLOT_FILE = "d:/ymir work/ui/gui/inventory/slot_base.tga"
FACE_SLOT_FILE = "d:/ymir work/ui/game/windows/box_face.sub"
ROOT_PATH = "d:/ymir work/ui/game/windows/"

LOCALE_PATH = uiScriptLocale.WINDOWS_PATH

if app.ENABLE_WEREDNNBS_UIGAME:
	PATCH_COMMON = ui.PATCH_COMMON

if app.ENABLE_WEREDNNBS_UIGAME:
	window = {
		"name" : "CharacterWindow",
		"style" : ("movable", "float",),

		"x" : 154,
		"y" : (SCREEN_HEIGHT - 37 - 361) / 2,

		"width" : 265,
		"height" : 361,

		"children" :
		(
			{
				"name" : "board",
				"type" : "board",
				"style" : ("attach",),

				"x" : 0,
				"y" : 0,

				"width" : 265,
				"height" : 361,

				"children" :
				(
					{
						"name" : "Character_TitleBar",
						"type" : "titlebar",
						"style" : ("attach",),

						"x" : 6,
						"y" : 7,

						"width" : 251,
						"color" : "red",

						"children" :
						(

							{ "name":"TitleName", "type":"text", "x":43, "y":2, "text":uiScriptLocale.CHARACTER_MAIN,"text_horizontal_align":"left,"},
							# { "name":"TitleName", "type":"image", "style" : ("attach",), "x":101, "y" : 1, "image" : LOCALE_PATH+"title_skill.sub", },

						),
					},
					{
						"name" : "Skill_TitleBar",
						"type" : "titlebar",
						"style" : ("attach",),

						"x" : 6,
						"y" : 7,

						"width" : 251,
						"color" : "red",

						"children" :
						(
							{ "name":"TitleName", "type":"text", "x":7, "y":2, "text":uiScriptLocale.CHARACTER_SKILL,"text_horizontal_align":"left,"},
							#{ "name":"TitleName", "type":"image", "style" : ("attach",), "x":101, "y" : 1, "image" : LOCALE_PATH+"title_skill.sub", },
						),
					},
					{
						"name" : "Emoticon_TitleBar",
						"type" : "titlebar",
						"style" : ("attach",),

						"x" : 6,
						"y" : 7,

						"width" : 251,
						"color" : "red",

						"children" :
						(
							{ "name":"TitleName", "type":"text", "x":7, "y":2, "text":uiScriptLocale.CHARACTER_ACTION,"text_horizontal_align":"left,"},
						),
					},
					{
						"name" : "Quest_TitleBar",
						"type" : "titlebar",
						"style" : ("attach",),

						"x" : 6,
						"y" : 7,

						"width" : 251,
						"color" : "red",

						"children" :
						(
							{ "name":"TitleName", "type":"text", "x":7, "y":2, "text":uiScriptLocale.CHARACTER_QUEST,"text_horizontal_align":"left,"},
						),
					},

					## Page Area
					{
						"name" : "Character_Page",
						"type" : "window",
						"style" : ("attach",),

						"x" : 1,
						"y" : 30,

						"width" : 265,
						"height" : 331,

						"children" :
						(

							## Guild Name Slot
							{
								"name" : "Guild_Name_Slot",
								"type" : "image",
								"x" : 141,
								"y" : 1,

								"width" : 97,
								"height" : 12,
								"image" : LOCALE_PATH+"slot_guild.sub",

								"children" :
								(
									{ "name":"TitleName", "type":"text", "x":8, "y":0, "text":uiScriptLocale.GUILD_INFO_NAME, "r":0.43137254, "g":0.43137254, "b":0.43137254, "a":1.0, "text_horizontal_align" : "left",},
									{ "name":"Guild_Name", "type":"text", "text":"길드 이름", "x":38, "y":0, "text_horizontal_align" : "left",},
								),
							},

							## Character Name Slot
							{
								"name" : "Character_Name_Slot",
								"type" : "image",
								"x" : 108,
								"y" : 2,

								"width" : 119,
								"height" : 14,
								"image" : LOCALE_PATH+"slot_name.sub",

								"children" :
								(
									{ "name":"TitleName", "type":"text", "x":8, "y":0, "text":uiScriptLocale.CREATE_NAME, "r":0.43137254, "g":0.43137254, "b":0.43137254, "a":1.0, "text_horizontal_align" : "left",},
									{ "name" : "Character_Name", "type":"text", "text":"캐릭터 이름", "x":35, "y":0, "text_horizontal_align" : "left",},
								),
							},

							## Face Slot
							{ "name" : "Face_Image", "type" : "image", "x" : -33, "y" : -70, "image" : "d:/ymir work/ui/gui/character/icon_warrior_m.tga" },
							##{ "name" : "Face_Slot", "type" : "image", "x" : -27, "y" : 7, "image" : FACE_SLOT_FILE, },

							## Header
							{ 
								"name":"Status_Header",
								"type":"image",

								"x": 0,
								"y": 30,

								"width":263,
								"height":41,

								"image":LOCALE_PATH+"label_header.sub",

								"children" :
								(

									# { "name":"Character_Bar_01_Text", "type" : "image", "x" : 0, "y" : 0, "image" : LOCALE_PATH+"label_std.sub", },
									# { "name":"Status_Header_Img", "type" : "image", "x" : 0, "y" : 30, "width" : 263, "height" : 39, "image" : LOCALE_PATH+"label_header.sub", },
									## Lv
									{
										"name":"Status_Lv", "type":"window", "x":0, "y":0, "width":59, "height":40, 
										"children" :
										(
											# { "name":"Level_Header", "type":"image", "x":0, "y":0, "image":LOCALE_PATH+"label_level.sub" },
											{ "name":"TitleName", "type":"text", "x":28, "y":15, "text":uiScriptLocale.CHARACTERWINDOW_LV, "r":0.43137254, "g":0.43137254, "b":0.43137254, "a":1.0, "text_horizontal_align" : "right",},
											{ "name":"Level_Value", "type":"text", "x":28, "y":13, "fontsize":"LARGE", "text":"999", "text_horizontal_align":"left" },
										),
									},

									## EXP
									{
										"name":"Status_CurExp", "type":"window", "x":61, "y":0, "width":100, "height":40,
										"children" :
										(
											##{ "name":"Exp_Slot", "type":"image", "x":0, "y":0, "image":LOCALE_PATH+"label_cur_exp.sub" },
											{ "name":"TitleName", "type":"text", "x":51, "y":6, "text":uiScriptLocale.CHARACTERWINDOW_EXP, "r":0.43137254, "g":0.43137254, "b":0.43137254, "a":1.0, "text_horizontal_align" : "center",},
											{ "name":"Exp_Value", "type":"text", "x":50, "y":19, "fontsize":"LARGE", "text":"12345678901", "text_horizontal_align":"center" },
										),
									},

									## REXP
									{
										"name":"Status_RestExp", "type":"window", "x":163, "y":0, "width":100, "height":40, 
										"children" :
										(
											##{ "name":"RestExp_Slot", "type":"image", "x":0, "y":0, "image":LOCALE_PATH+"label_last_exp.sub" },
											{ "name":"TitleName", "type":"text", "x":51, "y":6, "text":uiScriptLocale.CHARACTERWINDOW_EXP_NECESSARY, "r":0.43137254, "g":0.43137254, "b":0.43137254, "a":1.0, "text_horizontal_align" : "center",},
											{ "name":"RestExp_Value", "type":"text", "x":50, "y":19, "fontsize":"LARGE", "text":"12345678901", "text_horizontal_align":"center" },
										),
									},

									{
										"name" : "separator_medium",
										"type" : "image",

										"x" : 0,
										"y" : 35,

										"width" : 230,
										"height" : 13,

										"image": "%s/separator-medium.tga" % PATCH_COMMON,

										"horizontal_align" : "center",
									},

								),
							},
							## 기본 능력
							{
								"name":"Status_Standard", "type":"window", "x":0, "y":80, "width":263, "height":120,
								"children" :
								(

									## 기본 능력 제목
									##{ "name":"Character_Bar_01", "type":"horizontalbar", "x":12, "y":8, "width":223, },
									{ "name":"Character_Bar_01_Text", "type" : "image", "x" : 0, "y" : 0, "image" : LOCALE_PATH+"label_std.sub", },
									{ "name":"TitleName", "type":"text", "x":10, "y":5, "text":uiScriptLocale.CHARACTERWINDOW_STATUS, "text_horizontal_align" : "left",},

									## 기본 능력 아이템 리스트
									{"name":"Status_Standard_ItemList1", "type" : "image", "x": 9, "y":33, "image" : LOCALE_PATH+"label_std_item1.sub", },
									##{"name":"Status_Standard_ItemList2", "type" : "image", "x":100, "y":30, "image" : LOCALE_PATH+"label_std_item2.sub", },

									{ "name":"TitleName", "type":"text", "x":256, "y":5, "text":uiScriptLocale.CHARACTERWINDOW_AVAILABLE, "r":0.50588235, "g":0.61176470, "b":0.32941176, "a":1.0, "text_horizontal_align" : "right",},
									## 능력 수련 수치
									{ 
										"name":"Status_Plus_Label", 
										"type":"image", 
										"x":241, "y":5, 
										"image":LOCALE_PATH+"slot_empty.sub", 
										
										"children" :
										(
											{ "name":"Status_Plus_Value", "type":"text", "x":0, "y":0, "text":"99", "text_horizontal_align":"center", },
										),
									},

									{
										"name" : "separator_medium",
										"type" : "image",

										"x" : 0,
										"y" : 17,

										"width" : 230,
										"height" : 13,

										"image": "%s/separator-medium.tga" % PATCH_COMMON,

										"horizontal_align" : "center",
									},

									## HTH
									{
										"name":"HTH_Label", "type":"window", "x":35, "y":32, "width":60, "height":20,
										"children" :
										(
											##{ "name":"HTH_Slot", "type":"image", "x":0, "y":0, "image":SMALL_VALUE_FILE },
											{ "name":"HTH_Value", "type":"text", "x":18, "y":2, "text":"999", "text_horizontal_align":"center" },
											{ "name":"HTH_Plus", "type" : "button", "x":41, "y":2, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },
										),
									},
									## INT
									{
										"name":"INT_Label", "type":"window", "x":35, "y":32+20, "width":60, "height":20,
										"children" :
										(
											##{ "name":"INT_Slot", "type":"image", "x":0, "y":0, "image":SMALL_VALUE_FILE },
											{ "name":"INT_Value", "type":"text", "x":18, "y":2, "text":"999", "text_horizontal_align":"center" },
											{ "name":"INT_Plus", "type" : "button", "x" : 41, "y" : 2, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },
										)
									},
									## STR
									{
										"name":"STR_Label", "type":"window", "x":35, "y":32+20*2, "width":60, "height":20,
										"children" :
										(
											##{ "name":"STR_Slot", "type":"image", "x":0, "y":0, "image":SMALL_VALUE_FILE },
											{ "name":"STR_Value", "type":"text", "x":20, "y":2, "text":"999", "text_horizontal_align":"center" },
											{ "name":"STR_Plus", "type" : "button", "x" : 41, "y" : 2, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },
										)
									},
									## DEX
									{
										"name":"DEX_Label", "type":"window", "x":35, "y":32+20*3, "width":60, "height":20, 
										"children" :
										(
											##{ "name":"DEX_Slot", "type":"image", "x":0, "y":0, "image":SMALL_VALUE_FILE },
											{ "name":"DEX_Value", "type":"text", "x":20, "y":2, "text":"999", "text_horizontal_align":"center" },
											{ "name":"DEX_Plus", "type" : "button", "x" : 41, "y" : 2, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },
										)
									},

									{ "name":"HTH_Minus", "type" : "button", "x":9, "y":35, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },
									{ "name":"INT_Minus", "type" : "button", "x":9, "y":35+22, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },
									{ "name":"STR_Minus", "type" : "button", "x":9, "y":35+22*2, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },
									{ "name":"DEX_Minus", "type" : "button", "x":9, "y":35+22*3, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },

									####

									## HP
									{
										"name":"HEL_Label", "type":"window", "x":173, "y":32, "width":50, "height":20,
										"children" :
										(
											##{ "name":"HP_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
											{ "name":"HP_Value", "type":"text", "x":45, "y":2, "text":"9999/9999", "text_horizontal_align":"center" },
										),
									},
									## SP
									{
										"name":"SP_Label", "type":"window", "x":173, "y":32+20, "width":50, "height":20, 
										"children" :
										(
											##{ "name":"SP_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
											{ "name":"SP_Value", "type":"text", "x":45, "y":2, "text":"9999/9999", "text_horizontal_align":"center" },
										)
									},
									## ATT
									{
										"name":"ATT_Label", "type":"window", "x":173, "y":32+20*2, "width":50, "height":20, 
										"children" :
										(
											##{ "name":"ATT_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
											{ "name":"ATT_Value", "type":"text", "x":45, "y":2, "text":"999", "text_horizontal_align":"center" },
										),
									},
									## DEF
									{
										"name":"DEF_Label", "type":"window", "x":173, "y":32+20*3, "width":50, "height":20, 
										"children" :
										(
											##{ "name":"DEF_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
											{ "name":"DEF_Value", "type":"text", "x":45, "y":2, "text":"999", "text_horizontal_align":"center" },
										)
									},
								),
							},
							
							## 부가 능력
							{ 
								"name":"Status_Extent", "type":"window", "x":0, "y":200, "width":263, "height":50, 
								"children" :
								(

									## 부가 능력 제목
									##{ "name":"Status_Extent_Bar", "type":"horizontalbar", "x":12, "y":6, "width":223, },
									{ "name":"Status_Extent_Label", "type" : "image", "x" : 0, "y" : 0, "image" : LOCALE_PATH+"label_std.sub", },
									{ "name":"TitleName", "type":"text", "x":10, "y":5, "text":uiScriptLocale.CHARACTERWINDOW_ATTR, "text_horizontal_align" : "left",},
									
									{
										"name" : "separator_medium",
										"type" : "image",

										"x" : 0,
										"y" : 17,

										"width" : 230,
										"height" : 13,

										"image": "%s/separator-medium.tga" % PATCH_COMMON,

										"horizontal_align" : "center",
									},

									## 기본 능력 아이템 리스트
									#{"name":"Status_Extent_ItemList1", "type" : "image", "x":11, "y":31, "image" : LOCALE_PATH+"label_ext_item1.sub", },
									{"name":"Status_Extent_ItemList2", "type" : "image", "x": 9, "y":33, "image" : LOCALE_PATH+"label_ext_item2.sub", },

									## MSPD - 이동 속도
									{
										"name":"MOV_Label", "type":"window", "x":38, "y":33, "width":50, "height":20, 
										"children" :
										(
											##{ "name":"MSPD_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
											{ "name":"MSPD_Value", "type":"text", "x":26, "y":3, "text":"999", "text_horizontal_align":"center" },
										)
									},

									## ASPD - 공격 속도
									{
										"name":"ASPD_Label", "type":"window", "x":38, "y":33+20, "width":50, "height":20, 
										"children" :
										(
											##{ "name":"ASPD_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
											{ "name":"ASPD_Value", "type":"text", "x":26, "y":3, "text":"999", "text_horizontal_align":"center" },
										)
									},

									## CSPD - 주문 속도
									{
										"name":"CSPD_Label", "type":"window", "x":38, "y":33+20*2, "width":50, "height":20, 
										"children" :
										(
											##{ "name":"CSPD_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
											{ "name":"CSPD_Value", "type":"text", "x":26, "y":3, "text":"999", "text_horizontal_align":"center" },
										)
									},

									## MATT - 마법 공격력
									{
										"name":"MATT_Label", "type":"window", "x":192, "y":33, "width":50, "height":20, 
										"children" :
										(
											##{ "name":"MATT_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
											{ "name":"MATT_Value", "type":"text", "x":26, "y":3, "text":"999-999", "text_horizontal_align":"center" },
										)
									},

									## MDEF - 마법 방어력
									{
										"name":"MDEF_Label", "type":"window", "x":192, "y":33+20, "width":50, "height":20, 
										"children" :
										(
											##{ "name":"MDEF_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
											{ "name":"MDEF_Value", "type":"text", "x":26, "y":3, "text":"999", "text_horizontal_align":"center" },
										)
									},

									## 회피율
									{
										"name":"ER_Label", "type":"window", "x":192, "y":33+20*2, "width":50, "height":20, 
										"children" :
										(
											##{ "name":"ER_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
											{ "name":"ER_Value", "type":"text", "x":26, "y":3, "text":"999", "text_horizontal_align":"center" },
										)
									},

								),
							},
						),
					},
					{
						"name" : "Skill_Page",
						"type" : "window",
						"style" : ("attach",),

						"x" : 1,
						"y" : 30,

						"width" : 265,
						"height" : 331,

						"children" :
						(

							{
								"name":"Skill_Active_Title_Bar", "type":"horizontalbar", "x":0, "y":17, "width":263,

								"children" :
								(
									{ "name":"TitleName", "type":"text", "x":256, "y":5, "text":uiScriptLocale.CHARACTERWINDOW_AVAILABLE, "r":0.50588235, "g":0.61176470, "b":0.32941176, "a":1.0, "text_horizontal_align" : "right",},
									{ 
										"name":"Active_Skill_Point_Label", "x":176, "y":5,
										"children" :
										(
											{ "name":"Active_Skill_Point_Value", "type":"text", "x":67, "y":0, "text":"99", "text_horizontal_align":"center" },
										),
									},

									## Group Button
									{
										"name" : "Skill_Group_Button_1",
										"type" : "radio_button",

										"x" : 5,
										"y" : 2,

										"text" : "Group1",
										"text_color" : 0xFFFFE3AD,

										"default_image" : "d:/ymir work/ui/game/windows/skill_tab_button_01.sub",
										"over_image" : "d:/ymir work/ui/game/windows/skill_tab_button_02.sub",
										"down_image" : "d:/ymir work/ui/game/windows/skill_tab_button_03.sub",
									},

									{
										"name" : "Skill_Group_Button_2",
										"type" : "radio_button",

										"x" : 50,
										"y" : 2,

										"text" : "Group2",
										"text_color" : 0xFFFFE3AD,

										"default_image" : "d:/ymir work/ui/game/windows/skill_tab_button_01.sub",
										"over_image" : "d:/ymir work/ui/game/windows/skill_tab_button_02.sub",
										"down_image" : "d:/ymir work/ui/game/windows/skill_tab_button_03.sub",
									},

									{
										"name" : "Active_Skill_Group_Name",
										"type" : "text",

										"x" : 7,
										"y" : 1,
										"text" : "Active",

										"vertical_align" : "center",
										"text_vertical_align" : "center",
									},

								),
							},

							{
								"name":"Skill_ETC_Title_Bar", "type":"horizontalbar", "x":0, "y":193, "width":263,

								"children" :
								(
									{
										"name" : "Support_Skill_Group_Name",
										"type" : "text",

										"x" : 10,
										"y" : 3,
										"text" : uiScriptLocale.SKILL_SUPPORT_TITLE,

										"vertical_align" : "center",
										"text_vertical_align" : "center",
									},

									{ 
										"name":"Support_Skill_Point_Label", "type":"image", "x":145, "y":3, "image":LOCALE_PATH+"label_uppt.sub",
										"children" :
										(
											{ "name":"Support_Skill_Point_Value", "type":"text", "x":62, "y":0, "text":"99", "text_horizontal_align":"center" },
										),
									},
								),
							},
							##{ "name":"Skill_Board", "type":"image", "x":13, "y":38, "image":"d:/ymir work/ui/game/windows/skill_board.sub", },

							## Active Slot
							{
								"name" : "Skill_Active_Slot",
								"type" : "slot",

								"x" : 0 + 20,
								"y" : 0 + 15 + 32,

								"width" : 223,
								"height" : 223,
								"image" : ICON_SLOT_FILE,

								"slot" :	(
												{"index": 1, "x": 2, "y":  2, "width":32, "height":32},
												{"index":21, "x":39, "y":  2, "width":32, "height":32},
												{"index":41, "x":76, "y":  4, "width":32, "height":32},

												{"index": 3, "x": 2, "y": 38, "width":32, "height":32},
												{"index":23, "x":39, "y": 38, "width":32, "height":32},
												{"index":43, "x":76, "y": 38, "width":32, "height":32},

												{"index": 5, "x": 2, "y": 74, "width":32, "height":32},
												{"index":25, "x":39, "y": 74, "width":32, "height":32},
												{"index":45, "x":76, "y": 74, "width":32, "height":32},

												{"index": 7, "x": 2, "y":110, "width":32, "height":32},
												{"index":27, "x":39, "y":110, "width":32, "height":32},
												{"index":47, "x":76, "y":110, "width":32, "height":32},

												####

												{"index": 2, "x":114, "y":  2, "width":32, "height":32},
												{"index":22, "x":151, "y":  2, "width":32, "height":32},
												{"index":42, "x":188, "y":  2, "width":32, "height":32},

												{"index": 4, "x":114, "y": 38, "width":32, "height":32},
												{"index":24, "x":151, "y": 38, "width":32, "height":32},
												{"index":44, "x":188, "y": 38, "width":32, "height":32},

												{"index": 6, "x":114, "y": 74, "width":32, "height":32},
												{"index":26, "x":151, "y": 74, "width":32, "height":32},
												{"index":46, "x":188, "y": 74, "width":32, "height":32},

												{"index": 8, "x":114, "y":110, "width":32, "height":32},
												{"index":28, "x":151, "y":110, "width":32, "height":32},
												{"index":48, "x":188, "y":110, "width":32, "height":32},
											),
							},

							## ETC Slot
							{
								"name" : "Skill_ETC_Slot",
								"type" : "grid_table",
								"x" : 16 + 6,
								"y" : 223,
								"start_index" : 101,
								"x_count" : 6,
								"y_count" : 2,
								"x_step" : 32,
								"y_step" : 32,
								"x_blank" : 5,
								"y_blank" : 4,
								"image" : ICON_SLOT_FILE,
							},

						),
					},
					{
						"name" : "Emoticon_Page",
						"type" : "window",
						"style" : ("attach",),

						"x" : 1,
						"y" : 30,

						"width" : 265,
						"height" : 331,

						"children" :
						(
							## 기본 액션 제목
							{ "name":"Action_Bar", "type":"horizontalbar", "x":0, "y":17, "width":263, },
							{ "name":"Action_Bar_Text", "type":"text", "x":10, "y":22, "text":uiScriptLocale.CHARACTER_NORMAL_ACTION, },

							## Basis Action Slot
							{
								"name" : "SoloEmotionSlot",
								"type" : "grid_table",
								"x" : 20,
								"y" : 0 + 15 + 26 + 10,
								"horizontal_align" : "center",
								"start_index" : 1,
								"x_count" : 6,
								"y_count" : 3,
								"x_step" : 32,
								"y_step" : 32,
								"x_blank" : 6,
								"y_blank" : 4,
								"image" : ICON_SLOT_FILE,
							},

							## 상호 액션 제목
							{ "name":"Reaction_Bar", "type":"horizontalbar", "x":0, "y":170, "width":263, },
							{ "name":"Reaction_Bar_Text", "type":"text", "x":10, "y":175, "text":uiScriptLocale.CHARACTER_MUTUAL_ACTION, },

							## Reaction Slot
							{
								"name" : "DualEmotionSlot",
								"type" : "grid_table",
								"x" : 20,
								"y" : 200,
								"start_index" : 51,
								"x_count" : 6,
								"y_count" : 2,
								"x_step" : 32,
								"y_step" : 32,
								"x_blank" : 6,
								"y_blank" : 4,
								"image" : ICON_SLOT_FILE,
							},
						),
					},
					{
						"name" : "Quest_Page",
						"type" : "window",
						"style" : ("attach",),

						"x" : 1,
						"y" : 30,

						"width" : 265,
						"height" : 331,

						"children" :
						(
							{
								"name" : "Quest_Slot",
								"type" : "grid_table",
								"x" : 18,
								"y" : 18,
								"start_index" : 0,
								"x_count" : 1,
								"y_count" : 5,
								"x_step" : 32,
								"y_step" : 32,
								"y_blank" : 28,
								"image" : QUEST_ICON_BACKGROUND,
							},

							{
								"name" : "Quest_ScrollBar",
								"type" : "scrollbar",

								"x" : 25,
								"y" : 12,
								"size" : 290,
								"horizontal_align" : "right",
							},

							{ "name" : "Quest_Name_00", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 18, },
							{ "name" : "Quest_LastTime_00", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 34, "r":0.43137254, "g":0.43137254, "b":0.43137254, },
							{ "name" : "Quest_LastCount_00", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 50, "r":0.43137254, "g":0.43137254, "b":0.43137254, },

							{ "name" : "Quest_Name_01", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 78, },
							{ "name" : "Quest_LastTime_01", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 94, "r":0.43137254, "g":0.43137254, "b":0.43137254, },
							{ "name" : "Quest_LastCount_01", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 110, "r":0.43137254, "g":0.43137254, "b":0.43137254, },

							{ "name" : "Quest_Name_02", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 138, },
							{ "name" : "Quest_LastTime_02", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 154, "r":0.43137254, "g":0.43137254, "b":0.43137254, },
							{ "name" : "Quest_LastCount_02", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 170, "r":0.43137254, "g":0.43137254, "b":0.43137254, },

							{ "name" : "Quest_Name_03", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 198, },
							{ "name" : "Quest_LastTime_03", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 214, "r":0.43137254, "g":0.43137254, "b":0.43137254, },
							{ "name" : "Quest_LastCount_03", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 230, "r":0.43137254, "g":0.43137254, "b":0.43137254, },

							{ "name" : "Quest_Name_04", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 258, },
							{ "name" : "Quest_LastTime_04", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 274, "r":0.43137254, "g":0.43137254, "b":0.43137254, },
							{ "name" : "Quest_LastCount_04", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 290, "r":0.43137254, "g":0.43137254, "b":0.43137254, },

						),
					},

					## Tab Area
					{
						"name" : "TabControl",
						"type" : "window",

						"x" : 1,
						"y" : 331,

						"width" : 265,
						"height" : 30,

						"children" :
						(
							## Tab
							{
								"name" : "Tab_01",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 65,
								"height" : 30,

								"image" : LOCALE_PATH+"tab_1.sub",
							},
							{
								"name" : "Tab_02",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 65,
								"height" : 30,

								"image" : LOCALE_PATH+"tab_2.sub",
							},
							{
								"name" : "Tab_03",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 65,
								"height" : 30,

								"image" : LOCALE_PATH+"tab_3.sub",
							},
							{
								"name" : "Tab_04",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 65,
								"height" : 30,

								"image" : LOCALE_PATH+"tab_4.sub",
							},
							## RadioButton
							{
								"name" : "Tab_Button_01",
								"type" : "radio_button",

								"x" : 0,
								"y" : 0,

								"width" : 66,
								"height" : 30,
							},
							{
								"name" : "Tab_Button_02",
								"type" : "radio_button",

								"x" : 66,
								"y" : 0,

								"width" : 66,
								"height" : 30,
							},
							{
								"name" : "Tab_Button_03",
								"type" : "radio_button",

								"x" : 132,
								"y" : 0,

								"width" : 66,
								"height" : 30,
							},
							{
								"name" : "Tab_Button_04",
								"type" : "radio_button",

								"x" : 198,
								"y" : 0,

								"width" : 66,
								"height" : 30,
							},
						),
					},
				),
			},
		),
	}
else:
	window = {
		"name" : "CharacterWindow",
		"style" : ("movable", "float",),

		"x" : 24,
		"y" : (SCREEN_HEIGHT - 37 - 361) / 2,

		"width" : 253,
		"height" : 361,

		"children" :
		(
			{
				"name" : "board",
				"type" : "board",
				"style" : ("attach",),

				"x" : 0,
				"y" : 0,

				"width" : 253,
				"height" : 361,

				"children" :
				(
					{
						"name" : "Skill_TitleBar",
						"type" : "titlebar",
						"style" : ("attach",),

						"x" : 8,
						"y" : 7,

						"width" : 238,
						"color" : "red",

						"children" :
						(
							{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":uiScriptLocale.CHARACTER_SKILL, "all_align":"center" },
							#{ "name":"TitleName", "type":"image", "style" : ("attach",), "x":101, "y" : 1, "image" : LOCALE_PATH+"title_skill.sub", },
						),
					},
					{
						"name" : "Emoticon_TitleBar",
						"type" : "titlebar",
						"style" : ("attach",),

						"x" : 8,
						"y" : 7,

						"width" : 238,
						"color" : "red",

						"children" :
						(
							{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":uiScriptLocale.CHARACTER_ACTION, "all_align":"center" },
						),
					},
					{
						"name" : "Quest_TitleBar",
						"type" : "titlebar",
						"style" : ("attach",),

						"x" : 8,
						"y" : 7,

						"width" : 238,
						"color" : "red",

						"children" :
						(
							{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":uiScriptLocale.CHARACTER_QUEST, "all_align":"center" },
						),
					},

					## Tab Area
					{
						"name" : "TabControl",
						"type" : "window",

						"x" : 0,
						"y" : 328,

						"width" : 250,
						"height" : 31,

						"children" :
						(
							## Tab
							{
								"name" : "Tab_01",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 250,
								"height" : 31,

								"image" : LOCALE_PATH+"tab_1.sub",
							},
							{
								"name" : "Tab_02",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 250,
								"height" : 31,

								"image" : LOCALE_PATH+"tab_2.sub",
							},
							{
								"name" : "Tab_03",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 250,
								"height" : 31,

								"image" : LOCALE_PATH+"tab_3.sub",
							},
							{
								"name" : "Tab_04",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 250,
								"height" : 31,

								"image" : LOCALE_PATH+"tab_4.sub",
							},
							## RadioButton
							{
								"name" : "Tab_Button_01",
								"type" : "radio_button",

								"x" : 6,
								"y" : 5,

								"width" : 53,
								"height" : 27,
							},
							{
								"name" : "Tab_Button_02",
								"type" : "radio_button",

								"x" : 61,
								"y" : 5,

								"width" : 67,
								"height" : 27,
							},
							{
								"name" : "Tab_Button_03",
								"type" : "radio_button",

								"x" : 130,
								"y" : 5,

								"width" : 61,
								"height" : 27,
							},
							{
								"name" : "Tab_Button_04",
								"type" : "radio_button",

								"x" : 192,
								"y" : 5,

								"width" : 55,
								"height" : 27,
							},
						),
					},

					## Page Area
					{
						"name" : "Character_Page",
						"type" : "window",
						"style" : ("attach",),

						"x" : 0,
						"y" : 0,

						"width" : 250,
						"height" : 304,

						"children" :
						(

							## Title Area
							{
								"name" : "Character_TitleBar", "type" : "titlebar", "style" : ("attach",), "x" : 61, "y" : 7, "width" : 185, "color" : "red",
								"children" :
								(
									#{ "name" : "TitleName", "type" : "image", "style" : ("attach",), "x" : 70, "y" : 1, "image" : LOCALE_PATH+"title_status.sub", },
									{ "name" : "TitleName", "type":"text", "x":0, "y":-1, "text":uiScriptLocale.CHARACTER_MAIN, "all_align":"center" },
								),
							},

							## Guild Name Slot
							{
								"name" : "Guild_Name_Slot",
								"type" : "image",
								"x" : 60,
								"y" :27+7,
								"image" : LARGE_VALUE_FILE,

								"children" :
								(
									{
										"name" : "Guild_Name",
										"type":"text",
										"text":"길드 이름",
										"x":0,
										"y":0,
										"r":1.0,
										"g":1.0,
										"b":1.0,
										"a":1.0,
										"all_align" : "center",
									},
								),
							},

							## Character Name Slot
							{
								"name" : "Character_Name_Slot",
								"type" : "image",
								"x" : 153,
								"y" :27+7,
								"image" : LARGE_VALUE_FILE,

								"children" :
								(
									{
										"name" : "Character_Name",
										"type":"text",
										"text":"캐릭터 이름",
										"x":0,
										"y":0,
										"r":1.0,
										"g":1.0,
										"b":1.0,
										"a":1.0,
										"all_align" : "center",
									},
								),
							},

							## Header
							{ 
								"name":"Status_Header", "type":"window", "x":3, "y":31, "width":0, "height":0, 
								"children" :
								(
									## Lv
									{
										"name":"Status_Lv", "type":"window", "x":9, "y":30, "width":37, "height":42, 
										"children" :
										(
											{ "name":"Level_Header", "type":"image", "x":0, "y":0, "image":LOCALE_PATH+"label_level.sub" },
											{ "name":"Level_Value", "type":"text", "x":19, "y":19, "fontsize":"LARGE", "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										),
									},

									## EXP
									{
										"name":"Status_CurExp", "type":"window", "x":53, "y":30, "width":87, "height":42,
										"children" :
										(
											{ "name":"Exp_Slot", "type":"image", "x":0, "y":0, "image":LOCALE_PATH+"label_cur_exp.sub" },
											{ "name":"Exp_Value", "type":"text", "x":46, "y":19, "fontsize":"LARGE", "text":"12345678901", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },									),
									},

									## REXP
									{
										"name":"Status_RestExp", "type":"window", "x":150, "y":30, "width":50, "height":20, 
										"children" :
										(
											{ "name":"RestExp_Slot", "type":"image", "x":0, "y":0, "image":LOCALE_PATH+"label_last_exp.sub" },
											{ "name":"RestExp_Value", "type":"text", "x":46, "y":19, "fontsize":"LARGE", "text":"12345678901", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										),
									},
								),
							},

							## Face Slot
							{ "name" : "Face_Image", "type" : "image", "x" : 11, "y" : 11, "image" : "d:/ymir work/ui/game/windows/face_warrior.sub" },
							{ "name" : "Face_Slot", "type" : "image", "x" : 7, "y" : 7, "image" : FACE_SLOT_FILE, },

							## 기본 능력
							{
								"name":"Status_Standard", "type":"window", "x":3, "y":100, "width":200, "height":250,
								"children" :
								(
									## 기본 능력 제목
									{ "name":"Character_Bar_01", "type":"horizontalbar", "x":12, "y":8, "width":223, },
									{ "name":"Character_Bar_01_Text", "type" : "image", "x" : 13, "y" : 9, "image" : LOCALE_PATH+"label_std.sub", },
									
									## 능력 수련 수치
									{ 
										"name":"Status_Plus_Label", 
										"type":"image", 
										"x":150, "y":11, 
										"image":LOCALE_PATH+"label_uppt.sub", 
										
										"children" :
										(
											{ "name":"Status_Plus_Value", "type":"text", "x":62, "y":0, "text":"99", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										),
									},

									## 기본 능력 아이템 리스트
									{"name":"Status_Standard_ItemList1", "type" : "image", "x":17, "y":31, "image" : LOCALE_PATH+"label_std_item1.sub", },
									{"name":"Status_Standard_ItemList2", "type" : "image", "x":100, "y":30, "image" : LOCALE_PATH+"label_std_item2.sub", },

									## HTH
									{
										"name":"HTH_Label", "type":"window", "x":50, "y":32, "width":60, "height":20,
										"children" :
										(
											{ "name":"HTH_Slot", "type":"image", "x":0, "y":0, "image":SMALL_VALUE_FILE },
											{ "name":"HTH_Value", "type":"text", "x":20, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											{ "name":"HTH_Plus", "type" : "button", "x":41, "y":3, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },
										),
									},
									## INT
									{
										"name":"INT_Label", "type":"window", "x":50, "y":32+23, "width":60, "height":20,
										"children" :
										(
											{ "name":"INT_Slot", "type":"image", "x":0, "y":0, "image":SMALL_VALUE_FILE },
											{ "name":"INT_Value", "type":"text", "x":20, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											{ "name":"INT_Plus", "type" : "button", "x" : 41, "y" : 3, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },
										)
									},
									## STR
									{
										"name":"STR_Label", "type":"window", "x":50, "y":32+23*2, "width":60, "height":20,
										"children" :
										(
											{ "name":"STR_Slot", "type":"image", "x":0, "y":0, "image":SMALL_VALUE_FILE },
											{ "name":"STR_Value", "type":"text", "x":20, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											{ "name":"STR_Plus", "type" : "button", "x" : 41, "y" : 3, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },
										)
									},
									## DEX
									{
										"name":"DEX_Label", "type":"window", "x":50, "y":32+23*3, "width":60, "height":20, 
										"children" :
										(
											{ "name":"DEX_Slot", "type":"image", "x":0, "y":0, "image":SMALL_VALUE_FILE },
											{ "name":"DEX_Value", "type":"text", "x":20, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											{ "name":"DEX_Plus", "type" : "button", "x" : 41, "y" : 3, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },
										)
									},

									{ "name":"HTH_Minus", "type" : "button", "x":9, "y":35, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },
									{ "name":"INT_Minus", "type" : "button", "x":9, "y":35+23, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },
									{ "name":"STR_Minus", "type" : "button", "x":9, "y":35+23*2, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },
									{ "name":"DEX_Minus", "type" : "button", "x":9, "y":35+23*3, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },

									####

									## HP
									{
										"name":"HEL_Label", "type":"window", "x":145, "y":32, "width":50, "height":20,
										"children" :
										(
											{ "name":"HP_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
											{ "name":"HP_Value", "type":"text", "x":45, "y":3, "text":"9999/9999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										),
									},
									## SP
									{
										"name":"SP_Label", "type":"window", "x":145, "y":32+23, "width":50, "height":20, 
										"children" :
										(
											{ "name":"SP_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
											{ "name":"SP_Value", "type":"text", "x":45, "y":3, "text":"9999/9999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										)
									},
									## ATT
									{
										"name":"ATT_Label", "type":"window", "x":145, "y":32+23*2, "width":50, "height":20, 
										"children" :
										(
											{ "name":"ATT_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
											{ "name":"ATT_Value", "type":"text", "x":45, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										),
									},
									## DEF
									{
										"name":"DEF_Label", "type":"window", "x":145, "y":32+23*3, "width":50, "height":20, 
										"children" :
										(
											{ "name":"DEF_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
											{ "name":"DEF_Value", "type":"text", "x":45, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										)
									},
								),
							},
							
							## 부가 능력
							{ 
								"name":"Status_Extent", "type":"window", "x":3, "y":221, "width":200, "height":50, 
								"children" :
								(

									## 부가 능력 제목
									{ "name":"Status_Extent_Bar", "type":"horizontalbar", "x":12, "y":6, "width":223, },
									{ "name":"Status_Extent_Label", "type" : "image", "x" : 13, "y" : 8, "image" : LOCALE_PATH+"label_ext.sub", },

									## 기본 능력 아이템 리스트
									{"name":"Status_Extent_ItemList1", "type" : "image", "x":11, "y":31, "image" : LOCALE_PATH+"label_ext_item1.sub", },
									{"name":"Status_Extent_ItemList2", "type" : "image", "x":128, "y":32, "image" : LOCALE_PATH+"label_ext_item2.sub", },

									## MSPD - 이동 속도
									{
										"name":"MOV_Label", "type":"window", "x":66, "y":33, "width":50, "height":20, 
										"children" :
										(
											{ "name":"MSPD_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
											{ "name":"MSPD_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										)
									},

									## ASPD - 공격 속도
									{
										"name":"ASPD_Label", "type":"window", "x":66, "y":33+23, "width":50, "height":20, 
										"children" :
										(
											{ "name":"ASPD_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
											{ "name":"ASPD_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										)
									},

									## CSPD - 주문 속도
									{
										"name":"CSPD_Label", "type":"window", "x":66, "y":33+23*2, "width":50, "height":20, 
										"children" :
										(
											{ "name":"CSPD_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
											{ "name":"CSPD_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										)
									},

									## MATT - 마법 공격력
									{
										"name":"MATT_Label", "type":"window", "x":183, "y":33, "width":50, "height":20, 
										"children" :
										(
											{ "name":"MATT_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
											{ "name":"MATT_Value", "type":"text", "x":26, "y":3, "text":"999-999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										)
									},

									## MDEF - 마법 방어력
									{
										"name":"MDEF_Label", "type":"window", "x":183, "y":33+23, "width":50, "height":20, 
										"children" :
										(
											{ "name":"MDEF_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
											{ "name":"MDEF_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										)
									},

									## 회피율
									{
										"name":"ER_Label", "type":"window", "x":183, "y":33+23*2, "width":50, "height":20, 
										"children" :
										(
											{ "name":"ER_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
											{ "name":"ER_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										)
									},

								),
							},
						),
					},
					{
						"name" : "Skill_Page",
						"type" : "window",
						"style" : ("attach",),

						"x" : 0,
						"y" : 24,

						"width" : 250,
						"height" : 304,

						"children" :
						(

							{
								"name":"Skill_Active_Title_Bar", "type":"horizontalbar", "x":15, "y":17, "width":223,

								"children" :
								(
									{ 
										"name":"Active_Skill_Point_Label", "type":"image", "x":145, "y":3, "image":LOCALE_PATH+"label_uppt.sub",
										"children" :
										(
											{ "name":"Active_Skill_Point_Value", "type":"text", "x":62, "y":0, "text":"99", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										),
									},

									## Group Button
									{
										"name" : "Skill_Group_Button_1",
										"type" : "radio_button",

										"x" : 5,
										"y" : 2,

										"text" : "Group1",
										"text_color" : 0xFFFFE3AD,

										"default_image" : "d:/ymir work/ui/game/windows/skill_tab_button_01.sub",
										"over_image" : "d:/ymir work/ui/game/windows/skill_tab_button_02.sub",
										"down_image" : "d:/ymir work/ui/game/windows/skill_tab_button_03.sub",
									},

									{
										"name" : "Skill_Group_Button_2",
										"type" : "radio_button",

										"x" : 50,
										"y" : 2,

										"text" : "Group2",
										"text_color" : 0xFFFFE3AD,

										"default_image" : "d:/ymir work/ui/game/windows/skill_tab_button_01.sub",
										"over_image" : "d:/ymir work/ui/game/windows/skill_tab_button_02.sub",
										"down_image" : "d:/ymir work/ui/game/windows/skill_tab_button_03.sub",
									},

									{
										"name" : "Active_Skill_Group_Name",
										"type" : "text",

										"x" : 7,
										"y" : 1,
										"text" : "Active",

										"vertical_align" : "center",
										"text_vertical_align" : "center",
										"color" : 0xFFFFE3AD,
									},

								),
							},

							{
								"name":"Skill_ETC_Title_Bar", "type":"horizontalbar", "x":15, "y":200, "width":223,

								"children" :
								(
									{
										"name" : "Support_Skill_Group_Name",
										"type" : "text",

										"x" : 7,
										"y" : 1,
										"text" : uiScriptLocale.SKILL_SUPPORT_TITLE,

										"vertical_align" : "center",
										"text_vertical_align" : "center",
										"color" : 0xFFFFE3AD,
									},

									{ 
										"name":"Support_Skill_Point_Label", "type":"image", "x":145, "y":3, "image":LOCALE_PATH+"label_uppt.sub",
										"children" :
										(
											{ "name":"Support_Skill_Point_Value", "type":"text", "x":62, "y":0, "text":"99", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										),
									},
								),
							},
							{ "name":"Skill_Board", "type":"image", "x":13, "y":38, "image":"d:/ymir work/ui/game/windows/skill_board.sub", },

							## Active Slot
							{
								"name" : "Skill_Active_Slot",
								"type" : "slot",

								"x" : 0 + 16,
								"y" : 0 + 15 + 23,

								"width" : 223,
								"height" : 223,
								"image" : ICON_SLOT_FILE,

								"slot" :	(
												{"index": 1, "x": 1, "y":  4, "width":32, "height":32},
												{"index":21, "x":38, "y":  4, "width":32, "height":32},
												{"index":41, "x":75, "y":  4, "width":32, "height":32},

												{"index": 3, "x": 1, "y": 40, "width":32, "height":32},
												{"index":23, "x":38, "y": 40, "width":32, "height":32},
												{"index":43, "x":75, "y": 40, "width":32, "height":32},

												{"index": 5, "x": 1, "y": 76, "width":32, "height":32},
												{"index":25, "x":38, "y": 76, "width":32, "height":32},
												{"index":45, "x":75, "y": 76, "width":32, "height":32},

												{"index": 7, "x": 1, "y":112, "width":32, "height":32},
												{"index":27, "x":38, "y":112, "width":32, "height":32},
												{"index":47, "x":75, "y":112, "width":32, "height":32},

												####

												{"index": 2, "x":113, "y":  4, "width":32, "height":32},
												{"index":22, "x":150, "y":  4, "width":32, "height":32},
												{"index":42, "x":187, "y":  4, "width":32, "height":32},

												{"index": 4, "x":113, "y": 40, "width":32, "height":32},
												{"index":24, "x":150, "y": 40, "width":32, "height":32},
												{"index":44, "x":187, "y": 40, "width":32, "height":32},

												{"index": 6, "x":113, "y": 76, "width":32, "height":32},
												{"index":26, "x":150, "y": 76, "width":32, "height":32},
												{"index":46, "x":187, "y": 76, "width":32, "height":32},

												{"index": 8, "x":113, "y":112, "width":32, "height":32},
												{"index":28, "x":150, "y":112, "width":32, "height":32},
												{"index":48, "x":187, "y":112, "width":32, "height":32},
											),
							},

							## ETC Slot
							{
								"name" : "Skill_ETC_Slot",
								"type" : "grid_table",
								"x" : 18,
								"y" : 221,
								"start_index" : 101,
								"x_count" : 6,
								"y_count" : 2,
								"x_step" : 32,
								"y_step" : 32,
								"x_blank" : 5,
								"y_blank" : 4,
								"image" : ICON_SLOT_FILE,
							},

						),
					},
					{
						"name" : "Emoticon_Page",
						"type" : "window",
						"style" : ("attach",),

						"x" : 0,
						"y" : 24,

						"width" : 250,
						"height" : 304,

						"children" :
						(
							## 기본 액션 제목
							{ "name":"Action_Bar", "type":"horizontalbar", "x":12, "y":11, "width":223, },
							{ "name":"Action_Bar_Text", "type":"text", "x":15, "y":13, "text":uiScriptLocale.CHARACTER_NORMAL_ACTION },

							## Basis Action Slot
							{
								"name" : "SoloEmotionSlot",
								"type" : "grid_table",
								"x" : 30,
								"y" : 33,
								"horizontal_align" : "center",
								"start_index" : 1,
								"x_count" : 6,
								"y_count" : 3,
								"x_step" : 32,
								"y_step" : 32,
								"x_blank" : 0,
								"y_blank" : 0,
								"image" : ICON_SLOT_FILE,
							},

							## 상호 액션 제목
							{ "name":"Reaction_Bar", "type":"horizontalbar", "x":12, "y":8+150, "width":223, },
							{ "name":"Reaction_Bar_Text", "type":"text", "x":15, "y":10+150, "text":uiScriptLocale.CHARACTER_MUTUAL_ACTION },

							## Reaction Slot
							{
								"name" : "DualEmotionSlot",
								"type" : "grid_table",
								"x" : 30,
								"y" : 180,
								"start_index" : 51,
								"x_count" : 6,
								"y_count" : 3,
								"x_step" : 32,
								"y_step" : 32,
								"x_blank" : 0,
								"y_blank" : 0,
								"image" : ICON_SLOT_FILE,
							},
						),
					},
					{
						"name" : "Quest_Page",
						"type" : "window",
						"style" : ("attach",),

						"x" : 0,
						"y" : 24,

						"width" : 250,
						"height" : 304,

						"children" :
						(
							{
								"name" : "Quest_Slot",
								"type" : "grid_table",
								"x" : 18,
								"y" : 20,
								"start_index" : 0,
								"x_count" : 1,
								"y_count" : 5,
								"x_step" : 32,
								"y_step" : 32,
								"y_blank" : 28,
								"image" : QUEST_ICON_BACKGROUND,
							},

							{
								"name" : "Quest_ScrollBar",
								"type" : "scrollbar",

								"x" : 25,
								"y" : 12,
								"size" : 290,
								"horizontal_align" : "right",
							},

							{ "name" : "Quest_Name_00", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 14 },
							{ "name" : "Quest_LastTime_00", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 30 },
							{ "name" : "Quest_LastCount_00", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 46 },

							{ "name" : "Quest_Name_01", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 74 },
							{ "name" : "Quest_LastTime_01", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 90 },
							{ "name" : "Quest_LastCount_01", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 106 },

							{ "name" : "Quest_Name_02", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 134 },
							{ "name" : "Quest_LastTime_02", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 150 },
							{ "name" : "Quest_LastCount_02", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 166 },

							{ "name" : "Quest_Name_03", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 194 },
							{ "name" : "Quest_LastTime_03", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 210 },
							{ "name" : "Quest_LastCount_03", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 226 },

							{ "name" : "Quest_Name_04", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 254 },
							{ "name" : "Quest_LastTime_04", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 270 },
							{ "name" : "Quest_LastCount_04", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 286 },

						),
					},
				),
			},
		),
	}
