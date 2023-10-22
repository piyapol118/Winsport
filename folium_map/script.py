import folium
from folium import IFrame
import os
import base64

maps = folium.Map(location=[13.7294363, 100.7785291], zoom_start=16)
route = os.path.join("routes.json")

tooltip = "FBT"
html = """<center>
<a href="https://www.google.com/maps/dir//13.7225296,100.7802041/@13.7225248,100.7802135,21z?entry=ttu" target="_blank">
<h2>ซุ้มวินหน้าหอFBT</h2>
</a> 
<br/>
</center> 
<img src="data:image/jpg;base64,{}" style="width:75%;
height=75%
margin-right: 50px">
""".format
pic1 = base64.b64encode(open('./folium_map/images/FBT.jpg', 'rb').read()).decode()
iframe1 = IFrame(html(pic1), width=600, height=400)
popup1 = folium.Popup(iframe1, max_width=650)

markFBT = folium.Marker(location=[13.722430076051083, 100.78016732950607], popup=popup1, tooltip=tooltip).add_to(maps)

tooltip_en = "วินตรงข้ามจุดหยุดรถไฟ"
html = """<center>
<a href="https://www.google.com/maps/dir//13.7280591,100.7777959/@13.7279864,100.7777181,21z?entry=ttu" target="_blank">
<h2>วินตรงข้ามจุดหยุดรถไฟ</h2>
</a>
<br/>
</center> 
<img src="data:image/jpg;base64,{}" style="width:75%;
height=75%
margin-right: 50px">
""".format
pic2 = base64.b64encode(open('./folium_map/images/engineer1.jpg', 'rb').read()).decode()
iframe2 = IFrame(html(pic2), width=600, height=400)
popup2 = folium.Popup(iframe2, max_width=650)
marken = folium.Marker(location=[13.728018637540828, 100.77791790248858], popup=popup2, tooltip=tooltip_en).add_to(maps)

marklowson = folium.Marker(location=[13.72874879275372, 100.7781562959654]).add_to(maps)

markke1 = folium.Marker(location=[13.727919168645144, 100.76975143013294]).add_to(maps)

markke2 = folium.Marker(location=[13.727910195481883, 100.76754962029145]).add_to(maps)

markke3 = folium.Marker(location=[13.727867717247008, 100.76505150931416]).add_to(maps)

markke4 = folium.Marker(location=[13.727840367109678, 100.76443731800089]).add_to(maps)

markke5 = folium.Marker(location=[13.727840367109678, 100.76443731800089]).add_to(maps)

markerlast = folium.Marker(location=[13.727816731091863, 100.76352784022401]).add_to(maps)

maps.save("./flasksnaja/templates/routemap.html")
