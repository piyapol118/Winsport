import base64
import folium
from folium import IFrame

maps = folium.Map(location=[13.7294363, 100.7785291], zoom_start=16)
click = "กดเพื่อดูรายละเอียด"
html = '''
    <head>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Kanit:wght@800&display=swap" />
    </head>
    <style>
        body {{
            background-color: black;
        }}
    
        * {{
            font-family: 'Kanit';
            text-decoration: none;
        }}
        div {{
            margin-top: 10px;
        }}
        button {{
            cursor: pointer;
            background-color: #ff6600;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            margin-top: 10px;
            transition: 0.5s;
            border-style: none;
        }}

        button:hover {{
            cursor: pointer;
            box-shadow: 0px 0px 2px #ff9900;
            background-color: #f3870b;
            -webkit-transform: scale(1.05);
            transform: translateY(-50%) translateX(-50%);
            transform: scale(1.05);
        }}
        
        .leaflet-popup-content-wrapper {{
            background-color: black;
        }}

    </style>
    <body>
        <center>
            <h2 id="{}" style="color: white;">{}</h2>
            <img src="data:image/jpg;base64,{}" style="width: 95%; border-radius: 10px; margin-top: -10px;" alt="เกิดข้อผิดผลาด">
            <div>
                <a href="{}" target="_blank">
                    <button style="width:95%;">นำทาง</button>
                </a>
                <br>
                <a rel="noopener" href="{}" target="_blank">
                    <button style="width: 48%;">ดูรายละเอียด</button>
                </a>
                <a href="{}" target="_blank">
                    <button style="margin-left: 5px; width: 45%;">เรทราคา</button>
                </a>
            </div>
        </center>
    </body> 
    '''.format

