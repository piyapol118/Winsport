import base64
import folium
from folium import IFrame

maps = folium.Map(location=[13.7294363, 100.7785291], zoom_start=16)
click = "กดเพื่อดูรายละเอียด"
html = '''
    <style>
        div {{
            margin-top: 40px;
        }}
        button {{
            margin: 30px 0px 0px 30px;
        }}
    </style>
    <body>
        <center>
            <h2>{}</h2>
            <img src="data:image/jpg;base64,{}" style="width: 75%;" alt="เกิดข้อผิดผลาด">
            <div>
                <a href="{}" target="_blank">
                    <button>google</button>
                </a>
                <a rel="noopener" href="{}" target="_blank">
                    <button>ดูรายละเอียด</button>
                </a>
                <button>ราคา</button>
            </div>
        </center>
    </body>
    '''.format

datas = [
    {
        "tooltip": "วินแยกเทคโนฯ",
        "image_path": './folium/images2/yaek.jpg',
        "link": "https://www.google.com/maps/place/13%C2%B043'20.8%22N+100%C2%B046'48.6%22E/ \
        @13.7224842,100.7799326,20z/data=!4m4!3m3!8m2!3d13.7224301!4d100.7801673?entry=ttu",
        "location": [13.722430076051083, 100.78016732950607],
        "page": "http://127.0.0.1:5000/third#yaek" 
    },
    {
        "tooltip": "วินแยกพระจอมเกล้าฯ 1",
        "image_path": './folium/images2/cross1.jpg',
        "link": "https://www.google.com/maps/place/13%C2%B043'40.9%22N+100%C2%B046'40.5%22E/ \
        @13.7281008,100.7775868,19z/data=!4m4!3m3!8m2!3d13.7280278!4d100.7779167?entry=ttu",
        "location": [13.728018637540828, 100.77791790248858],
        "page": "http://127.0.0.1:5000/third#cross1"
    },
    {
        "tooltip": "วินแยกพระจอมเกล้าฯ 2",
        "image_path": "./folium/images2/cross2.jpg",
        "link": "https://www.google.com/maps/place/13%C2%B043'43.5%22N+100%C2%B046'41.4%22E/ \
        @13.7287292,100.7775981,19z/data=!4m4!3m3!8m2!3d13.72875!4d100.7781667?entry=ttu",
        "location": [13.72874879275372, 100.7781562959654],
        "page": "http://127.0.0.1:5000/third#cross2"
    },
    {
        "tooltip": "วินตึก 12 ชั้น",
        "image_path": "./folium/images2/tuek12.jpg",
        "link": "https://www.google.com/maps/place/13%C2%B043'40.8%22N+100%C2%B046'22.7%22E/ \
        @13.7280394,100.7726993,20z/data=!4m4!3m3!8m2!3d13.728!4d100.7729722?entry=ttu",
        "location": [13.7280394,100.7726993],
        "page": "http://127.0.0.1:5000/third#tuek12"
    },
    {
        "tooltip": "วินคลองสี่(4)",
        "image_path": "./folium/images2/klong4.jpg",
        "link": "https://www.google.com/maps/place/13%C2%B043'40.5%22N+100%C2%B046'11.1%22E/ \
        @13.7278775,100.7694966,20z/data=!4m4!3m3!8m2!3d13.7279167!4d100.76975?entry=ttu",
        "location": [13.727919168645144, 100.76975143013294],
        "page": "http://127.0.0.1:5000/third#klong4"
    },
    {
        "tooltip": "วินสังข์ทองงาม 1",
        "image_path": "./folium/images2/sangthong1.jpg",
        "link": "https://www.google.com/maps/place/13%C2%B043'40.5%22N+100%C2%B046'03.2%22E/ \
        @13.7279051,100.7673669,20z/data=!4m4!3m3!8m2!3d13.7279167!4d100.7675556?entry=ttu",
        "location": [13.727910195481883, 100.76754962029145],
        "page": "http://127.0.0.1:5000/third#sang1"
    },
    {
        "tooltip": "วินสังข์ทองงาม 2",
        "image_path": "./folium/images2/sangthong2.jpg",
        "link": "https://www.google.com/maps/place/13%C2%B043'40.3%22N+100%C2%B045'54.2%22E/ \
        @13.7278793,100.7644521,19z/data=!4m4!3m3!8m2!3d13.7278611!4d100.7650556?entry=ttu",
        "location": [13.727867717247008, 100.76505150931416],
        "page": "http://127.0.0.1:5000/third#sang2"
    },
    {
        "tooltip": "วินRNP เพลสสุวรรณภูมิ",
        "image_path": "./folium/images2/rnp.jpg",
        "link": "https://www.google.com/maps/place/13%C2%B043'40.2%22N+100%C2%B045'52.0%22E/ \
        @13.7277004,100.7642102,20z/data=!4m4!3m3!8m2!3d13.7278333!4d100.7644444?entry=ttu",
        "location": [13.727840367109678, 100.76443731800089],
        "page": "http://127.0.0.1:5000/third#rnp"
    },
    {
        "tooltip": "วินบ้านกลางสวน",
        "image_path": "./folium/images2/banklang.jpg",
        "link": "https://www.google.com/maps/place/13%C2%B043'40.1%22N+100%C2%B045'48.7%22E/ \
        @13.7276506,100.7632542,20z/data=!4m4!3m3!8m2!3d13.7278167!4d100.7635278?entry=ttu",
        "location": [13.727816731091863, 100.76352784022401],
        "page": "http://127.0.0.1:5000/third#banklang"
    }
]

for marker in datas:
    tooltip = marker["tooltip"]
    path = marker["image_path"]
    link = marker["link"]
    location = marker["location"]
    page = marker["page"]

    try:
        with open(path, 'rb') as file:
            image = base64.b64encode(file.read()).decode()
    except FileNotFoundError:
        image = ""

    iframe = IFrame(html(tooltip, image, link, page), width=550, height=500)
    popup = folium.Popup(iframe, max_width=650)
    marker = folium.Marker(location=location, popup=popup, tooltip=tooltip).add_to(maps)

maps.save("./flasksnaja/templates/routemap.html")
