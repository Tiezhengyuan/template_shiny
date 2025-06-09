from shiny import ui
from faicons import icon_svg

def value_msg():
    return ui.value_box(
        "Current Message",
        ui.output_text("cur_message"),
        showcase=icon_svg("comment-dots"),
    )

def value_status():
    return ui.value_box(
        "Current Status",
        ui.output_text("cur_status"),
        showcase=icon_svg("check"),
    )

def value_update():
    return ui.value_box(
        "Last update",
        ui.output_text("last_update"),
        showcase=icon_svg("clock"),
    )

def value_num_msg():
    return ui.value_box(
        "Number of Messages",
        ui.output_text("n_messages"),
        showcase=icon_svg("envelope"),
    )