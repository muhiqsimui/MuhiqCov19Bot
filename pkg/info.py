import requests as r

# =====================================================================================

# Data pemantauan diambil dari situs resmi indonesia covid19.go.id
url = r.get("https://data.covid19.go.id/public/api/update.json")
data = url.json()


# Data ODP dan PDP
jumlah_odp = str(data['data']['jumlah_odp'])
jumlah_pdp = str(data['data']['jumlah_pdp'])
total_spesimen = str(data['data']['total_spesimen'])
total_spesimen_negatif = str(data['data']['total_spesimen_negatif'])

# Data Covid Indonesia
data_ind = data['update']
jumlah_positif = str(data_ind['total']['jumlah_positif'])
jumlah_dirawat = str(data_ind['total']['jumlah_dirawat'])
jumlah_sembuh = str(data_ind['total']['jumlah_sembuh'])
jumlah_meninggal = str(data_ind['total']['jumlah_meninggal'])


# Update Penambahan Harian
upd_jumlah_positif = str(data_ind['penambahan']['jumlah_positif'])
upd_jumlah_dirawat = str(data_ind['penambahan']['jumlah_dirawat'])
upd_jumlah_sembuh = str(data_ind['penambahan']['jumlah_sembuh'])
upd_jumlah_meninggal = str(data_ind['penambahan']['jumlah_meninggal'])
upd_tanggal = str(data_ind['penambahan']['tanggal'])
upd_created = str(data_ind['penambahan']['created'])

# ===================================================================================

# DATA VAKSINASI
url_vaksinasi = r.get(
    'https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json')
data_vaksinasi = url_vaksinasi.json()

# ==================== DATA TEST PCR/SWAB ==================

# DATA PENAMBAHAN HARIAN TEST PCR/SWAB INDONESIA
penambahan_jumlah_spesimen_pcr_tcm = str(
    data_vaksinasi['pemeriksaan']['penambahan']['jumlah_spesimen_pcr_tcm'])
penambahan_jumlah_spesimen_antigen = str(
    data_vaksinasi['pemeriksaan']['penambahan']['jumlah_spesimen_antigen'])
penambahan_jumlah_orang_pcr_tcm = str(
    data_vaksinasi['pemeriksaan']['penambahan']['jumlah_orang_pcr_tcm'])
penambahan_jumlah_orang_antigen = str(
    data_vaksinasi['pemeriksaan']['penambahan']['jumlah_orang_antigen'])
penambahan_tanggal = str(
    data_vaksinasi['pemeriksaan']['penambahan']['tanggal'])
penambahan_created = str(
    data_vaksinasi['pemeriksaan']['penambahan']['created'])

# TOTAL SWAB PCR INDONESIA
total_jumlah_spesimen_pcr_tcm = str(
    data_vaksinasi['pemeriksaan']['total']['jumlah_spesimen_pcr_tcm'])
total_jumlah_spesimen_antigen = str(
    data_vaksinasi['pemeriksaan']['total']['jumlah_spesimen_antigen'])
total_jumlah_orang_pcr_tcm = str(
    data_vaksinasi['pemeriksaan']['total']['jumlah_orang_pcr_tcm'])
total_jumlah_orang_antigen = str(
    data_vaksinasi['pemeriksaan']['total']['jumlah_orang_antigen'])

# DATA PENAMBAHAN VAKSINASI
pcr_jumlah_vaksinasi_1 = str(
    data_vaksinasi['vaksinasi']['penambahan']['jumlah_vaksinasi_1'])
pcr_jumlah_vaksinasi_2 = str(
    data_vaksinasi['vaksinasi']['penambahan']['jumlah_vaksinasi_2'])
tanggal = str(data_vaksinasi['vaksinasi']['penambahan']['tanggal'])
created = str(data_vaksinasi['vaksinasi']['penambahan']['created'])

# TOTAL DATA YANG TELAH DIVAKSIN
vaksin_jumlah_vaksinasi_1 = str(
    data_vaksinasi['vaksinasi']['penambahan']['jumlah_vaksinasi_1'])
vaksin__jumlah_vaksinasi_2 = str(
    data_vaksinasi['vaksinasi']['penambahan']['jumlah_vaksinasi_2'])
