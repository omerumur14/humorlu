from random import choice, randint

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
	"hastanede",
]

def uretec():
	if randint(0,1) % 2 == 0:
		return "{}'da {} saatlerinde sağanak {} bekleniyor".format(choice(city), choice(time), choice(naturel_event))
	else:
		return "{} bugün {}'da bir {} görüldü".format(choice(famous), choice(district), choice(place))