datas = [
    {
        "id": "yaektech",
        "tooltip": "วินแยกเทคโนฯ",
        "image_path": './folium/images2/yaek.jpg',
        "link": "https://www.google.com/maps/place/13%C2%B043'20.8%22N+100%C2%B046'48.6%22E/ \
        @13.7224842,100.7799326,20z/data=!4m4!3m3!8m2!3d13.7224301!4d100.7801673?entry=ttu",
        "location": [13.722430076051083, 100.78016732950607],
        "page": "http://127.0.0.1:5000/third#yaek",
        "rate": "http://127.0.0.1:5000/rate#techno"
    },
    {
        "id": "yaek1",
        "tooltip": "วินแยกพระจอมเกล้าฯ 1",
        "image_path": './folium/images2/cross1.jpg',
        "link": "https://www.google.com/maps/place/13%C2%B043'40.9%22N+100%C2%B046'40.5%22E/ \
        @13.7281008,100.7775868,19z/data=!4m4!3m3!8m2!3d13.7280278!4d100.7779167?entry=ttu",
        "location": [13.728018637540828, 100.77791790248858],
        "page": "http://127.0.0.1:5000/third#cross1",
        "rate": "http://127.0.0.1:5000/rate#4yaek1"

    },
    {
        "id": "yaek2",        
        "tooltip": "วินแยกพระจอมเกล้าฯ 2",
        "image_path": "./folium/images2/cross2.jpg",
        "link": "https://www.google.com/maps/place/13%C2%B043'43.5%22N+100%C2%B046'41.4%22E/ \
        @13.7287292,100.7775981,19z/data=!4m4!3m3!8m2!3d13.72875!4d100.7781667?entry=ttu",
        "location": [13.72874879275372, 100.7781562959654],
        "page": "http://127.0.0.1:5000/third#cross2",
        "rate": "http://127.0.0.1:5000/rate#4yaek2"
    },
    {
        "id": "tueklo",        
        "tooltip": "วินตึก 12 ชั้น",
        "image_path": "./folium/images2/tuek12.jpg",
        "link": "https://www.google.com/maps/place/13%C2%B043'40.8%22N+100%C2%B046'22.7%22E/ \
        @13.7280394,100.7726993,20z/data=!4m4!3m3!8m2!3d13.728!4d100.7729722?entry=ttu",
        "location": [13.7280394,100.7726993],
        "page": "http://127.0.0.1:5000/third#tuek12",
        "rate": "http://127.0.0.1:5000/rate#geygee1"
    },
    {
        "id": "4klong",        
        "tooltip": "วินคลองสี่(4)",
        "image_path": "./folium/images2/klong4.jpg",
        "link": "https://www.google.com/maps/place/13%C2%B043'40.5%22N+100%C2%B046'11.1%22E/ \
        @13.7278775,100.7694966,20z/data=!4m4!3m3!8m2!3d13.7279167!4d100.76975?entry=ttu",
        "location": [13.727919168645144, 100.76975143013294],
        "page": "http://127.0.0.1:5000/third#klong4",
        "rate": "http://127.0.0.1:5000/rate#geygee2"
    },
    {
        "id": "sungthong1",        
        "tooltip": "วินสังข์ทองงาม 1",
        "image_path": "./folium/images2/sangthong1.jpg",
        "link": "https://www.google.com/maps/place/13%C2%B043'40.5%22N+100%C2%B046'03.2%22E/ \
        @13.7279051,100.7673669,20z/data=!4m4!3m3!8m2!3d13.7279167!4d100.7675556?entry=ttu",
        "location": [13.727910195481883, 100.76754962029145],
        "page": "http://127.0.0.1:5000/third#sang1",
        "rate": "http://127.0.0.1:5000/rate#geygee3"
    },
    {
        "id": "sungthong2",        
        "tooltip": "วินสังข์ทองงาม 2",
        "image_path": "./folium/images2/sangthong2.jpg",
        "link": "https://www.google.com/maps/place/13%C2%B043'40.3%22N+100%C2%B045'54.2%22E/ \
        @13.7278793,100.7644521,19z/data=!4m4!3m3!8m2!3d13.7278611!4d100.7650556?entry=ttu",
        "location": [13.727867717247008, 100.76505150931416],
        "page": "http://127.0.0.1:5000/third#sang2",
        "rate": "http://127.0.0.1:5000/rate#geygee4"
    },
    {
        "id": "rnpsuwan",        
        "tooltip": "วินRNP เพลสสุวรรณภูมิ",
        "image_path": "./folium/images2/rnp.jpg",
        "link": "https://www.google.com/maps/place/13%C2%B043'40.2%22N+100%C2%B045'52.0%22E/ \
        @13.7277004,100.7642102,20z/data=!4m4!3m3!8m2!3d13.7278333!4d100.7644444?entry=ttu",
        "location": [13.727840367109678, 100.76443731800089],
        "page": "http://127.0.0.1:5000/third#rnp",
        "rate": "http://127.0.0.1:5000/rate#geygee5"
    },
    {
        "id": "banglang",        
        "tooltip": "วินบ้านกลางสวน",
        "image_path": "./folium/images2/banklang.jpg",
        "link": "https://www.google.com/maps/place/13%C2%B043'40.1%22N+100%C2%B045'48.7%22E/ \
        @13.7276506,100.7632542,20z/data=!4m4!3m3!8m2!3d13.7278167!4d100.7635278?entry=ttu",
        "location": [13.727816731091863, 100.76352784022401],
        "page": "http://127.0.0.1:5000/third#banklang",
        "rate": "http://127.0.0.1:5000/rate#geygee6"

    }
]

for marker in datas:
    id = marker["id"]
    tooltip = marker["tooltip"]
    path = marker["image_path"]
    link = marker["link"]
    location = marker["location"]
    page = marker["page"]
    rate = marker["rate"]

    try:
        with open(path, 'rb') as file:
            image = base64.b64encode(file.read()).decode()
    except FileNotFoundError:
        image = ""

    iframe = IFrame(html(id, tooltip, image, link, page, rate), width=350, height=390)
    popup = folium.Popup(iframe, max_width=350)
    marker = folium.Marker(location=location, popup=popup, tooltip=tooltip, icon=folium.Icon(color='orange', icon='record')).add_to(maps) 

maps.save("./flasksnaja/templates/routemap.html")
