import uiScriptLocale
import app

ROOT = "d:/ymir work/ui/public/"
if app.ENABLE_WEREDNNBS_UIGAME:
	RESOURCE = "d:/ymir work/ui/gui/party/"

if app.ENABLE_WEREDNNBS_UIGAME:
	window = {
		"name" : "PartyMemeberInfoBoard",

		"x" : 0,
		"y" : 0,

		"width" : 109,
		"height" : 50,

		"children" :
		(

			{
				"name" : "bg_party",
				"type" : "image",
				'style': ('not_pick',),

				"x" : 0,
				"y" : 0,

				"image" : RESOURCE + "bg_party.tga",
			},

			{
				"name" : "CharacterImg",
				"type" : "image",

				"x":21+4,
				"y":0,

				"width"  : 16,
				"height" : 20,

				"image" : "d:/ymir work/ui/gui/character/icon_warrior_m_02.tga",
			},
			{
				"name" : "StateButton",
				"type" : "button",

				"x" : 0+4,
				"y" : 10,

				"default_image" : RESOURCE + "affect/party_state_normal_01.tga",
				"over_image" : RESOURCE + "affect/party_state_normal_02.tga",
				"down_image" : RESOURCE + "affect/party_state_normal_03.tga",
			},

			{
				"name" : "NameSlot",
				'style': ('not_pick',),

				"x" : 25+4,
				"y" : 17,
				"width" : 84,
				"height" : 17,
				##"color" : 0x99000000,

				"children" :
				(
					{
						"name" : "NamePrint",
						"type" : "text",

						"x" : 3,
						"y" : 2,

						"text" : uiScriptLocale.PARTY_MEMBER_INFO_NAME,
					},
				),
			},

			{
				"name" : "Gauge",
				"type" : "gauge",
				"style" : ("not_pick",),

				"x" : -10,
				"y" : 42,
				"width" : 136,
				"color" : "red",
			},

			{
				"name" : "ExperienceImage",
				"type" : "image",

				"x" : 22+1+4,
				"y" : 32,

				"image" : "d:/ymir work/ui/game/windows/party_affect_experience.sub",
			},
			{
				"name" : "AttackerImage",
				"type" : "image",

				"x" : 34+1+4,
				"y" : 32,

				"image" : "d:/ymir work/ui/game/windows/party_affect_attackgrade.sub",
			},
			{
				"name" : "DefenderImage",
				"type" : "image",

				"x" : 46+1+4,
				"y" : 32,

				"image" : "d:/ymir work/ui/game/windows/party_affect_defencegrade.sub",
			},
			{
				"name" : "BufferImage",
				"type" : "image",

				"x" : 34+1+4,
				"y" : 32,

				"image" : "d:/ymir work/ui/game/windows/party_affect_attackgrade.sub",
			},
			{
				"name" : "SkillMasterImage",
				"type" : "image",

				"x" : 46+1+4,
				"y" : 32,

				"image" : "d:/ymir work/ui/game/windows/party_affect_attackgrade.sub",
			},
			{
				"name" : "TimeBonusImage",
				"type" : "image",

				"x" : 58+1+4,
				"y" : 32,

				"image" : "d:/ymir work/ui/game/windows/party_affect_timebonus.sub",
			},
			{
				"name" : "RegenBonus",
				"type" : "image",

				"x" : 70+1+4,
				"y" : 32,

				"image" : "d:/ymir work/ui/game/windows/party_affect_regenbonus.sub",
			},
			{
				"name" : "IncreaseArea150",
				"type" : "image",

				"x" : 82+1+4,
				"y" : 32,

				"image" : "d:/ymir work/ui/game/windows/party_affect_increasearea_150.sub",
			},
			{
				"name" : "IncreaseArea200",
				"type" : "image",

				"x" : 94+1+4,
				"y" : 32,

				"image" : "d:/ymir work/ui/game/windows/party_affect_increasearea_200.sub",
			},

		),
	}
else:
	window = {
		"name" : "PartyMemeberInfoBoard",

		"x" : 0,
		"y" : 0,

		"width" : 106,
		"height" : 36,

		"children" :
		(

			{
				"name" : "StateButton",
				"type" : "button",

				"x" : 0,
				"y" : 0,

				"default_image" : "d:/ymir work/ui/game/windows/party_state_normal_01.sub",
				"over_image" : "d:/ymir work/ui/game/windows/party_state_normal_02.sub",
				"down_image" : "d:/ymir work/ui/game/windows/party_state_normal_03.sub",
			},

			{
				"name" : "NameSlot",
				"type" : "bar",
				"style" : ("not_pick",),

				"x" : 22,
				"y" : 0,
				"width" : 84,
				"height" : 17,
				"color" : 0x99000000,

				"children" :
				(
					{
						"name" : "NamePrint",
						"type" : "text",

						"x" : 3,
						"y" : 2,

						"text" : uiScriptLocale.PARTY_MEMBER_INFO_NAME,
					},
				),
			},

			{
				"name" : "Gauge",
				"type" : "gauge",
				"style" : ("not_pick",),

				"x" : 22,
				"y" : 17,
				"width" : 84,
				"color" : "red",
			},

			{
				"name" : "ExperienceImage",
				"type" : "image",

				"x" : 22,
				"y" : 24,

				"image" : "d:/ymir work/ui/game/windows/party_affect_experience.sub",
			},
			{
				"name" : "AttackerImage",
				"type" : "image",

				"x" : 34,
				"y" : 24,

				"image" : "d:/ymir work/ui/game/windows/party_affect_attackgrade.sub",
			},
			{
				"name" : "DefenderImage",
				"type" : "image",

				"x" : 46,
				"y" : 24,

				"image" : "d:/ymir work/ui/game/windows/party_affect_defencegrade.sub",
			},
			{
				"name" : "BufferImage",
				"type" : "image",

				"x" : 34,
				"y" : 24,

				"image" : "d:/ymir work/ui/game/windows/party_affect_attackgrade.sub",
			},
			{
				"name" : "SkillMasterImage",
				"type" : "image",

				"x" : 46,
				"y" : 24,

				"image" : "d:/ymir work/ui/game/windows/party_affect_attackgrade.sub",
			},
			{
				"name" : "TimeBonusImage",
				"type" : "image",

				"x" : 58,
				"y" : 24,

				"image" : "d:/ymir work/ui/game/windows/party_affect_timebonus.sub",
			},
			{
				"name" : "RegenBonus",
				"type" : "image",

				"x" : 70,
				"y" : 24,

				"image" : "d:/ymir work/ui/game/windows/party_affect_regenbonus.sub",
			},
			{
				"name" : "IncreaseArea150",
				"type" : "image",

				"x" : 82,
				"y" : 24,

				"image" : "d:/ymir work/ui/game/windows/party_affect_increasearea_150.sub",
			},
			{
				"name" : "IncreaseArea200",
				"type" : "image",

				"x" : 94,
				"y" : 24,

				"image" : "d:/ymir work/ui/game/windows/party_affect_increasearea_200.sub",
			},

		),
	}