# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 18:06:46 2022

@author: hakan
"""
import pandas as pd
import branca
import folium
import fontawesome as fa 
from branca.element import Template, MacroElement
from flask_project.server import connectToDB
import psycopg2
import psycopg2.extras


def add_map(latitude,longitude,type_basemap):
    basemaps={
    'Google Terrain':folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr='Google',
        name='Google Terrain',
        overlay=True,
        control=True
    ),
        }
    location=[latitude,longitude]
    map=folium.Map(location=location,zoom_start=12,tiles=type_basemap)
    for basemap,tilelyr in basemaps.items():
        basemaps[basemap].add_to(map)
    folium.LayerControl().add_to(map)
    return map
def add_marker(data_frame,mmap):
    print(data_frame)
    for i in range(len(data_frame)):
        html=popup_html(data_frame.iloc[i])
        iframe = branca.element.IFrame(html=html,width=510,height=500)
        popup = folium.Popup(folium.Html(html, script=True), max_width=500)
        if data_frame.loc[i,'querytab']=='museum':
            folium.Marker(
                location=[data_frame.loc[i,'latitude'],data_frame.loc[i,'longitude']],
                popup=popup,
                tooltip="Click Here!",
                icon=folium.Icon(color='orange',prefix='fa',icon='ticket')
                        ).add_to(mmap)

        elif data_frame.loc[i,'querytab']=='historical landmark':
            folium.Marker(
                location=[data_frame.loc[i,'latitude'],data_frame.loc[i,'longitude']],
                popup=popup,
                tooltip="Click Here!",
                icon=folium.Icon(color='brown',prefix='fa',icon='university')
                        ).add_to(mmap)
        elif data_frame.loc[i,'querytab']=='monastery':
            folium.Marker(
                location=[data_frame.loc[i,'latitude'],data_frame.loc[i,'longitude']],
                popup=popup,
                tooltip="Click Here!",
                icon=folium.Icon(color='gray',prefix='fa',icon='sun-o')
                        ).add_to(mmap)
        elif data_frame.loc[i,'querytab']=='castle':
            folium.Marker(
                location=[data_frame.loc[i,'latitude'],data_frame.loc[i,'longitude']],
                popup=popup,
                tooltip="Click Here!",
                icon=folium.Icon(color='red',prefix='fa',icon='shield')
                        ).add_to(mmap)
        elif data_frame.loc[i,'querytab']=='campsite':
            folium.Marker(
                location=[data_frame.loc[i,'latitude'],data_frame.loc[i,'longitude']],
                popup=popup,
                tooltip="Click Here!",
                icon=folium.Icon(color='yellow',prefix='fa',icon='flag')
                        ).add_to(mmap)
        elif data_frame.loc[i,'querytab']=='church':
            folium.Marker(
                location=[data_frame.loc[i,'latitude'],data_frame.loc[i,'longitude']],
                popup=popup,
                tooltip="Click Here!",
                icon=folium.Icon(color='blue',prefix='fa',icon='bell')
                        ).add_to(mmap)
        elif data_frame.loc[i,'querytab']=='parks':
            folium.Marker(
                location=[data_frame.loc[i,'latitude'],data_frame.loc[i,'longitude']],
                popup=popup,
                tooltip="Click Here!",
                icon=folium.Icon(color='green',prefix='fa',icon='tree')
                        ).add_to(mmap)
        elif data_frame.loc[i,'querytab']=='natural beauty spot':
            folium.Marker(
                location=[data_frame.loc[i,'latitude'],data_frame.loc[i,'longitude']],
                popup=popup,
                tooltip="Click Here!",
                icon=folium.Icon(color='pink',prefix='fa',icon='pagelines')
                        ).add_to(mmap)
        else:
            folium.Marker(
                location=[data_frame.loc[i,'latitude'],data_frame.loc[i,'longitude']],
                popup=popup,
                tooltip="Click Here!",
                icon=folium.Icon(color='purple',prefix='fa',icon='child')
                        ).add_to(mmap)
    return mmap


def popup_html(points):
    name=points.loc['name']
    city=points.loc['city']
    street=points.loc['street']
    description=points.loc['description']
    link=points.loc['site']

    left_col_color = "#19a7bd"
    right_col_color = "#f2f0d3"
    
    html = """<!DOCTYPE html>
<html>
<head>
<h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(name) + """
</head>
    <table style="height: 126px; width: 350px;">
<tbody>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">City</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(city) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Street</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(street) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Description</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(description) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Link</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";"><a href="{}", target='_blank'>{}</a></td>""".format(link,link) + """
</tr>
</tbody>
</table>
</html>
"""
    return html

def add_legend(map):
    template = """
    {% macro html(this, kwargs) %}
    
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>jQuery UI Draggable - Default functionality</title>
      <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
    
      <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
      <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
      
      <script>
      $( function() {
        $( "#maplegend" ).draggable({
                        start: function (event, ui) {
                            $(this).css({
                                right: "auto",
                                top: "auto",
                                bottom: "auto"
                            });
                        }
                    });
    });
    
      </script>
    </head>
    <body>
    
     
    <div id='maplegend' class='maplegend' 
        style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
         border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
         
    <div class='legend-title'>Legend</div>
    <div class='legend-scale'>
      <ul class='legend-labels'>
        <li><span style='background:orange;opacity:0.7;'></span>Museum</li>
        <li><span style='background:brown;opacity:0.7;'></span>Historical Landmark</li>
        <li><span style='background:blue;opacity:0.7;'></span>Church</li>
        <li><span style='background:gray;opacity:0.7;'></span>Monastery</li>
        <li><span style='background:red;opacity:0.7;'></span>Castle</li>
        <li><span style='background:yellow;opacity:0.7;'></span>Campsite</li>
        <li><span style='background:green;opacity:0.7;'></span>Parks</li>
        <li><span style='background:pink;opacity:0.7;'></span>Natural Beauty</li>
        <li><span style='background:purple;opacity:0.7;'></span>Others</li>
    
      </ul>
    </div>
    </div>
     
    </body>
    </html>
    
    <style type='text/css'>
      .maplegend .legend-title {
        text-align: left;
        margin-bottom: 5px;
        font-weight: bold;
        font-size: 70%;
        }
      .maplegend .legend-scale ul {
        margin: 0;
        margin-bottom: 5px;
        padding: 0;
        float: left;
        list-style: none;
        }
      .maplegend .legend-scale ul li {
        font-size: 80%;
        list-style: none;
        margin-left: 0;
        line-height: 18px;
        margin-bottom: 2px;
        }
      .maplegend ul.legend-labels li span {
        display: block;
        float: left;
        height: 12px;
        width: 30px;
        margin-right: 5px;
        margin-left: 0;
        border: 0.25 px solid #999;
        }
      .maplegend .legend-source {
        font-size: 80%;
        color: #777;
        clear: both;
        }
      .maplegend a {
        color: #777;
        }
    </style>
    {% endmacro %}"""

    macro = MacroElement()
    macro._template = Template(template)

    return map.get_root().add_child(macro)

def get_poi(poi_type):
    conn=connectToDB()
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cur.execute("select {},name,site,city,street,latitude,longitude,description from attraction").format(poi_type)
    except:
        print('Error executing select')
    results=cur.fetchall()
    return results