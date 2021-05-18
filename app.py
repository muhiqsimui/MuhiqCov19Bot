from flask import Flask, render_template, request
import requests as r
import json
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

coder = "Muhammad Iqbal"

covdunia = r.get('https://coronavirus-19-api.herokuapp.com/all')
jw = covdunia.json()
cov_total = jw['cases']
cov_death = jw['deaths']
cov_recover = jw['recovered']

# indonesia
resp = r.get('https://data.covid19.go.id/public/api/update.json')
cov_raw = resp.json()
cov_update = cov_raw['update']
# yogyakarta
resp_diy = r.get(
    'https://data.covid19.go.id/public/api/prov_detail_DAERAH_ISTIMEWA_YOGYAKARTA.json')
cov_raw_diy = resp_diy.json()
cov_total_diy = cov_raw_diy['kasus_total']
cov_meninggal_diy = cov_raw_diy['meninggal_dengan_tgl']
cov_sembuh_diy = cov_raw_diy['sembuh_dengan_tgl']


@ app.route("/")
def web():
    return render_template("index.php", cov_death_world=f'{jw["deaths"]}', cov_recover_world=f'{jw["recovered"]}', case_world=f'{jw["cases"]}', sembuh_diy=cov_sembuh_diy, meninggal_diy=cov_meninggal_diy, total_diy=cov_total_diy, me=coder, positifCovid=cov_update['total']['jumlah_positif'], sembuh=cov_update['total']['jumlah_sembuh'], kematian=cov_update['total']['jumlah_meninggal'], dirawat=cov_update['total']['jumlah_dirawat'], jp_day=cov_update['penambahan']['jumlah_positif'], jp_death=cov_update['penambahan']['jumlah_meninggal'], jp_recover=cov_update['penambahan']['jumlah_sembuh'], jp_treated=cov_update['penambahan']['jumlah_dirawat'], jp_date=cov_update['penambahan']['created'])


