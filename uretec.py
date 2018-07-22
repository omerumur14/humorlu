from random import randint

city = [
	"Ankara",
	"İstanbul",
	"Ordu",
	"Bolu",
	"Trabzon",
]

famous = [
	"Hüseyin",
	"Veli",
	"Burcu",
	"Tunahan",
	"Talha",
	"Fatih",
	"Sevilay",
	"Çağrı",
	"Yavuz",
	"Berkay",
	"Melike",
	"Ezgi",
	"Buse",
	"Mustafa",
	"Murat",
	"Bülent",
	"Ömer",
	"Ebru",
	"İsmail",
	"Zehra",
	"Pamir",
]

time = [
	"sabah",
	"akşam",
	"gece",
	"öğle",
]

naturel_event = [
	"yağmur",
	"dolu yağışı",
	"kar yağışı",
]

district = [
	"Aksaray",
	"Avcılar",
	"Gürpınar",
	"Bağcılar",
	"Esenyurt",
]

place = [
	"restoranda",
	"parkta",
	"otogarda",
	"yetimhanede",
	"hastaneda",
]

def uretec():
	if randint(0,1) % 2 == 0:
		return "{}'da {} saatlerinde sağanak {} bekleniyor".format(city[randint(0,4)], time[randint(0, 3)], naturel_event[randint(0,2)])
	else:
		return "{} bugün {}'da bir {} görüldü".format(famous[randint(0,20)], district[randint(0,4)], place[randint(0,4)])
