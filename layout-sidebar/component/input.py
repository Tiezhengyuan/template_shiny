from shiny import ui

def select_variable():
    #input.var()
    return ui.input_select(
            "var",
            "Select variable",
            choices=["bill_length_mm", "body_mass_g"]
        )

def group_spcies():
    # input.species()
    return ui.input_switch(
        "species",
        "Group by species",
        value=True
    )

def show_rug():
    # input.show_rug()
    return ui.input_switch(
        "show_rug",
        "Show Rug",
        value=True
    )