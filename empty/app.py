'''
'''
from shiny import App, ui

from module import *
from component import *
from data import *

# UI components
app_ui = ui.page_sidebar(
    'demo',
    title="Hello sidebar!",
)

# server modules
def server(input, output, session):
    Server(input, output, session)

app = App(app_ui, server)
