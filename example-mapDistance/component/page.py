
from shiny import ui

from .input import *

def page1():
    # a navset with two 'panels'.
    return ui.navset_card_underline(
        ui.nav_panel("Plot", ui.output_plot("hist")),
        ui.nav_panel("Table", ui.output_data_frame("penguins_data")),
        footer=select_variable(),
        title="Penguins data",
    )

def page2():
    return ui.navset_card_underline(
        # ui.nav_panel("Plot", ui.output_plot("hist")),
        # ui.nav_panel("Table", ui.output_data_frame("data")),
        # footer=select_variable(),
        title="Penguins data",
    )