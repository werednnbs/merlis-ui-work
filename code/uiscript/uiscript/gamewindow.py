import uiScriptLocale
import app

if app.ENABLE_WEREDNNBS_UIGAME:
	RESOURCE = "d:/ymir work/ui/gui/common/"

if app.ENABLE_WEREDNNBS_UIGAME:
	window = {
		"name" : "GameWindow",
		"style" : ("not_pick",),

		"x" : 0,
		"y" : 0,

		"width" : SCREEN_WIDTH,
		"height" : SCREEN_HEIGHT,

		"children" :
		(
			{ 
				"name":"HelpButton", 
				"type":"button", 
				"x" : 60,
				"y" : SCREEN_HEIGHT-170 - 45,
				"default_image" : RESOURCE + "btn_bigplus_up.tga",
				"over_image" : RESOURCE + "btn_bigplus_over.tga",
				"down_image" : RESOURCE + "btn_bigplus_down.tga",

				"children" : 
				(
					{ 
						"name":"HelpButtonLabel", 
						"type":"text", 
						"x": 20, 
						"y": 55, 
						"text":uiScriptLocale.GAME_HELP, 
						"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
						"text_horizontal_align":"center" 
					},
				),
			},
			{ 
				"name":"QuestButton", 
				"type":"button", 
				"x" : SCREEN_WIDTH-50-32,
				"y" : SCREEN_HEIGHT-400,
				"default_image" : RESOURCE + "btn_bigplusquest_up.tga",
				"over_image" : RESOURCE + "btn_bigplusquest_over.tga",
				"down_image" : RESOURCE + "btn_bigplusquest_down.tga",

				"children" : 
				(
					{ 
						"name":"QuestButtonLabel", 
						"type":"text", 
						"x": 20, 
						"y": 55, 
						"text":uiScriptLocale.GAME_QUEST, 
						"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
						"text_horizontal_align":"center" 
					},
				),
			},
			{ 
				"name":"StatusPlusButton", 
				"type" : "button", 
				"x" : 60, 
				"y" : SCREEN_HEIGHT-100 - 50, 
				"default_image" : RESOURCE + "skill_plus_button_normal.tga",
				"over_image" : RESOURCE + "skill_plus_button_over.tga",
				"down_image" : RESOURCE + "skill_plus_button_press.tga",

				"children" :
				(
					{ 
						"name":"StatusPlusLabel", 
						"type":"text", 
						"x": 20, 
						"y": 55,
						"text":uiScriptLocale.GAME_STAT_UP, 
						"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
						"text_horizontal_align":"center" 
					},		
				),
			},			
			{ 
				"name":"SkillPlusButton", 
				"type" : "button", 
				"x" : SCREEN_WIDTH-50-32,
				"y" : SCREEN_HEIGHT-100 - 25 - 25,
				"default_image" : RESOURCE + "status_plus_button_normal.tga",
				"over_image" : RESOURCE + "status_plus_button_over.tga",
				"down_image" : RESOURCE + "status_plus_button_press.tga",

				"children" : 
				(
					{ 
						"name":"SkillPlusLabel", 
						"type":"text", 
						"x": 20, 
						"y": 55, 
						"text":uiScriptLocale.GAME_SKILL_UP, 
						"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
						"text_horizontal_align":"center" 
					},	
				),
			},			
			{ 
				"name":"ExitObserver", 
				"type" : "button", 
				"x" : SCREEN_WIDTH-50-32,
				"y" : SCREEN_HEIGHT-170 - 25 - 25 - 25,
				"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
				"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
				"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",

				"children" : 
				(
					{ 
						"name":"ExitObserverButtonName", 
						"type":"text", 
						"x": 20, 
						"y": 55, 
						"text": uiScriptLocale.GAME_EXIT_OBSERVER, 
						"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
						"text_horizontal_align":"center" 
					},	
				),
			},
			{ 
				"name":"BuildGuildBuilding",
				"type" : "button",
				"x" : SCREEN_WIDTH-50-32,
				"y" : SCREEN_HEIGHT-170 - 25 - 25,
				"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
				"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
				"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",

				"children" : 
				(
					{ 
						"name":"BuildGuildBuildingButtonName",
						"type":"text",
						"x": 20,
						"y": 55,
						"text": uiScriptLocale.GUILD_BUILDING_TITLE,
						"r":1.0, "g":1.0, "b":1.0, "a":1.0,
						"text_horizontal_align":"center"
					},	
				),
			},
		),
	}
