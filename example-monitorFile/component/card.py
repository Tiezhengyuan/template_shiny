from shiny import ui

def card_logs():
    return ui.card(
        ui.card_header("Logs"),
        ui.output_data_frame("df"),
    )

def card_summary():
    return ui.card(
        ui.card_header("Log Summary"),
        ui.output_data_frame("message_counts"),
    )