@ app.route("/web")
def hello():
    cov_vaksin = r.get(
        'https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json')
    vaks = cov_vaksin.json()
    jw = vaks['pemeriksaan']['total']
    text = f"SPESIMEN ANTIGEN : {jw['jumlah_spesimen_antigen']} <br>SPESIMEN PCR :{jw['jumlah_spesimen_pcr_tcm']}"
    return(text)


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
        text = f'\n ==========🚀 *MENU* 🚀==========\n\n Berikut adalah fitur-fitur yang dapat anda gunakan : \n\n 1. Situasi Covid-19 Indonesia \n 2. Apa itu COVID-19 ? \n 3. Apa gejala COVID-19 ? \n 4. Cara melindungi diri dari COVID-19 \n 5. Cara melindungi orang lain dari COVID-19? \n 6. Penggunaan Masker kain? \n 7. Rumah sakit Rujukan COVID-19 \n 8. Apa itu rapid test ?\n 9. Lokasi swab test yogyakarta \n\n Silahkan balas dengan mengetikan angka sesuai Menu'
        # msg.body(f'Halo pengguna, Anda saat ini menggunakan whatsapp bot covid 19, ini adalah project tugas akhir yang dikerjakan oleh Programmer Muhammad Iqbal \n Universitas islam indonesia \n')
        msg.body(text)
        responded = True
    if '1' in pesan:
        text = f"🚀Pantau situasi Covid-19🚀 \n\n *🌎 Global 🌎* \n Kasus Terkonfirmasi : {cov_total} \n Sembuh : {cov_recover} \n Meninggal : {cov_death} \n\n "
        text2 = f"*🇮🇩 Indonesia 🇮🇩* \n Kasus Terkonfirmasi : {cov_update['total']['jumlah_positif']} \n Positif : {cov_update['total']['jumlah_dirawat']}\n Sembuh : {cov_update['total']['jumlah_sembuh']} \n\n"
        text3 = f"*✈ Yogyakarta ✈* \n Kasus Terkonfirmasi : {cov_total_diy}\n Sembuh : {cov_sembuh_diy}\n Meninggal : {cov_meninggal_diy}"
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
        text2 = f"✅ Bekerja, belajar dan beribadah di rumah \n\n✅ Jaga jarak minimal 1 meter dengan siapapun disekitarmu \n\n✅ Saat kamu batuk atau bersin: menjauh dan tutup mulut serta hidung kamu dengan tisu, saputangan atau lipatan siku. Segera buang tisu yang telah kamu pakai ke tempat sampah \n\n✅ Kalau kamu demam, batuk atau tidak enak badan, pakai masker. Jangan lupa ikuti cara pakai masker yang benar \n\n✅ Jika terpaksa beraktivitas di luar rumah, pakailah masker kain, jangan lupa cuci masker kain setiap hari \n\n✅ Jangan pernah meludah sembarangan \n\n✅ Sering cuci tangan pakai sabun dan air mengalir selama minimal 20 detik \n\n✅ Segera hubungi call center 119 atau Rumah Sakit rujukan bila orang terdekatmu mengalami gejala COVID-19"
        msg.body(text+text2)
        responded = True
    if '6' in pesan:
        text2 = f" *🌡Masker Kain🌡* \n\n"
        text = f"Semua orang *harus* menggunakan masker kain jika terpaksa beraktivitas di luar rumah. \n\nKamu bisa menggunakan masker kain tiga lapis yang dapat dicuci dan digunakan berkali-kali, agar masker bedah dan N-95 yang sekali pakai bisa ditujukan untuk petugas medis \n\n*Jangan lupa untuk mencuci masker kain* menggunakan air sabun agar tetap bersih. Penggunaan masker yang keliru justru meningkatkan risiko penularan. Jangan sentuh atau buka-tutup masker saat digunakan. Tetap jaga jarak minimal 1 meter dengan siapapun, jangan sentuh wajah dan cuci tangan pakai sabun sesering mungkin."
        msg.body(text2+text)
        responded = True

    if '7' in pesan:
     # Menampilkan daftar rumah sakit indonesia
        text = f"Menurut data Kementerian Kesehatan saat ini ada 132 Rumah Sakit rujukan di indonesia untuk penanganan kasus COVID-19.\n\n"
        text2 = f"Ketik nama daerah sesuai daerah yang ingin kamu cari tau\nBerikut daftarnya :\n\n"
        text3 = f"1.Aceh\n2.Sumatera Utara\n3.Sumatera Barat\n4.Riau\n5.Kepulauan Riau\n6.Jambi\n7.Sumatera Selatan\n8.Bangka Belitung\n9.Bengkulu\n10.Lampung\n11.DKI Jakarta\n12.Jawa Barat\n13.Banten\n14.Jawa Tengah\n15.Daerah Istimewa Yogyakarta\n16.Jawa Timur\n17.Bali\n18.Nusa Tenggara Barat\n19.Nusa Tenggara Timur\n20.Kalimantan Barat\n21.Kalimantan Tengah\n22.Kalimantan Selatan\n23.Kalimantan Timur\n24.Kalimantan Utara\n25.Gorontalo\n26.Sulawesi Utara\n27.Sulawesi Barat\n28.Sulawesi Tengah\n29. Sulawesi Selatan\n30.Sulawesi Tenggara\n31.Maluku\n32.Maluku Utara\n33.Papua\n34.Papua Barat  \n\n"
        msg.body(text+text2+text3)
        responded = True

    # Tutup Menampilkan daftar rumah sakit indonesia
    if '8' in pesan:
        text = f""
        msg.body(text)
        responded = True
    if '9' in pesan:
        text = f""
        msg.body(text)
        responded = True

    def rs(text):
        pesannya = pesan.title()
        text0 = f"Berikut adalah Rumah Sakit rujukan COVID-19 untuk daerah {pesannya}\n\n"
        msg.body(text0+text)
        responded = True
    # fungsi untuk menampilkan rumah sakit rujukan covid-19 di Indonesia

    def daerah():
        pl = pesan.lower()
        if "aceh" in pl:
            rs(f'a. RSUD Dr Zainoel Abidin\nb. RSU Cut Meutia')
        if "sumatera utara" in pl or "sumut" in pl:
            rs(f'a. RSUP H Adam Malik \nb. RSU Djasamen Saragih \nc. RSU Padang Sidempuan \nd. RSU Kabanjahe \ne. RSUD Tarutung')
        if "sumatera barat" in pl or "sumbar" in pl:
            rs(f"a. RSUP dr M Djamil \nb. RSU Achmad Mochtar")
        if "riau" in pl:
            rs(f"a. RSU Arifin Achmad \nb. RSUD Kota Dumai \nc. RSUD Puri Husada Tembilahan")
        if "kepulauan riau" in pl or "kepri" in pl:
            rs(f"a. RSUD Prov Kep Riau Tanjung Pinang \nb. RSUD Embung Fatimah \nc. RSUD Muhammad Sani Kab Karimun \nd. RS Badan Pengusahaan Batam")
        if "jambi" in pl:
            rs(f"a. RSUD Raden Mattaher")
        if "sumatera selatan" in pl or "sumsel" in pl:
            rs(f"a. RSUP M Hoesin \nb. RS Dr Rivai Abdullah \nc. RSUD Siti Fatimah Prov Sumsel \nd. RSUD Lahat \ne. RSUD Kayuagung")
        if "bangka belitung" in pl:
            rs(f"a. RSUD Depati Hamzah\nb. RSUD dr H Marsidi Judono")
        if "bengkulu" in pl:
            rs(f"a. RSUD M Yunus Bengkulu\nb. RSUD Arga Makmur\nc. RSUD Hasanuddin Damrah Manna")
        if "lampung" in pl:
            rs(f"a. RSUD Dr H Abdul Moeloek \nb. RSUD Ahmad Yani Metro \nc. RSUD Dr H Bob Bazar, SKM \nd. RSUD Mayjen HM Ryacudu")
        if "dki jakarta" in pl or "jakarta" in pl or "dki" in pl:
            rs(f"a. RSPI Prof Dr Sulianti Saroso \nb. RSUP Persahabatan \nc. RSUP Fatmawati \nd. RSUD Cengkareng \ne. RSUD Pasar Minggu \nf. RS Bhayangkara Tk I R Said Sukanto \ng. RSPAD Gatot Soebroto \nh. RSAL dr Mintoharjo")
        if "jawa barat" in pl or "jabar" in pl:
            rs(f"a. RSUP dr Hasan Sadikin \nb. RS Paru Dr HA Rotinsulu \nc. RS Paru dr M Goenawan Partowidigdo \nd. RSUD Gunung Jati Cirebon \ne. RSUD R Syamsudin, SH Sukabumi \nf. RSUD dr Slamet Garut \ng. RSUD Kab Indramayu \nh. RSU Tk II Dustira")
        if "banten" in pl:
            rs(f"a. RSUD Kab Tangerang \nb. RSUD dr Drajat Prawiranegara Serang")
        if "jawa tengah" in pl or "jateng" in pl:
            rs(f"a. RSUP dr Kariadi \nb. RS dr Soeradji Tirtonegoro Klaten \nc. RS Paru dr Ario Wirawan \nd. RSUD Prof Dr Margono Soekarjo \ne. RSUD dr Moewardi Surakarta \nf. RSUD Tidar Magelang \ng. RSUD KRMT Wongsonegoro \nh. RSUD Kardinah Tegal \ni. RSUD Banyumas \nj. RSU dr Loekmonohadi \nk. RSUD Kraton Kab Pekalongan \nl. RSUD dr Soeselo Slawi \nm. RSUD RAA Soewondo Kendal")
        if "daerah istimewa yogyakarta" in pl or "yogyakarta" in pl or "jogja" in pl or "diy" in pl:
            rs(f"a. RSUP dr Sardjito \nb. RSUD Panembahan Senopati Bantul \nc. RSUD Kota Yogyakarta \nd. RSUD Wates")
        if "jawa timur" in pl or "jatim" in pl:
            rs(f"a. RSUD dr Soetomo \nb. RSUD dr Soedono Madiun \nc. RSUD dr Saiful Anwar \nd. RSUD dr Soebandi Jember \ne. RSUD Kab Kediri Pare \nf. RSUD dr R Koesma tuban \ng. RSUD Blambangan \nh. RSUD Dr R Sosodoro Djatikoesoemo \ni. RSUD Dr Iskak Tulungagung \nj. RSUD Sidoarjo \nk. RS Universitas Airlangga")
        if "bali" in pl:
            rs(f"a. RSUP Sanglah \nb. RSUD Sanjiwani Gianyar \nc. RSUD Tabanan \nd. RSUD Kab Buleleng")
        if "nusa tenggara barat" in pl or "ntb" in pl:
            rs(f"a. RSUD NTB \nb. RSUD Kota Bima \nc. RSUD Dr R Sudjono \nd. RSUD HL Manambai Abdul Kadir")
        if "nusa tenggara timur" in pl or "ntt" in pl:
            rs(f"a. RSU Prof dr WZ Johannes \nb. RSU dr TC Hillers Maumere \nc. RSUD Komodo Labuan Bajo")
        if "kalimantan barat" in pl or "kalbar" in pl:
            rs(f"a. RSUD dr Soedarso Pontianak \nb. RSUD dr Abdul Azis Singkawang\nc. RSUD Ade Mohammad Djoen Sintang \nd. RSUD dr Agoesdjam Ketapang")
        if "kalimantan tengah" in pl or "kalteng" in pl:
            rs(f"a. RSUD dr Doris Sylvanus Palangkaraya\nb. RSUD dr Murjani Sampit\nc. RSUD Sultan Imanuddin Pangkalan Bun")
        if "kalimantan selatan" in pl or "kalsel" in pl:
            rs(f"a. RSUD Ulin Banjarmasin\nb. RSUD H Boejasin Pelaihari")
        if "kalimantan timur" in pl or "kaltim" in pl:
            rs(f"a. RSUD Abdul Wahab Sjahrani \nb. RSUD dr Kanujoso Djatiwibowo \nc. RSU Taman Husada Bontang \nd. RSUD Panglima Sebaya \ne. RSUD Aji Muhammad Parikesit")
        if "kalimantan utara" in pl or "kaltara" in pl:
            rs(f"a. RSU Kota Tarakan\nb. RSUD Tanjung Selor")
        if "gorontalo" in pl:
            rs(f"a. RSUD Prod dr H Aloei Saboe")
        if "sulawesi utara" in pl or "sulut" in pl:
            rs(f"a. RSUP Prof dr RD Kandou \nb. RSU Ratatotok Buyat \nc. RSUD Kota Kotamobagu \nd. RSUD dr Sam Ratulangi")
        if "sulawesi barat" in pl or "sulbar" in pl:
            rs(f"a. RSUD Provinsi Sulawesi Barat")
        if "sulawesi tengah" in pl or "sulteng" in pl:
            rs(f"a. RSUD Undata Palu \nb. RSU Anutapura Palu \nc. RSUD Kan Banggai Luwuk \nd. RSU Mokopido Toli-Toli \ne. RSUD Kolonedale")
        if "sulawesi selatan" in pl or "sulsel" in pl:
            rs(f"a. RSUP dr Wahidin Sudirohusodo \nb. RS Dr Tadjudin Chalid, MPH \nc. RSUD Labuang Baji \nd. RSU Andi Makkasau Parepare \ne. RSU Lakipadada Toraja \nf. RSUD Kab Sinjai \ng. RS TK II Pelamonia")
        if "sulawesi tenggara" in pl or "sultara" in pl:
            rs(f"a. RS Bahtera Mas Kendari")
        if "maluku" in pl:
            rs(f"a. RSUP dr J Leimena \nb. RSU Dr M Haulussy Ambon \nc. RSUD dr PP Magretti Saumlaki")
        if "maluku utara" in pl or "malut" in pl:
            rs(f"a. RSUD dr H Chasan Boesoirie")
        if "papua" in pl:
            rs(f"a. RSU Jayapura\nb. RSU Nabire\nc. RSU Merauke")
        if "papua barat" in pl:
            rs(f"a. RSUD Kabupaten Sorong\nb. RSUD Manokwari")

    daerah()
    if responded == False:
        msg.body('Anda bisa ketik Menu untuk mulai menggunakan whatsapp bot covid-19')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