else:
	window = {
		"name" : "GameWindow",
		"style" : ("not_pick",),

		"x" : 0,
		"y" : 0,

		"width" : SCREEN_WIDTH,
		"height" : SCREEN_HEIGHT,

		"children" :
		(
			{ 
				"name":"HelpButton", 
				"type":"button", 
				"x" : 50,
				"y" : SCREEN_HEIGHT-170,
				"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
				"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
				"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",

				"children" : 
				(
					{ 
						"name":"HelpButtonLabel", 
						"type":"text", 
						"x": 16, 
						"y": 40, 
						"text":uiScriptLocale.GAME_HELP, 
						"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
						"text_horizontal_align":"center" 
					},
				),
			},
			{ 
				"name":"QuestButton", 
				"type":"button", 
				"x" : SCREEN_WIDTH-50-32,
				"y" : SCREEN_HEIGHT-170,
				"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
				"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
				"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",

				"children" : 
				(
					{ 
						"name":"QuestButtonLabel", 
						"type":"text", 
						"x": 16, 
						"y": 40, 
						"text":uiScriptLocale.GAME_QUEST, 
						"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
						"text_horizontal_align":"center" 
					},
				),
			},
			{ 
				"name":"StatusPlusButton", 
				"type" : "button", 
				"x" : 68, 
				"y" : SCREEN_HEIGHT-100, 
				"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
				"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
				"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",

				"children" :
				(
					{ 
						"name":"StatusPlusLabel", 
						"type":"text", 
						"x": 16, 
						"y": 40, 
						"text":uiScriptLocale.GAME_STAT_UP, 
						"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
						"text_horizontal_align":"center" 
					},		
				),
			},			
			{ 
				"name":"SkillPlusButton", 
				"type" : "button", 
				"x" : SCREEN_WIDTH-50-32,
				"y" : SCREEN_HEIGHT-100,
				"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
				"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
				"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",

				"children" : 
				(
					{ 
						"name":"SkillPlusLabel", 
						"type":"text", 
						"x": 16, 
						"y": 40, 
						"text":uiScriptLocale.GAME_SKILL_UP, 
						"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
						"text_horizontal_align":"center" 
					},	
				),
			},			
			{ 
				"name":"ExitObserver", 
				"type" : "button", 
				"x" : SCREEN_WIDTH-50-32,
				"y" : SCREEN_HEIGHT-170,
				"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
				"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
				"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",

				"children" : 
				(
					{ 
						"name":"ExitObserverButtonName", 
						"type":"text", 
						"x": 16, 
						"y": 40, 
						"text": uiScriptLocale.GAME_EXIT_OBSERVER, 
						"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
						"text_horizontal_align":"center" 
					},	
				),
			},
			{ 
				"name":"BuildGuildBuilding",
				"type" : "button",
				"x" : SCREEN_WIDTH-50-32,
				"y" : SCREEN_HEIGHT-170,
				"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
				"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
				"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",

				"children" : 
				(
					{ 
						"name":"BuildGuildBuildingButtonName",
						"type":"text",
						"x": 16,
						"y": 40,
						"text": uiScriptLocale.GUILD_BUILDING_TITLE,
						"r":1.0, "g":1.0, "b":1.0, "a":1.0,
						"text_horizontal_align":"center"
					},	
				),
			},
		),
	}

