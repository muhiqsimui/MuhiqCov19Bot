import requests as r
import folium


def mapping():
    # this is base map
    map = folium.Map(
        caption="Persebaran COVID-19 Indonesia",
        location=[-4.6024846527267131, 113.41765363593119],
        zoom_start=6
    )

    url = r.get("https://data.covid19.go.id/public/api/prov.json")
    data = url.json()
    for i in data['list_data']:
        if i['lokasi'] != None and len(i['lokasi']) == 2:
            folium.Marker(
                location=[i['lokasi']['lat'], i['lokasi']['lon']],

                tooltip="<h5><b> {e} </b></h5> <b>jumlah kasus : {a}</b><br><b>jumlah sembuh : {b}</b><br><b>jumlah meninggal : {c}</b><br><b>jumlah dirawat : {d}</b>".
                format(
                    a=i['jumlah_kasus'], b=i['jumlah_sembuh'], c=i['jumlah_meninggal'], d=i['jumlah_dirawat'], e=i['key']
                ),
                # popup='Default popup Marker1',

                icon=folium.Icon(icon='circle', prefix='fa', color='red')
            ).add_to(map)

            folium.Circle(
                location=[i['lokasi']['lat'], i['lokasi']['lon']],

                radius=i['jumlah_kasus']*0.3,

                tooltip="<h5><b> {e} </b></h5> <b>jumlah kasus : {a}</b><br><b>jumlah sembuh : {b}</b><br><b>jumlah meninggal : {c}</b><br><b>jumlah dirawat : {d}</b>".
                format(
                    a=i['jumlah_kasus'], b=i['jumlah_sembuh'], c=i['jumlah_meninggal'], d=i['jumlah_dirawat'], e=i['key']
                ),

                # tooltip=i['key'],
                color="#e81313",
                fill=True,
                fill_color="#e81313",
            ).add_to(map)

    # map_title = '''<h1 align="center"> Peta Persebaran COVID-19 Indonesia </h1> '''
    # map.get_root().html.add_child(folium.Element(map_title))

    # home = ''' <a href="/"><h4> <<< Back to Home </h4></a> '''
    # map.get_root().html.add_child(folium.Element(home))

    return map._repr_html_()
