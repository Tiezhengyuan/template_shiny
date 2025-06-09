from faicons import icon_svg
from shiny import ui

def value_circle_dist():
    return ui.value_box(
            "Great Circle Distance",
            ui.output_text("great_circle_dist"),
            theme="gradient-blue-indigo",
            showcase=icon_svg("globe"),
    )

def value_geo_dist():
    return ui.value_box(
            "Geodisic Distance",
            ui.output_text("geo_dist"),
            theme="gradient-blue-indigo",
            showcase=icon_svg("ruler"),
    )

def value_alt_dist():
    return ui.value_box(
            "Altitude Difference",
            ui.output_text("altitude"),
            theme="gradient-blue-indigo",
            showcase=icon_svg("mountain"),
    )