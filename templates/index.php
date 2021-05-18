<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <!-- bootsrap dan js  -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>
  <!-- bootsrap dan js  -->
</head>

<body>

  <div class="container">
    <div class="row">
      <!-- navbar  -->
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" href="#"><img src="https://www.uii.ac.id/wp-content/uploads/2017/04/Logo-UII-Asli.png" alt="" class="card" width="100px"></a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Beranda</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Persebaran</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Edukasi</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Skrining</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Vaksinasi</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Rapid-Test</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="web">Info</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <!-- tutup navbar -->
    </div>
    <div class="row">
      <div class="col">
        <h1>Welcome to Covid-19 Whatsapp Bot</h1>
        <h6>Code By {{ me }}</h6>
        <p>Informatika, Universitas Islam Indonesia</p>
      </div>
    </div>
    <br>

    <div class="row">
      <div class="container">
        <!-- data covid19  -->
        <div class="row">
          <div class="col-md-3">
            <h5>Total Kasus Dunia</h5>
            Total Kasus : {{case_world}}
            <br>
            Sembuh : {{cov_recover_world}}
            <br>
            Meninggal : {{cov_death_world}}

          </div>
          <div class="col-md-3">
            <h5>Total Kasus Indonesia</h5>
            Total Kasus : {{ positifCovid }}
            <br>
            Sembuh : {{ sembuh }}
            <br>
            Meninggal : {{ kematian }}
            <br>
            Kasus Aktif : {{ dirawat }}
          </div>
          <div class="col">
            <h5>Total Kasus Yogyakarta</h5>
            Total kasus : <span id="total_kasus_diy"></span>{{total_diy}}
            <br>
            Sembuh : <span id=sembuh_diy>{{sembuh_diy}}</span>
            <br>
            Meninggal : <span id="meninggal_diy">{{meninggal_diy}}</span>
          </div>
        </div>
        <!-- tutup data covid19 -->
        <br>

        <br>
        <!-- update kasus -->
        <div class="row">
          <div class="col">
            <div class="row">
              <h4>Update Terkini COVID-19 Indonesia</h4>
            </div>
            <div class="row">
              <div class="col">
                <p>Jumlah Positif </p>
              </div>
              <div class="col">
                <p>: {{jp_day}}</p>
              </div>
            </div>
            <div class="row">
              <div class="col">
                <p>Jumlah Meninggal </p>
              </div>
              <div class="col">
                <p>: {{jp_death}}</p>
              </div>
            </div>
            <div class="row">
              <div class="col">
                <p>Jumlah Sembuh </p>
              </div>
              <div class="col">
                <p>: {{jp_recover}}</p>
              </div>
            </div>
            <div class="row">
              <div class="col">
                <p>Jumlah Dirawat</p>
              </div>
              <div class="col">
                <p>: {{jp_treated}}</p>
              </div>
            </div>
            <div class="row">
              Last update : {{jp_date}}
            </div>
          </div>
          <div class="col">
            Debug
          </div>
        </div>
        <!-- tutup update -->
        <br>
        <!-- banner bawah  -->
        <div class="row">
          <div class="col">
            <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="https://covid19.go.id/storage/app/media/slider-oct.png" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img src="https://covid19.go.id/storage/app/media/slider/slidervide.jpeg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img src="https://covid19.go.id/storage/app/media/slider/Banner%20Pendaftaran%20Vaksin%20Lansia-01.jpg" class="d-block w-100" alt="...">
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
          </div>

        </div>
        <!-- tutup banner bawah  -->
      </div>
    </div>

  </div>

</body>

</html>