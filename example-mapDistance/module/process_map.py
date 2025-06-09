import pandas as pd
import ipyleaflet as L
from shiny import ui
import requests

from data.constants import BASEMAPS, CITIES

class ProcessMap:
    def __init__(self, map: L.Map):
        self.map = map

    def update_marker(self, loc: tuple,  on_move:object, name: str):
        self.remove_layer(name)
        m = L.Marker(location=loc, draggable=True, name=name)
        m.on_move(on_move)
        self.map.add_layer(m)

    def on_move1(self, **kwargs):
        return self.on_move("loc1", **kwargs)

    def on_move2(self, **kwargs):
        return self.on_move("loc2", **kwargs)

    def on_move(self, id, **kwargs):
        '''
        When the markers are moved, update the selectize inputs to include the new
        location (which results in the locations() reactive value getting updated,
        which invalidates any downstream reactivity that depends on it)
        '''
        loc = kwargs["location"]
        loc_str = f"{loc[0]}, {loc[1]}"
        choices = city_names + [loc_str]
        ui.update_selectize(id, selected=loc_str, choices=choices)

    def update_line(self, loc1: tuple, loc2: tuple):
        self.remove_layer("line")
        new_layer = L.Polyline(
            locations=[loc1, loc2],
            color="blue",
            weight=2,
            name="line"
        )
        self.map.add_layer(new_layer)

    def update_basemap(self, basemap: str):
        for layer in self.map.layers:
            if isinstance(layer, L.TileLayer):
                self.map.remove_layer(layer)
        self.map.add_layer(L.basemap_to_tiles(BASEMAPS[basemap]))

    def remove_layer(self, name: str):
        for layer in self.map.layers:
            if layer.name == name:
                self.map.remove_layer(layer)

    @staticmethod
    def loc_str_to_coords(x: str) -> dict:
        '''
        When a marker is moved, the input value gets updated to "lat, lon",
        so we decode that into a dict (and also look up the altitude)
        '''
        latlon = x.split(", ")
        if len(latlon) != 2:
            return {}

        lat = float(latlon[0])
        lon = float(latlon[1])
        try:
            url = 'https://api.open-elevation.com'
            query = (
                f"{url}/api/v1/lookup?locations={lat},{lon}"
            )
            r = requests.get(query).json()
            altitude = r["results"][0]["elevation"]
        except Exception:
            altitude = None

        return {"latitude": lat, "longitude": lon, "altitude": altitude}