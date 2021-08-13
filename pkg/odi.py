import requests as r

# Data pemantauan diambil dari API covid Mathdroid

jumlah_positif = ''
jumlah_sembuh = ''
jumlah_meninggal = ''
data = ''


def cek_negara(x):
    x = str.lower(x)
    url_negara = r.get('https://covid19.mathdro.id/api/countries/')
    data_negara = url_negara.json()
    malist = data_negara['countries']
    daftar_negara = []
    for i in malist:
        daftar_negara.append(str.lower(i['name']))
    if x in daftar_negara:
        return True
    else:
        return False

# Ambil data covid dunia


def get_global():
    global jumlah_positif, jumlah_sembuh, jumlah_meninggal, data
    url_global = r.get("https://covid19.mathdro.id/api")
    data = url_global.json()
    jumlah_positif = str(data['confirmed']['value'])
    jumlah_sembuh = str(data['recovered']['value'])
    jumlah_meninggal = str(data['deaths']['value'])


# Ambil data berdasarkan negara


def get_country(countries):
    global jumlah_positif, jumlah_sembuh, jumlah_meninggal, data
    url_countries = r.get(
        'https://covid19.mathdro.id/api/countries/'+countries)
    data = url_countries.json()
    jumlah_positif = str(data['confirmed']['value'])
    jumlah_sembuh = str(data['recovered']['value'])
    jumlah_meninggal = str(data['deaths']['value'])
