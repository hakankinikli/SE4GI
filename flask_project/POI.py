# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 18:06:46 2022

@author: hakan
"""
from sqlalchemy import create_engine
import pandas as pd
import geopandas as gpd
from flask import  request,jsonify
from flask_project import db
import branca
import folium


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
def add_marker(dictlist,mmap):
    for point in dictlist:
        html=popup_html(point)
        iframe = branca.element.IFrame(html=html,width=510,height=280)
        popup = folium.Popup(folium.Html(html, script=True), max_width=500)
        if point['querytab']=='museum':
            folium.Marker(
                location=[point['latitude'],point['longitude']],
                popup=popup,
                tooltip="Click Here!",
                icon=folium.Icon(color='red',prefix="fa",icon='university')
                        ).add_to(mmap)

        else:
            folium.Marker(
                location=[point['latitude'],point['longitude']],
                popup=popup,
                tooltip="Click Here!",
                icon=folium.Icon(color='green')
                        ).add_to(mmap)
    return mmap


def popup_html(points):
    name=points['name']
    city=points['city']
    street=points['street']
    description=points['description']
    link=points['site']

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
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(link) + """
</tr>
</tbody>
</table>
</html>
"""
    return html