from shiny import ui
from shinywidgets import output_widget

def reset():
    return ui.input_action_button(
        "reset_tips",
        "Reset filter",
    )

def download():
    return ui.download_button(
        "download_tips",
        "Download table",
    )