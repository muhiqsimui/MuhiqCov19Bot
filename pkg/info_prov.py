import requests as r

jumlah_positif = ''
jumlah_sembuh = ''
jumlah_meninggal = ''
jumlah_dirawat = ''


def cek_provinsi(nama_provinsi):
    global jumlah_positif, jumlah_sembuh, jumlah_meninggal, jumlah_dirawat

    url = r.get("https://data.covid19.go.id/public/api/prov.json")
    data = url.json()
    for i in data['list_data']:
        if (i['key'] == str(nama_provinsi)):
            # print(i,'\n\n')
            jumlah_positif = i['jumlah_kasus']
            jumlah_sembuh = i['jumlah_sembuh']
            jumlah_meninggal = i['jumlah_meninggal']
            jumlah_dirawat = i['jumlah_dirawat']
