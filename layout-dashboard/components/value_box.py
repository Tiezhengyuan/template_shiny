from shiny import ui
from shinywidgets import output_widget

from .icons import ICONS


def total_tippers():
    return ui.value_box(
        "Total tippers",
        ui.output_ui("total_tippers"),
        showcase=ICONS["user"],
        showcase_layout='left center',
    )

def average_tip():
    return ui.value_box(
        "Average tip",
        ui.output_ui("average_tip"),
        showcase=ICONS["wallet"],
        showcase_layout='left center',
    )

def avarage_bill():
    return ui.value_box(
        "Average bill",
        ui.output_ui("average_bill"),
        showcase=ICONS["currency-dollar"],
        showcase_layout='left center',
    )
