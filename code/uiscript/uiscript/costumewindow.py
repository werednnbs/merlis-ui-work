import uiScriptLocale
import item
import app

COSTUME_START_INDEX = item.COSTUME_SLOT_START

if app.ENABLE_WEREDNNBS_UIGAME:
	window = {
		"name" : "CostumeWindow",

		"x" : SCREEN_WIDTH - 175 - 140,
		"y" : SCREEN_HEIGHT - 37 - 565,

		"style" : ("movable", "float",),

		"width" : 116,
		"height" : 170,

		"children" :
		(
			{
				"name" : "board",
				"type" : "board",
				"style" : ("attach",),

				"x" : 0,
				"y" : 0,

				"width" : 116,
				"height" : 170,
				
				"children" :
				(
					## Title
					{
						"name" : "TitleBar",
						"type" : "titlebar",
						"style" : ("attach",),

						"x" : 6,
						"y" : 7,

						"width" : 101,
						"color" : "yellow",

						"children" :
						(
							{ "name":"TitleName", "type":"text", "x":7, "y":3, "text":uiScriptLocale.COSTUME_WINDOW_TITLE, "text_horizontal_align":"left" },
						),
					},

					## Equipment Slot
					{
						"name" : "Costume_Base",
						"type" : "image",

						"x" : 2,
						"y" : 38,
						
						"image" : uiScriptLocale.LOCALE_UISCRIPT_PATH + "costume/costume_bg.jpg",					

						"children" :
						(

							{
								"name" : "CostumeSlot",
								"type" : "slot",

								"x" : 3,
								"y" : 3,

								"width" : 113,
								"height" : 145,

								"slot" : (
											{"index":COSTUME_START_INDEX+0, "x":61, "y":45, "width":32, "height":64},
											{"index":COSTUME_START_INDEX+1, "x":61, "y": 8, "width":32, "height":32},
											{"index":COSTUME_START_INDEX+2, "x":5, "y":145, "width":32, "height":32},
										),
							},
						),
					},

				),
			},
		),
	}
else:
	window = {
		"name" : "CostumeWindow",

		"x" : SCREEN_WIDTH - 175 - 140,
		"y" : SCREEN_HEIGHT - 37 - 565,

		"style" : ("movable", "float",),

		"width" : 140,
		"height" : 180,

		"children" :
		(
			{
				"name" : "board",
				"type" : "board",
				"style" : ("attach",),

				"x" : 0,
				"y" : 0,

				"width" : 140,
				"height" : 180,
				
				"children" :
				(
					## Title
					{
						"name" : "TitleBar",
						"type" : "titlebar",
						"style" : ("attach",),

						"x" : 6,
						"y" : 6,

						"width" : 130,
						"color" : "yellow",

						"children" :
						(
							{ "name":"TitleName", "type":"text", "x":60, "y":3, "text":uiScriptLocale.COSTUME_WINDOW_TITLE, "text_horizontal_align":"center" },
						),
					},

					## Equipment Slot
					{
						"name" : "Costume_Base",
						"type" : "image",

						"x" : 13,
						"y" : 38,
						
						"image" : uiScriptLocale.LOCALE_UISCRIPT_PATH + "costume/costume_bg.jpg",					

						"children" :
						(

							{
								"name" : "CostumeSlot",
								"type" : "slot",

								"x" : 3,
								"y" : 3,

								"width" : 127,
								"height" : 145,

								"slot" : (
											{"index":COSTUME_START_INDEX+0, "x":61, "y":45, "width":32, "height":64},
											{"index":COSTUME_START_INDEX+1, "x":61, "y": 8, "width":32, "height":32},
											{"index":COSTUME_START_INDEX+2, "x":5, "y":145, "width":32, "height":32},
										),
							},
						),
					},

				),
			},
		),
	}