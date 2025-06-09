from shiny import App, ui

from component import *
from module import *


app_ui = ui.page_navbar(
    ui.nav_spacer(),  # Push the navbar items to the right
    ui.nav_panel("Penguins", page1()),
    ui.nav_panel("Page 2", page2()),
    title="Study various data through navbar",
)

def server(input, output, session):
    Server(input, output, session)


app = App(app_ui, server)
