
import seaborn as sns
import ipyleaflet as L
from faicons import icon_svg
from geopy.distance import geodesic, great_circle
from shiny import App, reactive, render, ui
from shinywidgets import output_widget, render_widget


from data.constants import BASEMAPS, CITIES
from module.process_map import ProcessMap


def Server(input, output, session):
    # Reactive values to store location information
    loc1 = reactive.value()
    loc2 = reactive.value()
    print(loc1, loc2)

    # Update the reactive values when the selectize inputs change
    @reactive.effect
    def _():
        c1 = ProcessMap.loc_str_to_coords(input.loc1())
        loc1.set(CITIES.get(input.loc1(), c1))
        c2 = ProcessMap.loc_str_to_coords(input.loc2())
        loc2.set(CITIES.get(input.loc2(), c2))

    # Add marker for first location
    @reactive.effect
    def _():
        m = ProcessMap(map.widget)
        m.update_marker(loc1xy(), m.on_move1, "loc1")

    # Add marker for second location
    @reactive.effect
    def _():
        m = ProcessMap(map.widget)
        m.update_marker(loc2xy(), m.on_move2,  "loc2")

    # Add line and fit bounds when either marker is moved
    @reactive.effect
    def _():
        m = ProcessMap(map.widget)
        m.update_line(loc1xy(), loc2xy())

    # If new bounds fall outside of the current view, fit the bounds
    @reactive.effect
    def _():
        l1 = loc1xy()
        l2 = loc2xy()

        lat_rng = [min(l1[0], l2[0]), max(l1[0], l2[0])]
        lon_rng = [min(l1[1], l2[1]), max(l1[1], l2[1])]
        new_bounds = [
            [lat_rng[0], lon_rng[0]],
            [lat_rng[1], lon_rng[1]],
        ]

        b = map.widget.bounds
        if len(b) == 0:
            map.widget.fit_bounds(new_bounds)
        elif (
            lat_rng[0] < b[0][0]
            or lat_rng[1] > b[1][0]
            or lon_rng[0] < b[0][1]
            or lon_rng[1] > b[1][1]
        ):
            map.widget.fit_bounds(new_bounds)

    # Update the basemap
    @reactive.effect
    def _():
        m = ProcessMap(map.widget)
        m.update_basemap(input.basemap())

    # Convenient way to get the lat/lons as a tuple
    @reactive.calc
    def loc1xy():
        return loc1()["latitude"], loc1()["longitude"]

    @reactive.calc
    def loc2xy():
        return loc2()["latitude"], loc2()["longitude"]

    # Circle distance value box
    @render.text
    def great_circle_dist():
        circle = great_circle(loc1xy(), loc2xy())
        return f"{circle.kilometers.__round__(1)} km"

    # Geodesic distance value box
    @render.text
    def geo_dist():
        dist = geodesic(loc1xy(), loc2xy())
        return f"{dist.kilometers.__round__(1)} km"

    @render.text
    def altitude():
        try:
            return f'{loc1()["altitude"] - loc2()["altitude"]} m'
        except TypeError:
            return "N/A (altitude lookup failed)"

    # For performance, render the map once and then perform partial updates
    # via reactive side-effects
    @render_widget
    def map():
        return L.Map(zoom=4, center=(0, 0))