import uiScriptLocale
import app

ROOT = "d:/ymir work/ui/minimap/"

if app.ENABLE_WEREDNNBS_UIGAME:
	RESOURCE = "d:/ymir work/ui/gui/minimap/"

if app.ENABLE_WEREDNNBS_UIGAME:
	window = {
		"name" : "MiniMap",

		"x" : SCREEN_WIDTH - 145,
		"y" : 10,

		"width" : 159,
		"height" : 181,

		"children" :
		(
			## OpenWindow
			{
				"name" : "OpenWindow",
				"type" : "window",

				"x" : 0,
				"y" : 0,

				"width" : 159,
				"height" : 181,

				"children" :
				(
					{
						"name" : "OpenWindowBGI",
						"type" : "image",
						"x" : -12,
						"y" : -10,
						"image" : RESOURCE + "minimap.tga",
					},
					## MiniMapWindow
					{
						"name" : "MiniMapWindow",
						"type" : "window",

						"x" : 12,
						"y" : 12,

						"width" : 128,
						"height" : 128,
					},
					## En Yakin Isinlayici
					{
						"name" : "Homedir",
						"type" : "button",
						"tooltip_text" : "En yakin alandaki Isinlayiciya goturur.",

						"x" : 10-12,
						"y" : 103-14,


						# "default_image" : "home_norm.tga",
						# "over_image" : "home_tut.tga",
						# "down_image" : "home_bas.tga",
					},
					## ScaleUpButton
					{
						"name" : "ScaleUpButton",
						"type" : "button",

						"x" : 124-12,
						"y" : 110-14,

						"default_image" : RESOURCE + "minimap_scaleup_default.tga",
						"over_image" : RESOURCE + "minimap_scaleup_over.tga",
						"down_image" : RESOURCE + "minimap_scaleup_down.tga",
					},
					## ScaleDownButton
					{
						"name" : "ScaleDownButton",
						"type" : "button",

						"x" : 111-12,
						"y" : 123-14,

						"default_image" : RESOURCE + "minimap_scaledown_default.tga",
						"over_image" : RESOURCE + "minimap_scaledown_over.tga",
						"down_image" : RESOURCE + "minimap_scaledown_down.tga",
					},
					## MiniMapHideButton
					{
						"name" : "MiniMapHideButton",
						"type" : "button",

						"x" : 120-12,
						"y" : 13-14,

						"default_image" : RESOURCE + "minimap_close_default.tga",
						"over_image" : RESOURCE + "minimap_close_over.tga",
						"down_image" : RESOURCE + "minimap_close_down.tga",
					},
					## AtlasShowButton
					{
						"name" : "AtlasShowButton",
						"type" : "button",

						"x" : 21-12,
						"y" : 17-14,

						"default_image" : RESOURCE + "atlas_open_default.tga",
						"over_image" : RESOURCE + "atlas_open_over.tga",
						"down_image" : RESOURCE + "atlas_open_down.tga",
					},
					## ServerInfo
					{
						"name" : "ServerInfo",
						"type" : "text",
						
						"text_horizontal_align" : "center",

						"horizontal_align" : "center",

						"outline" : 1,

						"x" : 0,
						"y" : 150,

						"text" : "",
					},
					## PositionInfo
					{
						"name" : "PositionInfo",
						"type" : "text",
						
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70-3,
						"y" : 153,

						"text" : "",
					},
					## ObserverCount
					{
						"name" : "ObserverCount",
						"type" : "text",
						
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 175,

						"text" : "",
					},
				),
			},
			{
				"name" : "CloseWindow",
				"type" : "window",

				"x" : 0,
				"y" : 0,

				"width" : 132,
				"height" : 48,

				"children" :
				(
					## ShowButton
					{
						"name" : "MiniMapShowButton",
						"type" : "button",

						"x" : 100,
						"y" : 4,

						"default_image" : ROOT + "minimap_open_default.sub",
						"over_image" : ROOT + "minimap_open_default.sub",
						"down_image" : ROOT + "minimap_open_default.sub",
					},
				),
			},
		),
	}
else:
	window = {
		"name" : "MiniMap",

		"x" : SCREEN_WIDTH - 136,
		"y" : 0,

		"width" : 136,
		"height" : 137,

		"children" :
		(
			## OpenWindow
			{
				"name" : "OpenWindow",
				"type" : "window",

				"x" : 0,
				"y" : 0,

				"width" : 136,
				"height" : 137,

				"children" :
				(
					{
						"name" : "OpenWindowBGI",
						"type" : "image",
						"x" : 0,
						"y" : 0,
						"image" : ROOT + "minimap.sub",
					},
					## MiniMapWindow
					{
						"name" : "MiniMapWindow",
						"type" : "window",

						"x" : 4,
						"y" : 5,

						"width" : 128,
						"height" : 128,
					},
					## En Yakın Işınlayıcı
					{
						"name" : "Homedir",
						"type" : "button",
						"tooltip_text" : "En yakin alandaki Isinlayiciya goturur.",

						"x" : 10,
						"y" : 103,


						"default_image" : "home_norm.tga",
						"over_image" : "home_tut.tga",
						"down_image" : "home_bas.tga",
					},
					## ScaleUpButton
					{
						"name" : "ScaleUpButton",
						"type" : "button",

						"x" : 101,
						"y" : 116,

						"default_image" : ROOT + "minimap_scaleup_default.sub",
						"over_image" : ROOT + "minimap_scaleup_over.sub",
						"down_image" : ROOT + "minimap_scaleup_down.sub",
					},
					## ScaleDownButton
					{
						"name" : "ScaleDownButton",
						"type" : "button",

						"x" : 115,
						"y" : 103,

						"default_image" : ROOT + "minimap_scaledown_default.sub",
						"over_image" : ROOT + "minimap_scaledown_over.sub",
						"down_image" : ROOT + "minimap_scaledown_down.sub",
					},
					## MiniMapHideButton
					{
						"name" : "MiniMapHideButton",
						"type" : "button",

						"x" : 111,
						"y" : 6,

						"default_image" : ROOT + "minimap_close_default.sub",
						"over_image" : ROOT + "minimap_close_over.sub",
						"down_image" : ROOT + "minimap_close_down.sub",
					},
					## AtlasShowButton
					{
						"name" : "AtlasShowButton",
						"type" : "button",

						"x" : 12,
						"y" : 12,

						"default_image" : ROOT + "atlas_open_default.sub",
						"over_image" : ROOT + "atlas_open_over.sub",
						"down_image" : ROOT + "atlas_open_down.sub",
					},
					## ServerInfo
					{
						"name" : "ServerInfo",
						"type" : "text",
						
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 140,

						"text" : "",
					},
					## PositionInfo
					{
						"name" : "PositionInfo",
						"type" : "text",
						
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 160,

						"text" : "",
					},
					## ObserverCount
					{
						"name" : "ObserverCount",
						"type" : "text",
						
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 180,

						"text" : "",
					},
				),
			},
			{
				"name" : "CloseWindow",
				"type" : "window",

				"x" : 0,
				"y" : 0,

				"width" : 132,
				"height" : 48,

				"children" :
				(
					## ShowButton
					{
						"name" : "MiniMapShowButton",
						"type" : "button",

						"x" : 100,
						"y" : 4,

						"default_image" : ROOT + "minimap_open_default.sub",
						"over_image" : ROOT + "minimap_open_default.sub",
						"down_image" : ROOT + "minimap_open_default.sub",
					},
				),
			},
		),
	}