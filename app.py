from flask import Flask, render_template, request
import requests as r
import json
from twilio.twiml.messaging_response import MessagingResponse
from random import randrange

app = Flask(__name__)

coder = "Muhammad Iqbal"

# ganti variable server jika terjadi eror pada API
# server 1 API Javier Aviles
# server 2 API Mathdroid
server = 1
if(server == 1):
    covdunia = r.get('https://coronavirus-19-api.herokuapp.com/all')
    jw = covdunia.json()
    cov_total = jw['cases']
    cov_death = jw['deaths']
    cov_recover = jw['recovered']
    covduniadet = r.get("https://coronavirus-19-api.herokuapp.com/countries/")
    jg = covduniadet.json()
    cov_total_negara = len(jg)
elif(server == 2):
    covdunia = r.get('https://covid19.mathdro.id/api')
    jw = covdunia.json()
    cov_total = jw['confirmed']['value']
    cov_death = jw['deaths']['value']
    cov_recover = jw['recovered']['value']
    cov_total_negara = 'belum diketahui'

# indonesia
# SERVER 1 DEKONTAMINASI
# SERVER 2 COVID19.GO.ID PEMERINTAH
server_ind = 2

if (server_ind == 1):
    xin = r.get('https://dekontaminasi.com/api/id/covid19/stats')
    cov_raw = xin.json()
    cov_update = cov_raw['numbers']
    cov_ind_case = cov_update['infected']
    cov_ind_reco = cov_update['recovered']
    cov_ind_fatal = cov_update['fatal']
elif(server_ind == 2):
    xin = r.get('https://data.covid19.go.id/public/api/update.json')
    cov_raw = xin.json()
    cov_update = cov_raw['update']
    cov_ind_case = cov_update['total']['jumlah_positif']
    cov_ind_reco = cov_update['total']['jumlah_sembuh']
    cov_ind_fatal = cov_update['total']['jumlah_meninggal']

# # yogyakarta
if (server_ind == 1):
    resp_diy = r.get('https://dekontaminasi.com/api/id/covid19/stats')
    cov_raw_diy = resp_diy.json()
    cov_total_diy = cov_raw_diy['regions'][9]['numbers']['infected']
    cov_meninggal_diy = cov_raw_diy['regions'][9]['numbers']['fatal']
    cov_sembuh_diy = cov_raw_diy['regions'][9]['numbers']['recovered']
    cov_provin = cov_raw_diy['regions']
if (server_ind == 2):
    # BELUM DIPERBAIKI NANTI DISEUASIKAN SAMA BAGIAN COVID.ID PEMERINTAh
    resp_diy = r.get('https://data.covid19.go.id/public/api/prov.json')
    cov_raw_diy = resp_diy.json()
    cov_total_diy = cov_raw_diy['list_data'][9]['jumlah_kasus']
    cov_meninggal_diy = cov_raw_diy['list_data'][9]['jumlah_meninggal']
    cov_sembuh_diy = cov_raw_diy['list_data'][9]['jumlah_sembuh']
    cov_provin = cov_raw_diy['list_data']
# fungsi untuk menampilkan stat tiap provinsi


@ app.route("/")
def web():
    return render_template("index.php", cov_death_world=cov_death, cov_recover_world=cov_recover, case_world=cov_total, me=coder, positifCovid=cov_ind_case, sembuh=cov_ind_reco, kematian=cov_ind_fatal, sembuh_diy=cov_sembuh_diy, meninggal_diy=cov_meninggal_diy, total_diy=cov_total_diy)


@ app.route("/web")
def hello():
    return "ok"


