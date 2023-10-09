import folium
from folium import IFrame
import os
import base64

maps = folium.Map(location=[13.7294363, 100.7785291], zoom_start=16)
route = os.path.join("routes.json")

tooltip = "FBT"
html = """<center>
<h2>ซุ้มวินหน้าหอFBT</h2> 
<br/>
</center> 
<img src="data:image/jpg;base64,{}" style="width:75%;
height=75%
margin-right: 50px">
""".format
pic1 = base64.b64encode(open('./folium_map/images/FBT.jpg', 'rb').read()).decode()
iframe1 = IFrame(html(pic1), width=600, height=400)
popup1 = folium.Popup(iframe1, max_width=650)

marker1 = folium.Marker(location=[13.722430076051083, 100.78016732950607], popup=popup1, tooltip=tooltip).add_to(maps)

tooltip_en = "วินใกล้หอประชุมวิศวะ"
html = """<center>
<h2>วินใกล้หอประชุมวิศวะ</h2> 
<br/>
</center> 
<img src="data:image/jpg;base64,{}" style="width:75%;
height=75%
margin-right: 50px">
""".format
pic2 = base64.b64encode(open('./folium_map/images/engineer1.jpg', 'rb').read()).decode()
iframe2 = IFrame(html(pic2), width=600, height=400)
popup2 = folium.Popup(iframe2, max_width=650)

marker2 = folium.Marker(location=[13.728018637540828, 100.77791790248858], popup=popup2, tooltip=tooltip_en).add_to(maps)

maps.save("./flasksnaja/templates/routemap.html")
