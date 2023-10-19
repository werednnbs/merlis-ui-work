import uiScriptLocale
import item
import app

if app.ENABLE_WEREDNNBS_UIGAME:
	import ui

EQUIPMENT_START_INDEX = 225
if app.ENABLE_WEREDNNBS_UIGAME:
	RESOURCE = "d:/ymir work/ui/gui/inventory/"
	PATCH_COMMON = ui.PATCH_COMMON

if app.ENABLE_WEREDNNBS_UIGAME:
	window = {
		"name" : "InventoryWindow",

		## 600 - (width + 오른쪽으로 부터 띄우기 24 px)
		"x" : SCREEN_WIDTH - 196,
		"y" : SCREEN_HEIGHT - 57 - 585,

		"style" : ("movable", "float",),

		"width" : 172,
		"height" : 580,

		"children" :
		(
			## Inventory, Equipment Slots
			{
				"name" : "board",
				"type" : "board",
				"style" : ("attach",),

				"x" : 0,
				"y" : 0,

				"width" : 172,
				"height" : 580,

				"children" :
				(
					## Title
					{
						"name" : "TitleBar",
						"type" : "titlebar",
						"style" : ("attach",),

						"x" : 6,
						"y" : 7,

						"width" : 158,
						"color" : "yellow",

						"children" :
						(
							{ "name":"TitleName", "type":"text", "x":7, "y":2, "text":uiScriptLocale.INVENTORY_TITLE, "text_horizontal_align":"left" },
						),
					},

					## Equipment Slot
					{
						"name" : "Equipment_Base",
						"type" : "image",

						"x" : 1,
						"y" : 33,

						"image" : RESOURCE + "equipment_bg.tga",

						"children" :
						(

							{
								"name" : "EquipmentSlot",
								"type" : "slot",

								"x" : 3,
								"y" : 3,

								"width" : 150,
								"height" : 182,

								"slot" : (
											{"index":EQUIPMENT_START_INDEX+0, "x":45, "y":42, "width":32, "height":64},
											{"index":EQUIPMENT_START_INDEX+1, "x":45, "y":6, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+2, "x":45, "y":156, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+3, "x":90, "y":73, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+4, "x":2, "y":12, "width":32, "height":96},
											{"index":EQUIPMENT_START_INDEX+5, "x":131, "y":79, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+6, "x":131, "y":47, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+7, "x":2, "y":157, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+8, "x":90, "y":157, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+9, "x":131, "y":12, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+10, "x":90, "y":44, "width":32, "height":32},
											## 새 반지1
											##{"index":item.EQUIPMENT_RING1, "x":2, "y":106, "width":32, "height":32},
											## 새 반지2
											##{"index":item.EQUIPMENT_RING2, "x":75, "y":106, "width":32, "height":32},
											## 새 벨트
											{"index":item.EQUIPMENT_BELT, "x":39, "y":106, "width":32, "height":32},
										),
							},
							## Dragon Soul Button
							{
								"name" : "DSSButton",
								"type" : "button",

								"x" : 129,
								"y" : 121,

								"tooltip_text" : uiScriptLocale.TASKBAR_DRAGON_SOUL,

								"default_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_01.tga",
								"over_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_02.tga",
								"down_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_03.tga",
							},
							## MallButton
							{
								"name" : "MallButton",
								"type" : "button",

								"x" : 132,
								"y" : 157,

								"tooltip_text" : uiScriptLocale.MALL_TITLE,

								"default_image" : RESOURCE + "mall_button_01.tga",
								"over_image" : RESOURCE + "mall_button_02.tga",
								"down_image" : RESOURCE + "mall_button_03.tga",
							},
							## CostumeButton
							{
								"name" : "CostumeButton",
								"type" : "button",

								"x" : 93,
								"y" : 14,

								"tooltip_text" : uiScriptLocale.COSTUME_TITLE,

								"default_image" : RESOURCE + "costume_button_01.tga",
								"over_image" : RESOURCE + "costume_button_02.tga",
								"down_image" : RESOURCE + "costume_button_03.tga",
							},			
							{
								"name" : "Equipment_Tab_01",
								"type" : "radio_button",

								"x" : 86,
								"y" : 161,

								"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
								"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
								"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",

								"children" :
								(
									{
										"name" : "Equipment_Tab_01_Print",
										"type" : "text",

										"x" : 0,
										"y" : 0,

										"all_align" : "center",

										"text" : "I",
									},
								),
							},
							{
								"name" : "Equipment_Tab_02",
								"type" : "radio_button",

								"x" : 86 + 32,
								"y" : 161,

								"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
								"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
								"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",

								"children" :
								(
									{
										"name" : "Equipment_Tab_02_Print",
										"type" : "text",

										"x" : 0,
										"y" : 0,

										"all_align" : "center",

										"text" : "II",
									},
								),
							},

						),
					},

					{
						"name" : "sidebar",
						"type" : "image",

						"x" : 1,
						"y" : 36 + 191,

						"width" : 170,
						"height" : 26,

						"image" : RESOURCE + "inventory_decoration.tga",

						"children" :
						(

							{
								"name" : "Inventory_Tab_01",
								"type" : "radio_button",

								"x" : 4,
								"y" : 0,

								"default_image" : RESOURCE + "btn_normal.tga",
								"over_image" : RESOURCE + "btn_active.tga",
								"down_image" : RESOURCE + "btn_active.tga",
								"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_1,

								"children" :
								(
									{
										"name" : "Inventory_Tab_01_Print",
										"type" : "text",

										"x" : 0,
										"y" : 0,

										"all_align" : "center",

										"text" : "I",
									},
								),
							},
							{
								"name" : "Inventory_Tab_02",
								"type" : "radio_button",

								"x" : 5 + 32,
								"y" : 0,

								"default_image" : RESOURCE + "btn_normal.tga",
								"over_image" : RESOURCE + "btn_active.tga",
								"down_image" : RESOURCE + "btn_active.tga",
								"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,

								"children" :
								(
									{
										"name" : "Inventory_Tab_02_Print",
										"type" : "text",

										"x" : 0,
										"y" : 0,

										"all_align" : "center",

										"text" : "II",
									},
								),
							},
							{
								"name" : "Inventory_Tab_03",
								"type" : "radio_button",

								"x" : 6 + 32*2,
								"y" : 0,

								"default_image" : RESOURCE + "btn_normal.tga",
								"over_image" : RESOURCE + "btn_active.tga",
								"down_image" : RESOURCE + "btn_active.tga",
								"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_3,

								"children" :
								(
									{
										"name" : "Inventory_Tab_03_Print",
										"type" : "text",

										"x" : 0,
										"y" : 0,

										"all_align" : "center",

										"text" : "III",
									},
								),
							},
							{
								"name" : "Inventory_Tab_04",
								"type" : "radio_button",

								"x" : 7 + 32*3,
								"y" : 0,

								"default_image" : RESOURCE + "btn_normal.tga",
								"over_image" : RESOURCE + "btn_active.tga",
								"down_image" : RESOURCE + "btn_active.tga",
								"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_4,

								"children" :
								(
									{
										"name" : "Inventory_Tab_04_Print",
										"type" : "text",

										"x" : 0,
										"y" : 0,

										"all_align" : "center",

										"text" : "IV",
									},
								),
							},
							{
								"name" : "Inventory_Tab_05",
								"type" : "radio_button",

								"x" : 8 + 32*4,
								"y" : 0,

								"default_image" : RESOURCE + "btn_normal.tga",
								"over_image" : RESOURCE + "btn_active.tga",
								"down_image" : RESOURCE + "btn_active.tga",
								"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_5,

								"children" :
								(
									{
										"name" : "Inventory_Tab_05_Print",
										"type" : "text",

										"x" : 0,
										"y" : 0,

										"all_align" : "center",

										"text" : "V",
									},
								),
							},
							{
								"name" : "separator_medium",
								"type" : "image",

								"x" : 0,
								"y" : 20,

								"width" : 230,
								"height" : 13,

								"image": "%s/separator-medium.tga" % PATCH_COMMON,

								"horizontal_align" : "center",
							},
						),
					},

					## Item Slot
					{
						"name" : "ItemSlot",
						"type" : "grid_table",

						"x" : 4,
						"y" : 258,

						"start_index" : 0,
						"x_count" : 5,
						"y_count" : 9,
						"x_step" : 33,
						"y_step" : 33,

						"image" : RESOURCE + "slot_base.tga",
					},

					## Print
					{
						"name":"Money_Slot",
						"type":"button",

						"x":8,
						"y":22,

						"horizontal_align":"center",
						"vertical_align":"bottom",

						"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
						"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
						"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",

						"children" :
						(
							{
								"name":"Money_Icon",
								"type":"image",

								"x":-18,
								"y":2,

								"image":"d:/ymir work/ui/game/windows/money_icon.sub",
							},

							{
								"name" : "Money",
								"type" : "text",

								"x" : 3,
								"y" : 3,

								"horizontal_align" : "right",
								"text_horizontal_align" : "right",

								"text" : "123456789",
							},
						),
					},

				),
			},
		),
	}
