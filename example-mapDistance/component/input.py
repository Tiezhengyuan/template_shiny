from shiny import ui

from data.constants import BASEMAPS, CITIES

def select_loc1():
    city_names = sorted(list(CITIES.keys()))
    return ui.input_selectize(
        "loc1",
        "Location 1",
        choices=city_names,
        selected="New York"
    )

def select_loc2():
    city_names = sorted(list(CITIES.keys()))
    return ui.input_selectize(
        "loc2",
        "Location 2",
        choices=city_names,
        selected="London"
    )
    
def select_basemap():
    return ui.input_selectize(
        "basemap",
        "Choose a basemap",
        choices=list(BASEMAPS.keys()),
        selected="WorldImagery",
    )