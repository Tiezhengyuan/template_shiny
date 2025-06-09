'''
'''
from shiny import App, ui

from module import *
from component import *

# UI components
app_ui = ui.page_fillable(
    ui.layout_columns(
        value_msg(),
        value_status(),
        value_update(),
        value_num_msg(),
        col_widths=[6, 2, 2, 2],
        fill=False,
    ),
    ui.layout_columns(
        card_logs(),
        card_summary(),
        col_widths=[8, 4],
    ),
    class_="bslib-page-dashboard",
)

# server modules
def server(input, output, session):
    Server(input, output, session)

app = App(app_ui, server)
