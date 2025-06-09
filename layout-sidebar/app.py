'''
'''
from shiny import App, ui

from module import *
from component import *

# UI components
app_ui = ui.page_sidebar(
    ui.sidebar(
        select_variable(),
        group_spcies(),
        show_rug(),
    ),
    ui.output_plot("hist"),
    title="Hello sidebar!",
)

# server modules
def server(input, output, session):
    Server(input, output, session)

app = App(app_ui, server)
