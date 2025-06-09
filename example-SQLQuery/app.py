from shiny import App, ui
# from query import query_output_ui

from component import *
from module import *
from data import *


app_ui = ui.page_sidebar(
    ui.sidebar(
        'Select table:',
        weather(),
        metadata(),
        show_help(),
    ),
    ui.tags.div(
        query_output_ui(
            "initial_query",
            remove_id="initial_query"
        ),
        id="module_container",
    ),
    title="DuckDB query explorer",
    class_="bslib-page-dashboard",
)


def server(input, output, session):
    Server(input, output, session)


app = App(app_ui, server)
