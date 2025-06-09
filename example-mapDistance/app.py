'''
https://github.com/posit-dev/py-shiny-templates/blob/main/map-distance/app-core.py
'''
import ipyleaflet as L

from geopy.distance import geodesic, great_circle
from shiny import App, reactive, render, ui
from shinywidgets import output_widget, render_widget

from component import *
from module import *

app_ui = ui.page_sidebar(
    ui.sidebar(
        select_loc1(),
        select_loc2(),
        select_basemap(),
        ui.input_dark_mode(mode="dark"),
    ),
    ui.layout_column_wrap(
        value_circle_dist(),
        value_geo_dist(),
        value_alt_dist(),
        fill=False,
    ),
    ui.card(
        ui.card_header("Map (drag the markers to change locations)"),
        output_widget("map"),
    ),
    title="Location Distance Calculator",
    fillable=True,
    class_="bslib-page-dashboard",
)

def server(input, output, session):
    Server(input, output, session)

app = App(app_ui, server)