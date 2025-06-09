from shiny import ui

def select_variable():
    return ui.input_select(
        "var",
        "Select variable",
        choices=["bill_length_mm", "body_mass_g"]
    )