from shiny import ui

def weather():
    #input.weather()
    return ui.input_action_button(
        "weather",
        "Weather",
        class_="btn btn-primary"
    )

def metadata():
    # input.metadata()
    return ui.input_action_button(
            "metadata",
            "Metadata",
            class_="btn btn-secondary"
        )

def show_help():
    return ui.markdown(
        """
        This app lets you explore a dataset using SQL and duckdb.
        The data is stored in an on-disk [duckdb](https://duckdb.org/) database,
        which leads to extremely fast queries.
        """
    )