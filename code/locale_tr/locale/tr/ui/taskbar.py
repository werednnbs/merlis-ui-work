import uiScriptLocale
import app

ROOT = "d:/ymir work/ui/game/"
if app.ENABLE_WEREDNNBS_UIGAME:
	RESOURCE = "d:/ymir work/ui/gui/TaskBar/"

#Y_ADD_POSITION = -2
Y_ADD_POSITION = 0

if app.ENABLE_WEREDNNBS_UIGAME:
	window = {
		"name" : "TaskBar",

		"x" : 0,
		"y" : SCREEN_HEIGHT - 59,

		"width" : SCREEN_WIDTH,
		"height" : 59,

		"children" :
		(
			## Board
			{
				"name" : "Base_Board_01",
				"type" : "expanded_image",

				"x" : 0,
				"y" : 24,

				"rect" : (0.0, 0.0, float(SCREEN_WIDTH - 200) / 156.0, 0.0),

				"image" : RESOURCE + "TaskBar_Base.tga"
			},

			## Gauge
			{
				"name" : "Gauge_Board",
				"type" : "image",

				"width" : 237,
				"height" : 64,

				"x" : 0,
				"y" : -5,

				"image" : RESOURCE + "taskbar_left.tga",

				"children" :
				(

					{
						## ÅøÆÁÀ» ¶ç¿ì±â À§ÇÑ À©µµ¿ì
						"name" : "HPGauge_Board",
						"type" : "window",

						"x" : 59,
						"y" : 25,

						"width" : 174,
						"height" : 14,

						"children" :
						(
							{
								"name" : "HPRecoveryGaugeBar",
								"type" : "bar",

								"x" : 0,
								"y" : 0,
								"width" : 109,
								"height" : 7,
								"color" : 0x55ff0000,
							},
							{
								"name" : "HPGauge",
								"type" : "expanded_image",

								"x" : 0,
								"y" : 0,

								"image" : RESOURCE + "gauge_hp.tga",
							},
							{
								"name" : "HPGaugeTooltip",
								"type" : "text",
								
								"x" : 9,
								"y" : 0,

								"text_horizontal_align" : "left",
								"horizontal_align" : "left",
								"r" : 0.96, "g" : 0.58, "b" : 0.58, "a" : 1,
								
								"text" : "0/0",
							},
						),
					},
					{
						## ÅøÆÁÀ» ¶ç¿ì±â À§ÇÑ À©µµ¿ì
						"name" : "SPGauge_Board",
						"type" : "window",

						"x" : 55,
						"y" : 39,

						"width" : 170,
						"height" : 14,

						"children" :
						(
							{
								"name" : "SPRecoveryGaugeBar",
								"type" : "bar",

								"x" : 0,
								"y" : 0,
								"width" : 109,
								"height" : 5,
								"color" : 0x550000ff,
							},
							{
								"name" : "SPGauge",
								"type" : "expanded_image",

								"x" : 0,
								"y" : 0,

								"image" : RESOURCE + "gauge_sp.tga",
							},
							{
								"name" : "SPGaugeTooltip",
								"type" : "text",
								
								"x" : 9,
								"y" : 1,
								
								"text_horizontal_align" : "left",
								"horizontal_align" : "left",

								"text" : "0/0",
							},
						),
					},
					{
						## ÅøÆÁÀ» ¶ç¿ì±â À§ÇÑ À©µµ¿ì
						"name" : "STGauge_Board",
						"type" : "window",

						"x" : 40,
						"y" : 54,

						"width" : 174,
						"height" : 10,

						"children" :
						(
							{
								"name" : "STGauge",
								"type" : "expanded_image",

								"x" : 0,
								"y" : 0,

								"image" : RESOURCE + "gauge_st.tga",
							},
						),
					},
					{
						"name" : "RampageGauge",
						"type" : "button",

						"x" : 58,
						"y" : 8,

						# "tooltip_text" : uiScriptLocale.TASKBAR_CHARACTER,

						"default_image" : RESOURCE + "bottons/mouse_button_camera_01.tga",
						"over_image" : RESOURCE + "bottons/mouse_button_camera_02.tga",
						"down_image" : RESOURCE + "bottons/mouse_button_camera_03.tga",
					},
				),
			},

			# {
			# 	"name" : "EXP_Gauge_Board",
			# 	# "type" : "image",

			# 	"x" : 169,
			# 	"y" : -5,

			# 	# "image" : RESOURCE + "exp_gauge.tga",

			# 	"children" :
			# 	(
			# 		{
			# 			"name" : "EXPGauge_01",
			# 			"type" : "expanded_image",

			# 			"x" : 0,
			# 			"y" : 25,

			# 			"image" : RESOURCE + "EXP_Gauge_Point.tga",
			# 		},
			# 		{
			# 			"name" : "EXPGauge_02",
			# 			"type" : "expanded_image",

			# 			"x" : 27,
			# 			"y" : 25,

			# 			"image" : RESOURCE + "EXP_Gauge_Point.tga",
			# 		},
			# 		{
			# 			"name" : "EXPGauge_03",
			# 			"type" : "expanded_image",

			# 			"x" : 54,
			# 			"y" : 25,

			# 			"image" : RESOURCE + "EXP_Gauge_Point.tga",
			# 		},
			# 		{
			# 			"name" : "EXPGauge_04",
			# 			"type" : "expanded_image",

			# 			"x" : 81,
			# 			"y" : 25,

			# 			"image" : RESOURCE + "EXP_Gauge_Point.tga",
			# 		},
			# 	),
			# },

			# {
			# 	"name" : "Detail_Right",
			# 	"type" : "image",

			# 	"width" : 63,
			# 	"height" : 41,

			# 	"x" : SCREEN_WIDTH-63,
			# 	"y" : -32,

			# 	"image" : RESOURCE + "detail_right.tga",
			# },

			{
				"name" : "TaskBar_Right",
				# "type" : "image",

				"width" : 170,
				"height" : 59,

				"x" : SCREEN_WIDTH-170,
				"y" : 0,

				# "image" : RESOURCE + "taskbar_right.tga",

				"children" :
				(
						
					{
						"name" : "CharacterButton",
						"type" : "button",

						"x" : 28,
						"y" : 26  + Y_ADD_POSITION,

						"tooltip_text" : uiScriptLocale.TASKBAR_CHARACTER,

						"default_image" : RESOURCE + "bottons/Character_Button_01.tga",
						"over_image" : RESOURCE + "bottons/Character_Button_02.tga",
						"down_image" : RESOURCE + "bottons/Character_Button_03.tga",
					},
					{
						"name" : "InventoryButton",
						"type" : "button",

						"x" : 28 + 35,
						"y" : 26  + Y_ADD_POSITION,

						"tooltip_text" : uiScriptLocale.TASKBAR_INVENTORY,

						"default_image" : RESOURCE + "bottons/Inventory_Button_01.tga",
						"over_image" : RESOURCE + "bottons/Inventory_Button_02.tga",
						"down_image" : RESOURCE + "bottons/Inventory_Button_03.tga",
					},
					{
						"name" : "MessengerButton",
						"type" : "button",

						"x" : 28 + 70,
						"y" : 26  + Y_ADD_POSITION,

						"tooltip_text" : uiScriptLocale.TASKBAR_MESSENGER,

						"default_image" : RESOURCE + "bottons/Community_Button_01.tga",
						"over_image" : RESOURCE + "bottons/Community_Button_02.tga",
						"down_image" : RESOURCE + "bottons/Community_Button_03.tga",
					},
					{
						"name" : "SystemButton",
						"type" : "button",

						"x" : 28 + 105,
						"y" : 26  + Y_ADD_POSITION,

						"tooltip_text" : uiScriptLocale.TASKBAR_SYSTEM,

						"default_image" : RESOURCE + "bottons/System_Button_01.tga",
						"over_image" : RESOURCE + "bottons/System_Button_02.tga",
						"down_image" : RESOURCE + "bottons/System_Button_03.tga",
					},
				),
			},
			## QuickBar
			{
				"name" : "quickslot_board",
				"type" : "image",

				"x" : SCREEN_WIDTH/2 - 175,
				"y" : 0 + Y_ADD_POSITION,

				"width" : 411,
				"height" : 59,

				"image" : RESOURCE + "taskbar_center.tga",

				"children" :
				(
					{
						## ÅøÆÁÀ» ¶ç¿ì±â À§ÇÑ À©µµ¿ì
						"name" : "EXP_Gauge_Board",
						"type" : "window",

						"x" : 11,
						"y" : 50,

						"width" : 393,
						"height" : 10,

						"children" :
						(
							{
								"name" : "expGauge",
								"type" : "expanded_image",

								"x" : 0,
								"y" : 0,

								"image" : RESOURCE + "gauge_exp.tga",
							},
						),
					},
					{
						# ExpandButtonÀº ±âÁ¸¿¡ ChatButtonÀÌ¾úÀ¸³ª, ChatButtonÀÇ È¿¿ë¼ºÀÌ Àû´Ù ÆÇ´ÜÇÏ¿©
						# ExpandButtonÀ¸·Î ¹Ù²ï °ÍÀÌ´Ù.
						"name" : "ExpandButton",
						"type" : "button",

						"x" : 201,
						"y" : 11,
						"tooltip_text" : uiScriptLocale.TASKBAR_EXPAND,
						
						
						"default_image" : RESOURCE + "detail_center.tga",
						"over_image" : RESOURCE + "detail_center_hover.tga",
						"down_image" : RESOURCE + "detail_center.tga",
					},
					{
						"name" : "quick_slot_1",
						"type" : "grid_table",

						"start_index" : 0,

						"x" : 64,
						"y" : 15,

						"x_count" : 4,
						"y_count" : 1,
						"x_step" : 35,
						"y_step" : 32,

						"image" : RESOURCE + "slot_base_l.tga",
						"image_r" : 1.0,
						"image_g" : 1.0,
						"image_b" : 1.0,
						"image_a" : 1.0,

						"children" :
						(
							{ "name" : "slot_1", "type" : "image", "x" : 3, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/1.sub", },
							{ "name" : "slot_2", "type" : "image", "x" : 35+2, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/2.sub", },
							{ "name" : "slot_3", "type" : "image", "x" : 68+4, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/3.sub", },
							{ "name" : "slot_4", "type" : "image", "x" : 101+6, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/4.sub", },
						),
					},
					{
						"name" : "quick_slot_2",
						"type" : "grid_table",

						"start_index" : 4,

						"x" : 212,
						"y" : 15,

						"x_count" : 4,
						"y_count" : 1,
						"x_step" : 35,
						"y_step" : 32,

						"image" : RESOURCE + "slot_base_r.tga",
						"image_r" : 1.0,
						"image_g" : 1.0,
						"image_b" : 1.0,
						"image_a" : 1.0,

						"children" :
						(
							{ "name" : "slot_5", "type" : "image", "x" : 3, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f1.sub", },
							{ "name" : "slot_6", "type" : "image", "x" : 35+2, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f2.sub", },
							{ "name" : "slot_7", "type" : "image", "x" : 68+4, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f3.sub", },
							{ "name" : "slot_8", "type" : "image", "x" : 101+6, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f4.sub", },
						),
					},
					{
						"name" : "QuickSlotBoard",
						"type" : "window",

						"x" : 351,
						"y" : 21,
						"width" : 12,
						"height" : 25,
						"children" :
						(
							# {
							# 	"name" : "QuickSlotNumberBox",
							# 	"type" : "image",							
							# 	"x" : 0,
							# 	"y" : 13,
							# 	"image" : RESOURCE + "quickslot_btn_board.tga",
							# },
							{
								"name" : "QuickPageUpButton",
								"type" : "button",
								"tooltip_text" : uiScriptLocale.TASKBAR_PREV_QUICKSLOT,
								"x" : 1,
								"y" : 0,
								"default_image" : ROOT + "TaskBar/QuickSlot_UpButton_01.sub",
								"over_image" : ROOT + "TaskBar/QuickSlot_UpButton_02.sub",
								"down_image" : ROOT + "TaskBar/QuickSlot_UpButton_03.sub",
							},

							{ 
								"name" : "QuickPageNumber", 
								"type" : "image", 							
								"x" : 3, "y" : 16, "image" : "d:/ymir work/ui/game/taskbar/1.sub", 
							},
							{
								"name" : "QuickPageDownButton",
								"type" : "button",
								"tooltip_text" : uiScriptLocale.TASKBAR_NEXT_QUICKSLOT,

								"x" : 1,
								"y" : 6,

								"default_image" : ROOT + "TaskBar/QuickSlot_DownButton_01.sub",
								"over_image" : ROOT + "TaskBar/QuickSlot_DownButton_02.sub",
								"down_image" : ROOT + "TaskBar/QuickSlot_DownButton_03.sub",
							},
		
						),
					},
					## Mouse Button
					{
						"name" : "LeftMouseButton",
						"type" : "button",

						"x" : 45,
						"y" : 20+Y_ADD_POSITION,

						"default_image" : ROOT + "TaskBar/Mouse_Button_Move_01.sub",
						"over_image" : ROOT + "TaskBar/Mouse_Button_Move_02.sub",
						"down_image" : ROOT + "TaskBar/Mouse_Button_Move_03.sub",
					},
					{
						"name" : "RightMouseButton",
						"type" : "button",

						"x" : 45,
						"y" : 20+14+Y_ADD_POSITION,

						"default_image" : ROOT + "TaskBar/Mouse_Button_Move_01.sub",
						"over_image" : ROOT + "TaskBar/Mouse_Button_Move_02.sub",
						"down_image" : ROOT + "TaskBar/Mouse_Button_Move_03.sub",
					},
				),
			},
		),
	}
else:
	window = {
		"name" : "TaskBar",

		"x" : 0,
		"y" : SCREEN_HEIGHT - 37,

		"width" : SCREEN_WIDTH,
		"height" : 37,

		"children" :
		(
			## Board
			{
				"name" : "Base_Board_01",
				"type" : "expanded_image",

				"x" : 263,
				"y" : 0,

				"rect" : (0.0, 0.0, float(SCREEN_WIDTH - 263 - 256) / 256.0, 0.0),

				"image" : "d:/ymir work/ui/pattern/TaskBar_Base.tga"
			},

			## Gauge
			{
				"name" : "Gauge_Board",
				"type" : "image",

				"x" : 0,
				"y" : -10 + Y_ADD_POSITION,

				"image" : ROOT + "taskbar/gauge.sub",

				"children" :
				(
					{
						"name" : "RampageGauge",
						"type" : "ani_image",

						"x" : 8,
						"y" : 4,
						"width"  : 40,
						"height" : 40,

						"delay" : 6,

						"images" :
						(
							"locale/tr/ui/Mall/00.sub",
							"locale/tr/ui/Mall/01.sub",
							"locale/tr/ui/Mall/02.sub",
							"locale/tr/ui/Mall/03.sub",
							"locale/tr/ui/Mall/04.sub",
							"locale/tr/ui/Mall/05.sub",
							"locale/tr/ui/Mall/06.sub",
							"locale/tr/ui/Mall/07.sub",
							"locale/tr/ui/Mall/08.sub",
							"locale/tr/ui/Mall/09.sub",
							"locale/tr/ui/Mall/11.sub",
							"locale/tr/ui/Mall/12.sub",
							"locale/tr/ui/Mall/13.sub",
							"locale/tr/ui/Mall/14.sub",
							"locale/tr/ui/Mall/15.sub",
							"locale/tr/ui/Mall/16.sub",
						)
					},
					{
						"name" : "RampageGauge2",
						"type" : "ani_image",

						"x" : 8,
						"y" : 4,
						"width"  : 40,
						"height" : 40,

						"delay" : 6,

						"images" :
						(
							"locale/tr/ui/Mall/00.sub",
							"locale/tr/ui/Mall/01.sub",
							"locale/tr/ui/Mall/02.sub",
							"locale/tr/ui/Mall/03.sub",
							"locale/tr/ui/Mall/04.sub",
							"locale/tr/ui/Mall/05.sub",
							"locale/tr/ui/Mall/06.sub",
							"locale/tr/ui/Mall/07.sub",
							"locale/tr/ui/Mall/08.sub",
							"locale/tr/ui/Mall/09.sub",
							"locale/tr/ui/Mall/11.sub",
							"locale/tr/ui/Mall/12.sub",
							"locale/tr/ui/Mall/13.sub",
							"locale/tr/ui/Mall/14.sub",
							"locale/tr/ui/Mall/15.sub",
							"locale/tr/ui/Mall/16.sub",
						)
					},
					{
						## ÅøÆÁÀ» ¶ç¿ì±â À§ÇÑ À©µµ¿ì
						"name" : "HPGauge_Board",
						"type" : "window",

						"x" : 59,
						"y" : 14,

						"width" : 95,
						"height" : 11,

						"children" :
						(
							{
								"name" : "HPRecoveryGaugeBar",
								"type" : "bar",

								"x" : 0,
								"y" : 0,
								"width" : 95,
								"height" : 13,
								"color" : 0x55ff0000,
							},
							{
								"name" : "HPGauge",
								"type" : "ani_image",

								"x" : 0,
								"y" : 0,

								"delay" : 6,

								"images" :
								(
									"D:/Ymir Work/UI/Pattern/HPGauge/01.tga",
									"D:/Ymir Work/UI/Pattern/HPGauge/02.tga",
									"D:/Ymir Work/UI/Pattern/HPGauge/03.tga",
									"D:/Ymir Work/UI/Pattern/HPGauge/04.tga",
									"D:/Ymir Work/UI/Pattern/HPGauge/05.tga",
									"D:/Ymir Work/UI/Pattern/HPGauge/06.tga",
									"D:/Ymir Work/UI/Pattern/HPGauge/07.tga",
								),
							},
						),
					},
					{
						## ÅøÆÁÀ» ¶ç¿ì±â À§ÇÑ À©µµ¿ì
						"name" : "SPGauge_Board",
						"type" : "window",

						"x" : 59,
						"y" : 24,

						"width" : 95,
						"height" : 11,

						"children" :
						(
							{
								"name" : "SPRecoveryGaugeBar",
								"type" : "bar",

								"x" : 0,
								"y" : 0,
								"width" : 95,
								"height" : 13,
								"color" : 0x550000ff,
							},
							{
								"name" : "SPGauge",
								"type" : "ani_image",

								"x" : 0,
								"y" : 0,

								"delay" : 6,

								"images" :
								(
									"D:/Ymir Work/UI/Pattern/SPGauge/01.tga",
									"D:/Ymir Work/UI/Pattern/SPGauge/02.tga",
									"D:/Ymir Work/UI/Pattern/SPGauge/03.tga",
									"D:/Ymir Work/UI/Pattern/SPGauge/04.tga",
									"D:/Ymir Work/UI/Pattern/SPGauge/05.tga",
									"D:/Ymir Work/UI/Pattern/SPGauge/06.tga",
									"D:/Ymir Work/UI/Pattern/SPGauge/07.tga",
								),
							},
						),
					},
					{
						## ÅøÆÁÀ» ¶ç¿ì±â À§ÇÑ À©µµ¿ì
						"name" : "STGauge_Board",
						"type" : "window",

						"x" : 59,
						"y" : 38,

						"width" : 95,
						"height" : 6,

						"children" :
						(
							{
								"name" : "STGauge",
								"type" : "ani_image",

								"x" : 0,
								"y" : 0,

								"delay" : 6,

								"images" :
								(
									"D:/Ymir Work/UI/Pattern/STGauge/01.tga",
									"D:/Ymir Work/UI/Pattern/STGauge/02.tga",
									"D:/Ymir Work/UI/Pattern/STGauge/03.tga",
									"D:/Ymir Work/UI/Pattern/STGauge/04.tga",
									"D:/Ymir Work/UI/Pattern/STGauge/05.tga",
									"D:/Ymir Work/UI/Pattern/STGauge/06.tga",
									"D:/Ymir Work/UI/Pattern/STGauge/07.tga",
								),
							},
						),
					},

				),
			},
			{
				"name" : "EXP_Gauge_Board",
				"type" : "image",

				"x" : 158,
				"y" : 0 + Y_ADD_POSITION,

				"image" : ROOT + "taskbar/exp_gauge.sub",

				"children" :
				(
					{
						"name" : "EXPGauge_01",
						"type" : "expanded_image",

						"x" : 5,
						"y" : 9,

						"image" : ROOT + "TaskBar/EXP_Gauge_Point.sub",
					},
					{
						"name" : "EXPGauge_02",
						"type" : "expanded_image",

						"x" : 30,
						"y" : 9,

						"image" : ROOT + "TaskBar/EXP_Gauge_Point.sub",
					},
					{
						"name" : "EXPGauge_03",
						"type" : "expanded_image",

						"x" : 55,
						"y" : 9,

						"image" : ROOT + "TaskBar/EXP_Gauge_Point.sub",
					},
					{
						"name" : "EXPGauge_04",
						"type" : "expanded_image",

						"x" : 80,
						"y" : 9,

						"image" : ROOT + "TaskBar/EXP_Gauge_Point.sub",
					},
				),
			},

			## Mouse Button
			{
				"name" : "LeftMouseButton",
				"type" : "button",

				"x" : SCREEN_WIDTH/2 - 128,
				"y" : 3 + Y_ADD_POSITION,

				"default_image" : ROOT + "TaskBar/Mouse_Button_Move_01.sub",
				"over_image" : ROOT + "TaskBar/Mouse_Button_Move_02.sub",
				"down_image" : ROOT + "TaskBar/Mouse_Button_Move_03.sub",
			},
			{
				"name" : "RightMouseButton",
				"type" : "button",

				"x" : SCREEN_WIDTH/2 + 128 + 66 + 11,
				"y" : 3 + Y_ADD_POSITION,

				"default_image" : ROOT + "TaskBar/Mouse_Button_Move_01.sub",
				"over_image" : ROOT + "TaskBar/Mouse_Button_Move_02.sub",
				"down_image" : ROOT + "TaskBar/Mouse_Button_Move_03.sub",
			},

			## Button
			{
				"name" : "CharacterButton",
				"type" : "button",

				"x" : SCREEN_WIDTH - 144,
				"y" : 3 + Y_ADD_POSITION,

				"tooltip_text" : uiScriptLocale.TASKBAR_CHARACTER,

				"default_image" : ROOT + "TaskBar/Character_Button_01.sub",
				"over_image" : ROOT + "TaskBar/Character_Button_02.sub",
				"down_image" : ROOT + "TaskBar/Character_Button_03.sub",
			},
			{
				"name" : "InventoryButton",
				"type" : "button",

				"x" : SCREEN_WIDTH - 110,
				"y" : 3 + Y_ADD_POSITION,

				"tooltip_text" : uiScriptLocale.TASKBAR_INVENTORY,

				"default_image" : ROOT + "TaskBar/Inventory_Button_01.sub",
				"over_image" : ROOT + "TaskBar/Inventory_Button_02.sub",
				"down_image" : ROOT + "TaskBar/Inventory_Button_03.sub",
			},
			{
				"name" : "MessengerButton",
				"type" : "button",

				"x" : SCREEN_WIDTH - 76,
				"y" : 3 + Y_ADD_POSITION,

				"tooltip_text" : uiScriptLocale.TASKBAR_MESSENGER,

				"default_image" : ROOT + "TaskBar/Community_Button_01.sub",
				"over_image" : ROOT + "TaskBar/Community_Button_02.sub",
				"down_image" : ROOT + "TaskBar/Community_Button_03.sub",
			},
			{
				"name" : "SystemButton",
				"type" : "button",

				"x" : SCREEN_WIDTH - 42,
				"y" : 3 + Y_ADD_POSITION,

				"tooltip_text" : uiScriptLocale.TASKBAR_SYSTEM,

				"default_image" : ROOT + "TaskBar/System_Button_01.sub",
				"over_image" : ROOT + "TaskBar/System_Button_02.sub",
				"down_image" : ROOT + "TaskBar/System_Button_03.sub",
			},

			## QuickBar
			{
				"name" : "quickslot_board",
				"type" : "window",

				"x" : SCREEN_WIDTH/2 - 128 + 32 + 10,
				"y" : 0 + Y_ADD_POSITION,

				"width" : 256 + 14 + 2 + 11,
				"height" : 37,

				"children" :
				(
					{
						# ExpandButtonÀº ±âÁ¸¿¡ ChatButtonÀÌ¾úÀ¸³ª, ChatButtonÀÇ È¿¿ë¼ºÀÌ Àû´Ù ÆÇ´ÜÇÏ¿©
						# ExpandButtonÀ¸·Î ¹Ù²ï °ÍÀÌ´Ù.
						"name" : "ExpandButton",
						"type" : "button",

						"x" : 128,
						"y" : 1,
						"tooltip_text" : uiScriptLocale.TASKBAR_EXPAND,
						
						
						"default_image" : ROOT + "TaskBar/Chat_Button_01.sub",
						"over_image" : ROOT + "TaskBar/Chat_Button_02.sub",
						"down_image" : ROOT + "TaskBar/Chat_Button_03.sub",
					},
					{
						"name" : "quick_slot_1",
						"type" : "grid_table",

						"start_index" : 0,

						"x" : 0,
						"y" : 3,

						"x_count" : 4,
						"y_count" : 1,
						"x_step" : 32,
						"y_step" : 32,

						"image" : "d:/ymir work/ui/Public/Slot_Base.sub",
						"image_r" : 1.0,
						"image_g" : 1.0,
						"image_b" : 1.0,
						"image_a" : 1.0,

						"children" :
						(
							{ "name" : "slot_1", "type" : "image", "x" : 3, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/1.sub", },
							{ "name" : "slot_2", "type" : "image", "x" : 35, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/2.sub", },
							{ "name" : "slot_3", "type" : "image", "x" : 67, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/3.sub", },
							{ "name" : "slot_4", "type" : "image", "x" : 99, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/4.sub", },
						),
					},
					{
						"name" : "quick_slot_2",
						"type" : "grid_table",

						"start_index" : 4,

						"x" : 128 + 14,
						"y" : 3,

						"x_count" : 4,
						"y_count" : 1,
						"x_step" : 32,
						"y_step" : 32,

						"image" : "d:/ymir work/ui/Public/Slot_Base.sub",
						"image_r" : 1.0,
						"image_g" : 1.0,
						"image_b" : 1.0,
						"image_a" : 1.0,

						"children" :
						(
							{ "name" : "slot_5", "type" : "image", "x" : 3, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f1.sub", },
							{ "name" : "slot_6", "type" : "image", "x" : 35, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f2.sub", },
							{ "name" : "slot_7", "type" : "image", "x" : 67, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f3.sub", },
							{ "name" : "slot_8", "type" : "image", "x" : 99, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f4.sub", },
						),
					},
					{
						"name" : "QuickSlotBoard",
						"type" : "window",

						"x" : 128+14+128+2,
						"y" : 0,
						"width" : 11,
						"height" : 37,
						"children" :
						(
							{
								"name" : "QuickSlotNumberBox",
								"type" : "image",							
								"x" : 1,
								"y" : 15,
								"image" : ROOT + "taskbar/QuickSlot_Button_Board.sub",
							},
							{
								"name" : "QuickPageUpButton",
								"type" : "button",
								"tooltip_text" : uiScriptLocale.TASKBAR_PREV_QUICKSLOT,
								"x" : 1,
								"y" : 9,
								"default_image" : ROOT + "TaskBar/QuickSlot_UpButton_01.sub",
								"over_image" : ROOT + "TaskBar/QuickSlot_UpButton_02.sub",
								"down_image" : ROOT + "TaskBar/QuickSlot_UpButton_03.sub",
							},

							{ 
								"name" : "QuickPageNumber", 
								"type" : "image", 							
								"x" : 3, "y" : 15, "image" : "d:/ymir work/ui/game/taskbar/1.sub", 
							},
							{
								"name" : "QuickPageDownButton",
								"type" : "button",
								"tooltip_text" : uiScriptLocale.TASKBAR_NEXT_QUICKSLOT,

								"x" : 1,
								"y" : 24,

								"default_image" : ROOT + "TaskBar/QuickSlot_DownButton_01.sub",
								"over_image" : ROOT + "TaskBar/QuickSlot_DownButton_02.sub",
								"down_image" : ROOT + "TaskBar/QuickSlot_DownButton_03.sub",
							},
		
						),
					},
				),
			},

		),
	}
