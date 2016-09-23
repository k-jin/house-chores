import http.client, urllib.parse, datetime
week = datetime.date.today().isocalendar()[1]&8
housemates = [
	{"name" : "Mikell", "id" : "13941004"},
	{"name" : "Cooper", "id" : "13850584"},
	{"name" : "Alex", 	"id" : "13802102"},
	{"name" : "Kev", 	"id" : "13850948"},
	{"name" : "Ish", 	"id" : "13197281"},
	{"name" : "Mazeed", "id" : "11985064"},
	{"name" : "Isaac", 	"id" : "11990751"},
	{"name" : "Allan", 	"id" : "12021585"}
]
morning_msg = "@" + housemates[week]["name"] + " take out the trash please :D"
bring_it_home = "@" + housemates[week]["name"] + " bring 'er home"
if datetime.datetime.today().weekday() == 2:
	msg = morning_msg
else: 
	msg = bring_it_home
data = {
	"bot_id" : "1d089fba642aa0577c588837f5",
	"text": msg,
	"attachments": [
		{
			"loci": [[0,len(housemates[week]["name"]) + 1]],
			"type": "mentions",
            "user_ids": [housemates[week]["id"]]
        }
    ]
}

encoded_data = urllib.parse.urlencode(data)

conn = http.client.HTTPSConnection("api.groupme.com")
conn.request("POST", "/v3/bots/post", encoded_data)

response = conn.getresponse()
print(response.status, response.reason)
conn.close()