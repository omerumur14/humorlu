from random import choice, randint

cities = [
	"Ankara",
	"İstanbul",
	"Ordu",
	"Bolu",
	"Trabzon",
]

famous_people = [
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

times = [
	"sabah",
	"akşam",
	"gece",
	"öğle",
]

natural_events = [
	"yağmur",
	"dolu yağışı",
	"kar yağışı",
]

districts = [
	"Aksaray",
	"Avcılar",
	"Gürpınar",
	"Bağcılar",
	"Esenyurt",
]

places = [
	"restoranda",
	"parkta",
	"otogarda",
	"yetimhanede",
	"hastanede",
]
def yazi_tura():
	return choice([True, False])

def uretec():
	if  yazi_tura():
		return "{}'da {} saatlerinde sağanak {} bekleniyor".format(choice(city), choice(time), choice(naturel_event))
	else:
		return "{} bugün {}'da bir {} görüldü".format(choice(famous), choice(district), choice(place))
