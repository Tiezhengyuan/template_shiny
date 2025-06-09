import urllib.request
from pathlib import Path

import duckdb
# from query import query_output_server, query_output_ui
from shiny import App, reactive, ui


from component import *
from module import *
from data import *


def Server(input, output, session):
    mod_counter = reactive.value(0)

    query_output_server("initial_query", con=con, remove_id="initial_query")

    @reactive.effect
    @reactive.event(input.weather)
    def _():
        counter = mod_counter.get() + 1
        mod_counter.set(counter)
        id = "query_" + str(counter)
        ui.insert_ui(
            selector="#module_container",
            where="afterBegin",
            ui=query_output_ui(id, remove_id=id),
        )
        query_output_server(id, con=con, remove_id=id)

    @reactive.effect
    @reactive.event(input.metadata)
    def _():
        counter = mod_counter.get() + 1
        mod_counter.set(counter)
        id = "query_" + str(counter)
        query = "SELECT * from information_schema.columns"
        ui.insert_ui(
            selector="#module_container",
            where="afterBegin",
            ui=query_output_ui(
                id, query=query, remove_id=id
            ),
        )
        query_output_server(id, con=con, remove_id=id)
