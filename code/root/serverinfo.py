import app
import localeInfo
import dates
app.ServerName = None

SRV1 = {
	"name":dates.NAME,
	"host":dates.IP,
	"auth1":dates.AUTH,
	"ch1":dates.CH1,
	"ch2":dates.CH2,
	"ch3":dates.CH3,
	"ch4":dates.CH4,
	"ch5":dates.CH5,
	"ch6":dates.CH6,
}

STATE_NONE = "..."

STATE_DICT = {
	0 : "...",
	1 : "NORM",
	2 : "HIGH",
	3 : "FULL"
}

SERVER1_CHANNEL_DICT = {
	1:{"key":11,"name":"Channel 1","ip":SRV1["host"],"tcp_port":SRV1["ch1"],"udp_port":SRV1["ch1"],"state":STATE_NONE,},
	2:{"key":12,"name":"Channel 2","ip":SRV1["host"],"tcp_port":SRV1["ch2"],"udp_port":SRV1["ch2"],"state":STATE_NONE,},
	3:{"key":13,"name":"Channel 3","ip":SRV1["host"],"tcp_port":SRV1["ch3"],"udp_port":SRV1["ch3"],"state":STATE_NONE,},
	4:{"key":14,"name":"Channel 4","ip":SRV1["host"],"tcp_port":SRV1["ch4"],"udp_port":SRV1["ch4"],"state":STATE_NONE,},
	5:{"key":15,"name":"Channel 5","ip":SRV1["host"],"tcp_port":SRV1["ch5"],"udp_port":SRV1["ch5"],"state":STATE_NONE,},
	6:{"key":16,"name":"Channel 6","ip":SRV1["host"],"tcp_port":SRV1["ch6"],"udp_port":SRV1["ch6"],"state":STATE_NONE,},
}


REGION_NAME_DICT = {
	0 : SRV1["name"],
}

REGION_AUTH_SERVER_DICT = {
	0 : {
		1 : { "ip":SRV1["host"], "port":SRV1["auth1"], },
	}
}

REGION_DICT = {
	0 : {
		1 : { "name" :SRV1["name"], "channel" : SERVER1_CHANNEL_DICT, },
	},
}

MARKADDR_DICT = {
	10 : { "ip" : SRV1["host"], "tcp_port" : SRV1["ch1"], "mark" : "10.tga", "symbol_path" : "10", },
}

TESTADDR = { "ip" : SRV1["host"], "tcp_port" : SRV1["ch1"], "udp_port" : SRV1["ch1"], }

#DONE