@ app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    pesan = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'menu' in pesan or 'Menu' in pesan or 'MENU' in pesan:
        text = f'\n ==========🚀 *MENU* 🚀==========\n\n Berikut adalah fitur-fitur yang dapat anda gunakan : \n\n 1. Situasi COVID-19 Indonesia \n 2. Apa itu COVID-19 ? \n 3. Apa gejala COVID-19 ? \n 4. Cara melindungi diri dari COVID-19 \n 5. Cara melindungi orang lain dari COVID-19? \n 6. Penggunaan Masker kain? \n 7. Rumah sakit Rujukan COVID-19 \n 8. Edukasi test COVID-19\n 9. SKRINING Mandiri COVID-19 \n\n ketik *NEWS* untuk Berita seputar COVID-19 \n\n Silahkan balas dengan mengetikan angka sesuai Menu'
        # msg.body(f'Halo pengguna, Anda saat ini menggunakan whatsapp bot covid 19, ini adalah project tugas akhir yang dikerjakan oleh Programmer Muhammad Iqbal \n Universitas islam indonesia \n')
        msg.body(text)
        responded = True
    if '1' in pesan:
        text = f"🚀Pantau situasi Covid-19🚀 \n\n *🌎 Global 🌎* \n Kasus Terkonfirmasi : {cov_total} \n Sembuh : {cov_recover} \n Meninggal : {cov_death} \n Total negara : {cov_total_negara} \n\n "
        text2 = f"\n *🇮🇩 Indonesia 🇮🇩* \n Kasus Terkonfirmasi : {cov_ind_case} \n Sembuh : {cov_ind_reco}\n Meninggal : {cov_ind_fatal} \n\n"
        text3 = f"\n *✈ Yogyakarta ✈* \n Kasus Terkonfirmasi : {cov_total_diy}\n Sembuh : {cov_sembuh_diy}\n Meninggal : {cov_meninggal_diy}"
        text4 = f"\n\n Anda dapat pantau provinsi lain cukup dengan ketik nama provinsi anda"
        # msg.media(
        #     "https://infeksiemerging.kemkes.go.id/storage/posts/May2021/ENnufhHVqBJr4JQix8mL.png")
        # tidak pakai gambar karena memperlambat jalannya app
        msg.body(text+text2+text3)
        responded = True
    if '2' in pesan:
        text = f" *✨COVID-19* \nCOVID-19 adalah penyakit menular yang disebabkan oleh jenis coronavirus yang baru ditemukan. Virus baru dan penyakit yang disebabkannya ini tidak dikenal sebelum mulainya wabah di Wuhan, Tiongkok, bulan Desember 2019. \n\nCOVID-19 ini sekarang menjadi sebuah pandemi yang terjadi di banyak negara di seluruh dunia. \n\n sumber: WHO"
        msg.body(text)
        responded = True
    if '3' in pesan:
        text = f" *🚀GEJALA COVID-19🚀* \n\n"
        text2 = f" Gejala-gejala COVID-19 yang paling umum adalah demam, batuk kering, dan rasa lelah. Gejala lainnya yang lebih jarang dan mungkin dialami beberapa pasien meliputi rasa nyeri dan sakit, hidung tersumbat, sakit kepala, konjungtivitis, sakit tenggorokan, diare, kehilangan indera rasa atau penciuman, ruam pada kulit, atau perubahan warna jari tangan atau kaki. Gejala-gejala yang dialami biasanya bersifat ringan dan muncul secara bertahap. Beberapa orang menjadi terinfeksi tetapi hanya memiliki gejala ringan. \n\n"
        text3 = f" Sebagian besar (sekitar 80%) orang yang terinfeksi berhasil pulih tanpa perlu perawatan khusus. Sekitar 1 dari 5 orang yang terinfeksi COVID-19 menderita sakit parah dan kesulitan bernapas. Orang-orang lanjut usia (lansia) dan orang-orang dengan kondisi medis penyerta seperti tekanan darah tinggi, gangguan jantung dan paru-paru, diabetes, atau kanker memiliki kemungkinan lebih besar mengalami sakit lebih serius."
        msg.body(text+text2+text3)
        responded = True
    if '4' in pesan:
        text = f" *🛡️Jaga diri dan keluarga anda dari virus COVID-19🛡️* \n\n"
        text2 = f"✅Tetap di rumah. Bekerja, belajar dan beribadah di rumah \n\n✅ Jika terpaksa keluar rumah karena kebutuhan penting, pakai masker kain, selalu jaga jarak minimal 1 meter dengan orang di lain dan sering cuci tangan pakai sabun atau cairan pembersih tangan (alcohol minimal 60%). \n\n✅ Jangan kontak langsung dengan orang bergejala COVID-19. Lakukan komunikasi via telepon, chat atau video call \n\n✅ Hindari kerumunan \n\n✅ Jangan sentuh mata, hidung dan mulut \n\n✅ Selalu cuci tangan pakai sabun dan air mengalir! Sebelum makan dan menyiapkan makanan, setelah dari toilet, setelah memegang binatang dan sehabis berpergian \n\n✅ Ketika batuk atau bersin, tutup mulut dan hidung dengan siku terlipat atau tisu. Buang langsung tisu ke tempat sampah setelah digunakan \n\n✅ Beritahu petugas kesehatan jika kamu mengalami gejala, pernah kontak erat dengan orang bergejala atau bepergian ke wilayah terjangkit COVID-19 \n\n✅ Jika petugas kesehatan menyatakan kamu harus isolasi diri, maka patuhi agar lekas sembuh dan tidak menulari orang lain \n\n✅ Bersikaplah terbuka tentang statusmu pada orang lain di sekitar. Ini adalah bentuk nyata kepedulianmu pada diri sendiri dan sesama"
        msg.body(text+text2)
        responded = True
    if '5' in pesan:
        text = f"*🛡️Lakukan ini agar kita dapat menghentikan penyebaran virus COVID-19🛡️* \n\n"
        text2 = f"✅Bekerja, belajar dan beribadah di rumah \n\n✅ Jaga jarak minimal 1 meter dengan siapapun disekitarmu \n\n✅ Saat kamu batuk atau bersin: menjauh dan tutup mulut serta hidung kamu dengan tisu, saputangan atau lipatan siku. Segera buang tisu yang telah kamu pakai ke tempat sampah \n\n✅ Kalau kamu demam, batuk atau tidak enak badan, pakai masker. Jangan lupa ikuti cara pakai masker yang benar \n\n✅ Jika terpaksa beraktivitas di luar rumah, pakailah masker kain, jangan lupa cuci masker kain setiap hari \n\n✅ Jangan pernah meludah sembarangan \n\n✅ Sering cuci tangan pakai sabun dan air mengalir selama minimal 20 detik \n\n✅ Segera hubungi call center 119 atau Rumah Sakit rujukan bila orang terdekatmu mengalami gejala COVID-19"
        msg.body(text+text2)
        responded = True
    if '6' in pesan:
        text2 = f" *🌡Masker Kain🌡* \n\n"
        text = f"Semua orang *harus* menggunakan masker kain jika terpaksa beraktivitas di luar rumah. \n\nKamu bisa menggunakan masker kain tiga lapis yang dapat dicuci dan digunakan berkali-kali, agar masker bedah dan N-95 yang sekali pakai bisa ditujukan untuk petugas medis \n\n*Jangan lupa untuk mencuci masker kain* menggunakan air sabun agar tetap bersih. Penggunaan masker yang keliru justru meningkatkan risiko penularan. Jangan sentuh atau buka-tutup masker saat digunakan. Tetap jaga jarak minimal 1 meter dengan siapapun, jangan sentuh wajah dan cuci tangan pakai sabun sesering mungkin."
        msg.body(text2+text)
        responded = True

    def vaksin():
        v_update = r.get("https://vaksincovid19-api.vercel.app/api/vaksin")
        vdata = v_update.json()
        text = f"*🇮🇩 Informasi vaksinasi Indonesia 🇮🇩* \n\nTotal Target Vaksinasi : {vdata['totalsasaran']}\n"
        text2 = f"🎯Target vaksinasi tenaga medis :\n{vdata['sasaranvaksinsdmk']}\n"
        text3 = f"🎯Target vaksinasi lansia :\n{vdata['sasaranvaksinlansia']}\n"
        text4 = f"🎯Target vaksinasi petugas publik :\n{vdata['sasaranvaksinpetugaspublik']}\n\n"
        vaxinasi = f"Progress Vaksinasi \n ✅Vaksinasi Tahap 1 :\n{vdata['vaksinasi1']}\n ✅Vaksinasi Tahap 2 : \n{vdata['vaksinasi2']}\n\n sumber data: dekontaminasi api"
        msg.body(text+text2+text3+text4+vaxinasi)

    if '7' in pesan or 'Vaksin' in pesan or 'vaksin' in pesan or 'Vaksinasi' in pesan or 'vaksinasi' in pesan:
     # Menampilkan daftar rumah sakit indonesia
        vaksin()
        rsx = f".\n\nMenurut data Kementerian Kesehatan saat ini ada 132 Rumah Sakit rujukan di indonesia untuk penanganan kasus COVID-19.\n\n"
        rsx2 = f"Ketik nama daerah sesuai daerah yang ingin kamu cari tau\nBerikut daftarnya :\n\n"
        rsx3 = f"1.Aceh\n2.Sumatera Utara\n3.Sumatera Barat\n4.Riau\n5.Kepulauan Riau\n6.Jambi\n7.Sumatera Selatan\n8.Bangka Belitung\n9.Bengkulu\n10.Lampung\n11.DKI Jakarta\n12.Jawa Barat\n13.Banten\n14.Jawa Tengah\n15.Daerah Istimewa Yogyakarta\n16.Jawa Timur\n17.Bali\n18.Nusa Tenggara Barat\n19.Nusa Tenggara Timur\n20.Kalimantan Barat\n21.Kalimantan Tengah\n22.Kalimantan Selatan\n23.Kalimantan Timur\n24.Kalimantan Utara\n25.Gorontalo\n26.Sulawesi Utara\n27.Sulawesi Barat\n28.Sulawesi Tengah\n29. Sulawesi Selatan\n30.Sulawesi Tenggara\n31.Maluku\n32.Maluku Utara\n33.Papua\n34.Papua Barat  \n\n"
        msg.body(rsx+rsx2+rsx3)
        responded = True

    # Tutup Menampilkan daftar rumah sakit indonesia
    if '8' in pesan:
        title = f"*Edukasi test COVID-19*\n\nUntuk mengetahui kita terjangkit corona atau tidak adalah dengan cara melakukan serangkaian test dari tenaga medis saat ini tersedia berbagai macam test antara lain Rapid Test, SWAB Test, PCR, dan GeNose berikut penjelasannya :\n\n"
        text1 = f" *1.Rapid Test* \nRapid test adalah metode pemeriksaan / tes secara cepat didapatkan hasilnya. Pemeriksaan ini menggunakan alat catridge untuk melihat adanya  antibodi yang ada dalam tubuh ketika ada infeksi virus. \n\n"
        text2 = f" *2.SWAB Test Antigen* \nSwab adalah cara untuk memperoleh bahan pemeriksaan ( sampel ) . Swab dilakukan pada nasofaring dan atau orofarings. Pengambilan ini dilakukan dengan cara mengusap rongga nasofarings  dan atau orofarings dengan menggunakan alat seperti  kapas lidi khusus. \n\n"
        text3 = f" *3.PCR* \nPCR adalah singkatan dari polymerase chain reaction. PCR merupakan metode pemeriksaan virus SARS Co-2 dengan mendeteksi DNA virus. Uji ini akan  didapatkan hasil apakah seseorang positif atau tidak SARS Co-2. Dibanding rapid test, pemeriksaan RT-PCR lebih akurat. Metode ini jugalah yang direkomendasikan WHO untuk mendeteksi Covid-19. Namun akurasi ini dibarengi dengan kerumitan proses dan harga alat yang lebih tinggi. \n\n"
        text4 = f" *4.GeNose*\n Gadjah Mada Electronic Nose COVID-19 (GeNose C19) adalah alat tes diagnostik cepat berbasis kecerdasan buatan untuk mendeteksi COVID-19 melalui embusan napas yang dikembangkan oleh Universitas Gadjah Mada. Orang yang menggunakan alat ini cukup mengembuskan napas ke kantong sekali pakai untuk kemudian dianalisis oleh GeNose dalam waktu tiga menit \n\n"
        msg.body(title+text1+text2+text3+text4)
        responded = True
    if '9' in pesan:
        text = f"Anda dapat melakukan skrining awal COVID-19 dengan mengakses link berikut https://skrining.jogjaprov.go.id/"
        msg.body(text)
        responded = True
    if 'news' in pesan or "News" in pesan or 'berita' in pesan:

        webnews = r.get("https://dekontaminasi.com/api/id/covid19/news")
        datn = webnews.json()
        v = randrange(len(datn))
        text = f"{datn[v]['title']}\n{datn[v]['url']}"
        msg.body(text)
        responded = True

    def prolog():
        text = f"Berikut daftar *Rumah Sakit rujukan COVID-19* \n\n"
        msg.body(text)

    def rs(text):
        msg.body(text)
        responded = True

    def cari(kota):
        prolog()
        # rs_url = r.get("https://dekontaminasi.com/api/id/covid19/hospitals")
        # BACKUP API KALO DOWN
        rs_url = r.get(
            "https://raw.githubusercontent.com/muhiqsimui/PyTraining/main/json/rs.json")
        datrs = rs_url.json()
        for pro in cov_provin:
            if (server_ind == 1):
                if pro['name'] == kota:
                    rs(f".\n *{pro['name']}* \n Kasus :{pro['numbers']['infected']} \n Sembuh : {pro['numbers']['recovered']} \n Meninggal :{pro['numbers']['fatal']}\n\n")
            elif(server_ind == 2):
                kotax=kota.upper()
                if pro['key'] == kotax:
                    rs(f".\n *{pro['key']}* \n Kasus :{pro['jumlah_kasus']} \n Sembuh : {pro['jumlah_sembuh']} \n Meninggal :{pro['jumlah_meninggal']}\n\n")
        for j in datrs:
            # kota=kota.title()
            if j['province'] == kota:
                rs(f".\n\n *{j['province']}* \nKota : {j['region']}\nNama RS :{j['name']}\nTelepon :{j['phone']}\nAlamat RS :{j['address']}\n.\n.")

    def daerah():

        pl = pesan.lower()
        if "aceh" in pl:
            cari("Aceh")
        if "sumatera utara" in pl or "sumut" in pl or "medan" in pl:
            cari('Sumatera Utara')
            # rs(f'a. RSUP H Adam Malik \nb. RSU Djasamen Saragih \nc. RSU Padang Sidempuan \nd. RSU Kabanjahe \ne. RSUD Tarutung')
        if "sumatera barat" in pl or "sumbar" in pl or "padang" in pl:
            cari('Sumatera Barat')
            # rs(f"a. RSUP dr M Djamil \nb. RSU Achmad Mochtar")
        if "kepulauan riau" in pl or "kepri" in pl or "Kep. Riau" in pl or "tanjungpinang" in pl:
            cari('Kep. Riau')
            # rs(f"a. RSUD Prov Kep Riau Tanjung Pinang \nb. RSUD Embung Fatimah \nc. RSUD Muhammad Sani Kab Karimun \nd. RS Badan Pengusahaan Batam")
        if "riau" in pl or "pekanbaru" in pl:
            cari('Riau')
            # rs(f"a. RSU Arifin Achmad \nb. RSUD Kota Dumai \nc. RSUD Puri Husada Tembilahan")

        if "jambi" in pl:
            cari('Jambi')
            # rs(f"a. RSUD Raden Mattaher")
        if "sumatera selatan" in pl or "sumsel" in pl or "palembang" in pl:
            cari('Sumatera Selatan')
            # rs(f"a. RSUP M Hoesin \nb. RS Dr Rivai Abdullah \nc. RSUD Siti Fatimah Prov Sumsel \nd. RSUD Lahat \ne. RSUD Kayuagung")
        if "bangka belitung" in pl or 'Kep. Bangka Belitung' in pl:
            cari('Kep. Bangka Belitung')
            # rs(f"a. RSUD Depati Hamzah\nb. RSUD dr H Marsidi Judono")
        if "bengkulu" in pl:
            cari("Bengkulu")
            # rs(f"a. RSUD M Yunus Bengkulu\nb. RSUD Arga Makmur\nc. RSUD Hasanuddin Damrah Manna")
        if "lampung" in pl:
            cari("Lampung")
            # rs(f"a. RSUD Dr H Abdul Moeloek \nb. RSUD Ahmad Yani Metro \nc. RSUD Dr H Bob Bazar, SKM \nd. RSUD Mayjen HM Ryacudu")
        if "dki jakarta" in pl or "jakarta" in pl or "dki" in pl:
            cari("DKI Jakarta")
            # rs(f"a. RSPI Prof Dr Sulianti Saroso \nb. RSUP Persahabatan \nc. RSUP Fatmawati \nd. RSUD Cengkareng \ne. RSUD Pasar Minggu \nf. RS Bhayangkara Tk I R Said Sukanto \ng. RSPAD Gatot Soebroto \nh. RSAL dr Mintoharjo")
        if "jawa barat" in pl or "jabar" in pl or "bandung" in pl:
            cari("Jawa Barat")
            # rs(f"a. RSUP dr Hasan Sadikin \nb. RS Paru Dr HA Rotinsulu \nc. RS Paru dr M Goenawan Partowidigdo \nd. RSUD Gunung Jati Cirebon \ne. RSUD R Syamsudin, SH Sukabumi \nf. RSUD dr Slamet Garut \ng. RSUD Kab Indramayu \nh. RSU Tk II Dustira")
        if "banten" in pl:
            cari("Banten")
            # rs(f"a. RSUD Kab Tangerang \nb. RSUD dr Drajat Prawiranegara Serang")
        if "jawa tengah" in pl or "jateng" in pl or "semarang" in pl:
            # PROBLEM GK JALAN lebih 1600
            cari("Jawa Tengah")
            # rs(f"a. RSUP dr Kariadi \nb. RS dr Soeradji Tirtonegoro Klaten \nc. RS Paru dr Ario Wirawan \nd. RSUD Prof Dr Margono Soekarjo \ne. RSUD dr Moewardi Surakarta \nf. RSUD Tidar Magelang \ng. RSUD KRMT Wongsonegoro \nh. RSUD Kardinah Tegal \ni. RSUD Banyumas \nj. RSU dr Loekmonohadi \nk. RSUD Kraton Kab Pekalongan \nl. RSUD dr Soeselo Slawi \nm. RSUD RAA Soewondo Kendal")
        if "daerah istimewa yogyakarta" in pl or "yogyakarta" in pl or "jogja" in pl or "diy" in pl:
            cari('DI Yogyakarta')
            # rs(f"a. RSUP dr Sardjito \nb. RSUD Panembahan Senopati Bantul \nc. RSUD Kota Yogyakarta \nd. RSUD Wates")
        if "jawa timur" in pl or "jatim" in pl or "Jawa Timur" in pl or "surabaya" in pl:
            # PROBLEM GK JALAN lebih 1600 karakter
            cari('Jawa Timur')
            # rs(f"a. RSUD dr Soetomo \nb. RSUD dr Soedono Madiun \nc. RSUD dr Saiful Anwar \nd. RSUD dr Soebandi Jember \ne. RSUD Kab Kediri Pare \nf. RSUD dr R Koesma tuban \ng. RSUD Blambangan \nh. RSUD Dr R Sosodoro Djatikoesoemo \ni. RSUD Dr Iskak Tulungagung \nj. RSUD Sidoarjo \nk. RS Universitas Airlangga")
        if "bali" in pl:
            cari('Bali')
            # rs(f"a. RSUP Sanglah \nb. RSUD Sanjiwani Gianyar \nc. RSUD Tabanan \nd. RSUD Kab Buleleng")
        if "nusa tenggara barat" in pl or "ntb" in pl:
            cari('Nusa Tenggara Barat')
            # rs(f"a. RSUD NTB \nb. RSUD Kota Bima \nc. RSUD Dr R Sudjono \nd. RSUD HL Manambai Abdul Kadir")
        if "nusa tenggara timur" in pl or "ntt" in pl:
            cari('Nusa Tenggara Timur')
            # rs(f"a. RSU Prof dr WZ Johannes \nb. RSU dr TC Hillers Maumere \nc. RSUD Komodo Labuan Bajo")
        if "kalimantan barat" in pl or "kalbar" in pl:
            cari('Kalimantan Barat')
            # rs(f"a. RSUD dr Soedarso Pontianak \nb. RSUD dr Abdul Azis Singkawang\nc. RSUD Ade Mohammad Djoen Sintang \nd. RSUD dr Agoesdjam Ketapang")
        if "kalimantan tengah" in pl or "kalteng" in pl:
            cari('Kalimantan Tengah')
            # rs(f"a. RSUD dr Doris Sylvanus Palangkaraya\nb. RSUD dr Murjani Sampit\nc. RSUD Sultan Imanuddin Pangkalan Bun")
        if "kalimantan selatan" in pl or "kalsel" in pl:
            cari('Kalimantan Selatan')
            # rs(f"a. RSUD Ulin Banjarmasin\nb. RSUD H Boejasin Pelaihari")
        if "kalimantan timur" in pl or "kaltim" in pl:
            cari('Kalimantan Timur')
            # rs(f"a. RSUD Abdul Wahab Sjahrani \nb. RSUD dr Kanujoso Djatiwibowo \nc. RSU Taman Husada Bontang \nd. RSUD Panglima Sebaya \ne. RSUD Aji Muhammad Parikesit")
        if "kalimantan utara" in pl or "kaltara" in pl:
            cari('Kalimantan Utara')
            # rs(f"a. RSU Kota Tarakan\nb. RSUD Tanjung Selor")
        if "gorontalo" in pl:
            cari('Gorontalo')
            # rs(f"a. RSUD Prod dr H Aloei Saboe")
        if "sulawesi utara" in pl or "sulut" in pl:
            cari('Sulawesi Utara')
            # rs(f"a. RSUP Prof dr RD Kandou \nb. RSU Ratatotok Buyat \nc. RSUD Kota Kotamobagu \nd. RSUD dr Sam Ratulangi")
        if "sulawesi barat" in pl or "sulbar" in pl:
            cari('Sulawesi Barat')
            # rs(f"a. RSUD Provinsi Sulawesi Barat")
        if "sulawesi tengah" in pl or "sulteng" in pl:
            cari('Sulawesi Tengah')
            # rs(f"a. RSUD Undata Palu \nb. RSU Anutapura Palu \nc. RSUD Kan Banggai Luwuk \nd. RSU Mokopido Toli-Toli \ne. RSUD Kolonedale")
        if "sulawesi selatan" in pl or "sulsel" in pl or "makassar" in pl:
            cari('Sulawesi Selatan')
            # rs(f"a. RSUP dr Wahidin Sudirohusodo \nb. RS Dr Tadjudin Chalid, MPH \nc. RSUD Labuang Baji \nd. RSU Andi Makkasau Parepare \ne. RSU Lakipadada Toraja \nf. RSUD Kab Sinjai \ng. RS TK II Pelamonia")
        if "sulawesi tenggara" in pl or "sultara" in pl:
            cari('Sulawesi Tenggara')
            # rs(f"a. RS Bahtera Mas Kendari")
        if "maluku" in pl:
            cari('Maluku')
            # rs(f"a. RSUP dr J Leimena \nb. RSU Dr M Haulussy Ambon \nc. RSUD dr PP Magretti Saumlaki")
        if "maluku utara" in pl or "malut" in pl:
            cari('Maluku Utara')
            # rs(f"a. RSUD dr H Chasan Boesoirie")
        if "papua" in pl:
            cari('Papua')
            # rs(f"a. RSU Jayapura\nb. RSU Nabire\nc. RSU Merauke")
        if "papua barat" in pl or 'sorong' in pl:
            cari('Papua Barat')
            # rs(f"a. RSUD Kabupaten Sorong\nb. RSUD Manokwari")

    daerah()

    # def daerah():

    #     if 'rs' in pesan:
    #         rs_url = r.get(
    #             "https://dekontaminasi.com/api/id/covid19/hospitals")
    #         datrs = rs_url.json()
    #         text = f"Provinsi :{datrs[9]['province']}\n Kota : {datrs[9]['region']}\nTelepon :{datrs[9]['phone']}\n Telepon :{datrs[9]['phone']}\nAlamat RS :{datrs[9]['address']}"
    #         msg.body(text)
    #     responded = True

    # daerah()
    if responded == False:
        msg.body(
            'Anda bisa ketik *Menu* untuk mulai menggunakan *Whatsapp Bot COVID-19*')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
