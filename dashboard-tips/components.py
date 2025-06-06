
from shiny.express import input, ui

def create_sidebar(bill_rng):
    with ui.sidebar(open="desktop"):
        ui.input_slider(
            "total_bill",
            "Bill amount",
            min=bill_rng[0],
            max=bill_rng[1],
            value=bill_rng,
            pre="$",
        )
        ui.input_checkbox_group(
            "time",
            "Food service",
            ["Lunch", "Dinner"],
            selected=["Lunch", "Dinner"],
            inline=True,
        )
        ui.input_action_button("reset", "Reset filter")