else:
	window = {
		"name" : "InventoryWindow",

		## 600 - (width + ¿À¸¥ÂÊÀ¸·Î ºÎÅÍ ¶ç¿ì±â 24 px)
		"x" : SCREEN_WIDTH - 176,
		"y" : SCREEN_HEIGHT - 37 - 565,

		"style" : ("movable", "float",),

		"width" : 176,
		"height" : 565,

		"children" :
		(
			## Inventory, Equipment Slots
			{
				"name" : "board",
				"type" : "board",
				"style" : ("attach",),

				"x" : 0,
				"y" : 0,

				"width" : 176,
				"height" : 565,

				"children" :
				(
					## Title
					{
						"name" : "TitleBar",
						"type" : "titlebar",
						"style" : ("attach",),

						"x" : 8,
						"y" : 7,

						"width" : 161,
						"color" : "yellow",

						"children" :
						(
							{ "name":"TitleName", "type":"text", "x":77, "y":3, "text":uiScriptLocale.INVENTORY_TITLE, "text_horizontal_align":"center" },
						),
					},

					## Equipment Slot
					{
						"name" : "Equipment_Base",
						"type" : "image",

						"x" : 10,
						"y" : 33,

						"image" : "d:/ymir work/ui/equipment_bg.tga",

						"children" :
						(

							{
								"name" : "EquipmentSlot",
								"type" : "slot",

								"x" : 3,
								"y" : 3,

								"width" : 150,
								"height" : 182,

								"slot" : (
											{"index":EQUIPMENT_START_INDEX+0, "x":39, "y":37, "width":32, "height":64},
											{"index":EQUIPMENT_START_INDEX+1, "x":39, "y":2, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+2, "x":39, "y":145, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+3, "x":75, "y":67, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+4, "x":3, "y":3, "width":32, "height":96},
											{"index":EQUIPMENT_START_INDEX+5, "x":114, "y":67, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+6, "x":114, "y":35, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+7, "x":2, "y":145, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+8, "x":75, "y":145, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+9, "x":114, "y":2, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+10, "x":75, "y":35, "width":32, "height":32},
											## »õ ¹ÝÁö1
											##{"index":item.EQUIPMENT_RING1, "x":2, "y":106, "width":32, "height":32},
											## »õ ¹ÝÁö2
											##{"index":item.EQUIPMENT_RING2, "x":75, "y":106, "width":32, "height":32},
											## »õ º§Æ®
											{"index":item.EQUIPMENT_BELT, "x":39, "y":106, "width":32, "height":32},
										),
							},
							## Dragon Soul Button
							{
								"name" : "DSSButton",
								"type" : "button",

								"x" : 114,
								"y" : 107,

								"tooltip_text" : uiScriptLocale.TASKBAR_DRAGON_SOUL,

								"default_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_01.tga",
								"over_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_02.tga",
								"down_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_03.tga",
							},
							## MallButton
							{
								"name" : "MallButton",
								"type" : "button",

								"x" : 118,
								"y" : 148,

								"tooltip_text" : uiScriptLocale.MALL_TITLE,

								"default_image" : "d:/ymir work/ui/game/TaskBar/Mall_Button_01.tga",
								"over_image" : "d:/ymir work/ui/game/TaskBar/Mall_Button_02.tga",
								"down_image" : "d:/ymir work/ui/game/TaskBar/Mall_Button_03.tga",
							},
							## CostumeButton
							{
								"name" : "CostumeButton",
								"type" : "button",

								"x" : 78,
								"y" : 5,

								"tooltip_text" : uiScriptLocale.COSTUME_TITLE,

								"default_image" : "d:/ymir work/ui/game/taskbar/costume_Button_01.tga",
								"over_image" : "d:/ymir work/ui/game/taskbar/costume_Button_02.tga",
								"down_image" : "d:/ymir work/ui/game/taskbar/costume_Button_03.tga",
							},			
							{
								"name" : "Equipment_Tab_01",
								"type" : "radio_button",

								"x" : 86,
								"y" : 161,

								"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
								"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
								"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",

								"children" :
								(
									{
										"name" : "Equipment_Tab_01_Print",
										"type" : "text",

										"x" : 0,
										"y" : 0,

										"all_align" : "center",

										"text" : "I",
									},
								),
							},
							{
								"name" : "Equipment_Tab_02",
								"type" : "radio_button",

								"x" : 86 + 32,
								"y" : 161,

								"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
								"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
								"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",

								"children" :
								(
									{
										"name" : "Equipment_Tab_02_Print",
										"type" : "text",

										"x" : 0,
										"y" : 0,

										"all_align" : "center",

										"text" : "II",
									},
								),
							},

						),
					},

					{
						"name" : "Inventory_Tab_01",
						"type" : "radio_button",

						"x" : 7,
						"y" : 33 + 191,

						"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
						"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
						"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
						"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_1,

						"children" :
						(
							{
								"name" : "Inventory_Tab_01_Print",
								"type" : "text",

								"x" : 0,
								"y" : 0,

								"all_align" : "center",

								"text" : "I",
							},
						),
					},
					{
						"name" : "Inventory_Tab_02",
						"type" : "radio_button",

						"x" : 7 + 32,
						"y" : 33 + 191,

						"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
						"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
						"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
						"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,

						"children" :
						(
							{
								"name" : "Inventory_Tab_02_Print",
								"type" : "text",

								"x" : 0,
								"y" : 0,

								"all_align" : "center",

								"text" : "II",
							},
						),
					},
					{
						"name" : "Inventory_Tab_03",
						"type" : "radio_button",

						"x" : 7 + 32*2,
						"y" : 33 + 191,

						"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
						"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
						"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
						"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_3,

						"children" :
						(
							{
								"name" : "Inventory_Tab_03_Print",
								"type" : "text",

								"x" : 0,
								"y" : 0,

								"all_align" : "center",

								"text" : "III",
							},
						),
					},
					{
						"name" : "Inventory_Tab_04",
						"type" : "radio_button",

						"x" : 7 + 32*3,
						"y" : 33 + 191,

						"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
						"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
						"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
						"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_4,

						"children" :
						(
							{
								"name" : "Inventory_Tab_04_Print",
								"type" : "text",

								"x" : 0,
								"y" : 0,

								"all_align" : "center",

								"text" : "IV",
							},
						),
					},
					{
						"name" : "Inventory_Tab_05",
						"type" : "radio_button",

						"x" : 7 + 32*4,
						"y" : 33 + 191,

						"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
						"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
						"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
						"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_5,

						"children" :
						(
							{
								"name" : "Inventory_Tab_05_Print",
								"type" : "text",

								"x" : 0,
								"y" : 0,

								"all_align" : "center",

								"text" : "V",
							},
						),
					},

					## Item Slot
					{
						"name" : "ItemSlot",
						"type" : "grid_table",

						"x" : 8,
						"y" : 246,

						"start_index" : 0,
						"x_count" : 5,
						"y_count" : 9,
						"x_step" : 32,
						"y_step" : 32,

						"image" : "d:/ymir work/ui/public/Slot_Base.sub"
					},

					## Print
					{
						"name":"Money_Slot",
						"type":"button",

						"x":8,
						"y":28,

						"horizontal_align":"center",
						"vertical_align":"bottom",

						"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
						"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
						"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",

						"children" :
						(
							{
								"name":"Money_Icon",
								"type":"image",

								"x":-18,
								"y":2,

								"image":"d:/ymir work/ui/game/windows/money_icon.sub",
							},

							{
								"name" : "Money",
								"type" : "text",

								"x" : 3,
								"y" : 3,

								"horizontal_align" : "right",
								"text_horizontal_align" : "right",

								"text" : "123456789",
							},
						),
					},

				),
			},
		),
	}